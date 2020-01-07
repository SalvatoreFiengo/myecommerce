from django.db import models


class Product(models.Model):
    DEFAULT = "1"
    FIFTH = "2"
    TENTH = "3"
    QUARTER = "4"
    HALF = "5"
    TQUARTER = "6"
    OFFER_CHOICES = (
        (DEFAULT, '0'),
        (FIFTH, '5'),
        (TENTH, '10'),
        (QUARTER, '25'),
        (HALF, '50'),
        (TQUARTER, '75'),
    )
    EL_CO = "1"
    MO_TV_MS_GA = "2"
    TO_CH_BA = "3"
    CL_SH_WH = "4"
    HE_BE = "5"
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
    offer = models.CharField(max_length=2, choices=OFFER_CHOICES, default=DEFAULT)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default=None, blank=False)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
