from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from helper.variables import categories


class Product(models.Model):
    DEFAULT = 0
    FIFTH = 5
    TENTH = 10
    QUARTER = 25
    HALF = 50
    TQUARTER = 75
    OFFER_CHOICES = (
        (DEFAULT, 0),
        (FIFTH, 5),
        (TENTH, 10),
        (QUARTER, 25),
        (HALF, 50),
        (TQUARTER, 75),
    )
    EL_CO = "Electronic & Computers"
    MO_TV_MS_GA = "Movies, TV, Music & Games"
    TO_CH_BA = "Toys, Children & Baby"
    CL_SH_WH = "Clothes, Shoes & Whatces"
    HE_BE = "Health & Beauty"
    CATEGORY_CHOICES = (
        (EL_CO, categories["EL_CO"]),
        (MO_TV_MS_GA, categories["MO_TV_MS_GA"]),
        (TO_CH_BA, categories["TO_CH_BA"]),
        (CL_SH_WH, categories["CL_SH_WH"]),
        (HE_BE, categories["HE_BE"]),        
    )

    vendor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False)
    name = models.CharField(max_length=25, default='')
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    offer = models.DecimalField(max_digits=8, decimal_places=2, choices=OFFER_CHOICES, default=DEFAULT)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default=None)
    discount = models.DecimalField(max_digits=9, decimal_places=2, default=0, editable=False)
    stock = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Product)
def save_product_background(sender, instance, **kwargs):
    """after instance of Product model is saved, check if offer is greater of 0 
    if so assign a discount to the product """

    if instance.offer > 0:
        offer_amount = (instance.offer/100)*instance.price
        instance.discount = instance.price - offer_amount
        instance.discount = "%.2f" % instance.discount
        
  

