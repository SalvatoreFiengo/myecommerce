# My-Ecommerce

My-Ecommerce is an e-commerce website that allows to buy online but also allows the user to post their own items.
Includes a profile section, in which users can update their own data.
All products can be uploaded with an image, description, price and offer.
Also best offers will be included in a carousel as presentation to the main page
My-Ecommerce has implemented Stripe for testing transactions, therefore won't accept real credit card numbers
Although it is possible to experience My-Ecommerce checkout system using (Stripe test credit card numbers)[https://stripe.com/docs/testing#cards].
 
## UX
 
User Stories:

- As a user, I want to visit the main page and all informative sections without having to register/login.
- As a user, I want to be able to register/log in to have access to other sections of the website.
- As a user, I want to be able to modify my profile and save information the website will remember for me.
- As a buyer, once logged in, I want to select a product and choose its quantity then add it to my cart.
- As a vendor, I wanto to be able to add my items so others can buy them
- As a vendor, I wanto my items to have a reference to my username
- As a vendor, I wanto to be able to review/modify my items in a page only i can visit

Project Mocks can be found in project-mocks folder as PNG files
database structure showing modificaitons to standard Django database can be found in project-mocks folder as ecommerce_database.png

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
1. Registration allows user to register and redirects to edit profile page in case user wants to add more information.
    -   success or failure in registering to website will result in a modal showing related message
2. Log in allows user to log into the website and have access to his profile, his own products and cart
    -   success or failure in registering to website will result in a modal showing related message
3. Reset password allows user to request an email and have his/her password reset 
    -   success or failure in registering to website will result in a modal showing related message
4. All auth features render an empty index page that redirects to main page.  
    this extra step is meant to be there to easily add a presentation view,   
    such as "your favourite purchases" and other information going forward
5. Base.html: basic template for all pages, 
    - includes filter and search capabilities 
    - carousel visible only if related information are provided in the template
6. main page, /products/,
    - shows product with offers at screen via a carousel, 
    - can filter by category and a search 
    - then presents all products 
7. product details, 
    - accessible by main page, allows user to review products details
8. profile,
    - allows user to insert his/her information extending the user model
    - information useful to easier checkout are included and can be modified here
9. your products,
    - if user is also a vendor he/she can add and edit his/her products in this section
10. cart
    - allows user to review what is added to cart
    - allows quantity adjustments and checkout
11. checkout
    - form with information about order 
    - form to add a credit card
    - checkout credit card client and server validation to reduce api calls to stripe  
### Existing Features
- Feature 1 - allows users to register to website by having them fill out registration form: email username and password
    -   validation on email: basic client validation and server side check if it is empty (cannot be empty)
- Feature 2 - allows users to log in into website by fill out login form with username/email and password
- Feature 3 - allows users to reset password by providing email address
    - sends an email via smtp with a secure link to reset password
    - allows user to reset by providing password an its confirmation
    - inform user if password reset is successful
- Feature 6 - allows users to surf the main page providing informaiton about current offers 
    - allows filtering and search
    - allows to surf other pages via nav buttons and product details via product preview section
    - allows user to add product to cart specifying quantity (not required) via product preview section
- Feature 7 - allows users to review informaiton about a single product
    - allows user to add product to cart specifying quantity (not required)
- Feature 8 - allows users to insert information related to his/her profile by filling profile form
    - allows user to select if they are vendor by clicking related button and so doing give access to "your products" section
    - information from profile can be used to pre populate checkout form (not credit card)
- Feature 9 - allows vendors to add delete or edit their own products
    -   allows vendors to preview products added, edited 
- Feature 10 - allows users to review their shopping cart
    -  allows users to adjust item quantities by clicking plus minus buttons displaying total based on quantity
    -  if product has an offer total will count in discounted price
- Feature 11 - allows users to fill their shipping information and credit card informaiton then to pay
    - shipping information are retrieved from profile if present
    - credit card informaiton are checked client side and server side to reduce http call to stripe api
    - messages reporting any errors are displayed, client side as errors in form, serverside as errors in modal 

### Features Left to Implement
- Extend profile with a publishable section for vendors available to users that want to know what else they sell 
- Feedbacks about products and vendors
- "index" to be populated wiht "your favourites" "chosen for you" and newsletter

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [Python 3](https://www.python.org/download/releases/3.0/)
    - The project uses **Python 3** as base language for its backend
- [Django 1.11.24](https://docs.djangoproject.com/en/3.0/releases/1.11.24/)
    - The project uses **Django** to ease the creation of complex, database-driven websites
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Bootstrap 3](https://getbootstrap.com/docs/3.3/)
    - The project uses **Bootstrap** to simplify layout developing and provide Gliphycon icons.
- [Amazon s3](https://aws.amazon.com/free/storage/?trk=ps_a131L000005OOOyQAO&trkCampaign=UK&sc_channel=PS&sc_campaign=acquisition_UK&sc_publisher=Google&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Storage|S3|UK|EN|Text&sc_content=s3_e&sc_detail=amazon%20s3&sc_category=S3&sc_segment=293639776553&sc_matchtype=e&sc_country=UK&s_kwcid=AL!4422!3!293639776553!e!!g!!amazon%20s3&ef_id=EAIaIQobChMImMaQhv-j5wIViZntCh3U1QfPEAAYASAAEgJujPD_BwE:G:s)
    - The project uses **AWS S3** to store media and static files
- [Heroku](https://dashboard.heroku.com/apps)
    - The project uses **Heroku** to host the application
- [Travis](https://travis-ci.com/)
    - The project uses **Travis** to build and test the software in connection to github 
- [Stripe](https://stripe.com/ie)
    - The project uses **Stripe** to test credit card payments
- [Fontawesome](https://fontawesome.com/)
    - The project uses **Fontawesome** to provide icons

## Testing


[![Build Status](https://travis-ci.com/SalvatoreFiengo/myecommerce.svg?branch=master)](https://travis-ci.com/SalvatoreFiengo/myecommerce)

- tested html with [html W3 validator](https://validator.w3.org/)
- tested CSS with [CSS W3 validator](https://jigsaw.w3.org/css-validator/validator)
- Python tested with [PEP8 online](http://pep8online.com/)
- Javascript tested with [Esprima](https://esprima.org/demo/validate.html) and [Jshint](https://jshint.com/)

Other users used My-ecommerce and reported any errors encountered.
They registered, logged in, tested checkout and added their own products

Automated tests are included in test.py for each app: accounts, helper, product, product_manager, cart
Total automated tests 18
To perform automated tests db.SQLite has been used 
in ecommerce.settings added 
- import sys
- if "test" in sys.arg then run db.sqlite3 as default database 

1. Login form:
    1. Go to the "Home" page
    2. click on Sign in
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears and user redirect to home.
2. Registration form:
    1. Go to the "Home" page
    2. Click on Sign up
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with an existing email address and verify that a relevant error message appears
    5. Try to submit the form with a password and invalid confirmation and verify that a relevant error message appears
    6. Try to submit the form with all inputs valid and verify that a success message appears and user redirect to profile page.
3. Password reset:
    1. Click on sign in
    2. Click on reset password
    3. Try to submit the empty form and verify that an error message about the required fields appears
    4. Try to submit the form with all inputs valid and verify that a success message appears and email is received.
    -   1. click on link provided via email
        2. Try to submit the empty form and verify that an error message about the required fields appears
        3. Try to submit the form with password and invalid confirmation an verify that an error message appears
        4. Try to submit the form with all inputs valid and verify that a success message appears.
4. Cart:
    1. Click on Cart 
    2. verify that a message displaying no items are available is present
    3. go to home
    4. try add to cart without specifying quantity and ensure badge with number items chosen is added to cart icon
    5. click on cart 
    6. verify that correct number of items is shown
    7. verify total is correct
    8. repeat from 4 to 7 adding another item
    9. try add specifying quantity from home page and check is shown in cart
    10. try add and deduct quantity from cart and verify page is updated correctly
5. Checkout:
    1. Go to home
    2. Add item to cart
    3. Click checkout
    4. Verify missing information in order or credit card forms throw a "paymetn form" error
    5. Verify error are shown for every field missing info in order form
    6. Verify wrong credit card number form information throws shows an error in credit card form
    7. Verify any error on backend (Stripe) is correctly shown via message on screen
6. User Profile:
    1. Click on Profile
    2. Verify "Your Products" button is not visible
    3. Click on edit profile
    4. Try to submit the empty form and verify that an error message about the required fields appears
    5. Try to submit the form and verify that profile is updated correctly
    6. Try to submit the form after changing vendor status and verify "Your Products" button is visible in profile
7. User products - add/edit product:
    1. Click on Profile
    2. Click on "Your Products"
    3. Verify your products page loads correctly
    4. Click on add product
    5. Verify modal with form is empty
    6. Try to submit the empty form and verify that an error message about the required fields appears specifying page 1
    7. Try to submit the empty form  in page 2 and verify that an error message about the required fields appears specifying page 2
    8. Try to submit the form with an image greater than 500kb and verify that an error message appears specifying page 1
    9. Try to submit the form with stock equal to 0 and verify that an error message appears specifying page 2
8. search:
    1. Input search
    2. Verify error message is shown if no item are found
    3. Verify perfect match is shown 
    4. verify partial input is shown if contains partial input in product name 
9. filter:
    1. select category and click filter
    2. verify only products with same category are shown
    3. verify if no items in category a message is shown

On x-small, small screens nav collapese showing a menu icon 
No major issues spotted on IE or Edge

### Bugs/issues encountered:
  
- due to old migrations got error **invalid literal for int() with base 10: 'Select'** when migrating to postgresql in heroku:
- launched 
    1. find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
    2. find . -path "*/migrations/*.pyc"  -delete
    3. then had to reinstall django --> fixed

- access denied by s3boto3 to static files in media folder
    -  Django is suspicious of relative path starting with "/"
    - dashes removed

## Deployment

### Github deployment:
Deployed as per instructions on Github, 
files not pushed (in .gitignore file):
- "__pycache__/"
- "accounts/__pycache__/"
- "accounts/migrations/__pycache__/"
- "db.sqlite3"
- "env.py"
- "myecommerce/__pycache__/"
- "products/__pycache__/"
- "products/migrations/__pycache__/"
- "virtual/"
- "media/"
- "static/"
- "*.png"
### Heroku deployment:
1. Created requirements.txt
2. Procfile pointing to gunicorn
3. Added an app to heroku
4. activated postgres addon (database provided by Heroku)
5. set environment variables: 
    - AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY to get static and media files from S3
    - DATABASE_URL 
    - DISABLE_COLLECTSTATIC: 1, collectstatic will be run only via console
    - EMAIL_ADDRESS, EMAIL PASSWOD, to provide email when resetting passwords
    - SECRET_KEY, Django secret key
    - STRIPE_PUBLISHABLE, STRIPE_SECRET, stripe publishable and secret keys to get access to stripe apis
6. Connected Heroku to Github
7. Click on Deploy Branch
(not a fan of Enable automatic deploys)

### Local deployment:
All environment variables are stored in an env.py file that imports "os" and calls os.environ.setdefault to set them
1. set environment variables: 
    - AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY to get static and media files from S3
    - DATABASE_URL
    - EMAIL_ADDRESS, EMAIL PASSWOD, to provide email when resetting passwords
    - SECRET_KEY, Django secret key
    - STRIPE_PUBLISHABLE, STRIPE_SECRET, stripe publishable and secret keys to get access to stripe apis 

Worth to mention I used a virtual environment to install dependencies and run application locally
Virtual environment named virtual
To access Virtual environment: source virtual/scripts/activate
Then to run the project locally: python manage.py runserver

## Credits
Many thanks to:
- Code Accademy tutorials from which I used and modified authentication, cart and checkout
- [Stack Overflow](https://stackoverflow.com/) and [Martavis P.](https://stackoverflow.com/users/2693236/martavis-p) 
    - which helped with a CSS solution: 
        [Bootstrap 3 navbar-collapse absolute](https://stackoverflow.com/questions/23403923/make-bootstrap-3-collapsed-menu-overlay-page) 

- [simpleisbetterthancomplex](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)
    - which helped with "how to extend django user model"

### Media
- favicon image,(Shop icon)[https://icons8.com/icons/set/shop--v4]  from: (Icons8)[https://icons8.com]
- The photos used in this site were obtained from [Freepik](http://www.freepik.com)
    -  white background: [Background vector created by starline - www.freepik.com](https://www.freepik.com/free-photos-vectors/background)
    - Backgroung images and laptop:
        - [Background vector created by freepik - www.freepik.com](https://www.freepik.com/free-photos-vectors/background)
        - [Technology photo created by freepik - www.freepik.com](https://www.freepik.com/free-photos-vectors/technology)
    - default/empty image
        - Icons made by flaticon downloaded on  [freepik](https://www.flaticon.com/authors/freepik) originally from [www.flaticon.com](https://www.flaticon.com/)

    - Beauty section: 
        - lotion:
            [Background photo created by freepik - www.freepik.com](https://www.freepik.com/free-photos-vectors/background)
        -   background <a href="https://www.freepik.com/free-photos-vectors/background">Background photo created by freepik - www.freepik.com</a>
    - Music Movies and Games
        - [Background photo created by freepik - www.freepik.com](https://www.freepik.com/free-photos-vectors/background)
    - Toys children
        - [Children photo created by freepik - www.freepik.com](https://www.freepik.com/free-photos-vectors/children)
    - add a product: 
        - [Background photo created by rawpixel.com - www.freepik.com](https://www.freepik.com/free-photos-vectors/background)

- products added by users:
    -   I had to change some pictures for copyright reasons:
        -   Miracle Body Lotion : [Fashion psd created by freepik - www.freepik.com](https://www.freepik.com/free-photos-vectors/fashion)
        -   graphic card & My Thoughts: [link](https://www.pxfuel.com/en/free-photo-exqda/download/1024x768) 

