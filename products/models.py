from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from helper.variables import background


class Product(models.Model):
    DEFAULT = 0
    FIFTH = 5
    TENTH = 10
    QUARTER = 25
    HALF = 50
    TQUARTER = 75
    OFFER_CHOICES = (
        (DEFAULT, "0"),
        (FIFTH, "5%"),
        (TENTH, "10%"),
        (QUARTER, "25%"),
        (HALF, "50%"),
        (TQUARTER, "75%"),
    )
    EL_CO = "Electronic & Computers"
    MO_TV_MS_GA = "Movies, TV, Music & Games"
    TO_CH_BA = "Toys, Children & Baby"
    CL_SH_WH = "Clothes, Shoes & Whatces"
    HE_BE = "Health & Beauty"
    CATEGORY_CHOICES = (
        (EL_CO, 'Electronic & Computers'),
        (MO_TV_MS_GA, 'Movies, TV, Music & Games'),
        (TO_CH_BA, 'Toys, Children & Baby'),
        (CL_SH_WH, 'Clothes, Shoes & Whatces'),
        (HE_BE, 'Health & Beauty'),        
    )

    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    offer = models.DecimalField(max_digits=8, decimal_places=2, choices=OFFER_CHOICES, default=DEFAULT)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default=None, blank=False)
    discount = models.DecimalField(max_digits=9, decimal_places=2, default=0, editable=False)
    stock = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    background = models.CharField(max_length=100, default="/media/images/background.jpg", editable=False)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.name

@receiver(post_save, sender=Product)
def save_product_background(sender, instance, **kwargs):
    """after instance of Product model is saved, check if its category is in 'background dict'
    if so assign it to the new product background parameter"""

    if instance.category in background:
        instance.background = background[instance.category]
