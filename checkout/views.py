from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from products.models import Product
from helper.variables import background
import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                price = product.discount if product.offer > 0 else product.price
                total += quantity * price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
                if customer.paid:
                    messages.success(
                        request, "You have successfully paid", extra_tags="Transaction Successful")
                    for id, quantity in cart.items():
                        product = get_object_or_404(Product, pk=id)
                        product.stock -= quantity
                        product.save() 
                    request.session['cart'] = {}
                    return redirect(reverse('products'))
                else:
                    messages.error(request, "Unable to take payment")
            except stripe.error.CardError:
                error_message = "Your card was declined, please try a different card"
                messages.error(request, error_message,
                               extra_tags="Card Not Accepted")
                pass
            except stripe.error.RateLimitError as e:
                # Too many requests made to the API too quickly
                error_message = e.json_body["error"]
                messages.error(request, f"{error_message.get('message')}",
                               extra_tags="Too many attempts")
                pass
            except stripe.error.InvalidRequestError as e:
                # Invalid parameters were supplied to Stripe's API
                error_message = e.json_body["error"]
                messages.error(request, f"{error_message.get('message')}",
                               extra_tags="Invalid Request Error")
                pass
            except stripe.error.AuthenticationError as e:
                # Authentication with Stripe's API failed
                # (maybe you changed API keys recently)
                error_message = "Please contact Website administrator"
                messages.error(request, error_message,
                               extra_tags="Unknown Error")
                print(+e.json_body["error"])
                pass
            except stripe.error.APIConnectionError as e:
                # Network communication with Stripe failed
                error_message = e.json_body["error"]
                messages.error(request, f"{error_message.get('message')}",
                               extra_tags="Network Error")
                pass
            except stripe.error.StripeError as e:
                # Display a very generic error to the user, and maybe send
                # yourself an email
                error_message = e.json_body["error"]
                messages.error(request, f"{error_message.get('message')}",
                               extra_tags="Generic Error")
                pass
            except Exception as e:
                # any other error
                error_message =e.json_body["error"]
                messages.error(request, f"{error_message.get('message')}",
                               extra_tags="Card Not Accepted")
                pass

        else:
            messages.error(
                request, "Please review and amend any error in your paymetn form", extra_tags="Payment form")
    else:
        user_data = {'full_name': request.user.first_name+" "+request.user.last_name,
                     'phone_number': request.user.userprofile.phone_number,
                     'country': request.user.userprofile.country,
                     'post_code': request.user.userprofile.post_code,
                     'town_or_city': request.user.userprofile.town_or_city,
                     'street_address1': request.user.userprofile.street_address1,
                     'street_address2': request.user.userprofile.street_address2,
                     'county': request.user.userprofile.county
                     }
        payment_form = MakePaymentForm()
        order_form = OrderForm(initial=user_data)
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE, "background_image": background["default"]})
