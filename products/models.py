from django.db import models


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
    price = models.DecimalField(max_digits=6, decimal_places=2)
    offer = models.DecimalField(max_digits=6, decimal_places=2, choices=OFFER_CHOICES, default=DEFAULT)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default=None, blank=False)
    discount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
