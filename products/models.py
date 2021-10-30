from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    brand = models.CharField(max_length=254)
    model_name = models.CharField(max_length=254)
    product_name = models.CharField(max_length=254, null=True, blank=True)
    alternate_names = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    launched = models.CharField(max_length=254)
    console_family = models.CharField(max_length=254)
    console_type = models.CharField(max_length=254)
    input_method = models.CharField(max_length=254)
    hard_disk = models.CharField(max_length=254)
    ram = models.CharField(max_length=254)
    processor = models.CharField(max_length=254)
    weight = models.CharField(max_length=254, null=True, blank=True)
    battery_type = models.CharField(max_length=254, null=True, blank=True)
    screen_size = models.CharField(max_length=254, null=True, blank=True)
    graphics = models.CharField(max_length=254, null=True, blank=True)
    hdmi = models.CharField(max_length=254, null=True, blank=True)
    usb = models.CharField(max_length=254, null=True, blank=True)
    has_wifi = models.BooleanField(default=False, null=True, blank=True)
    ethernet = models.BooleanField(default=False, null=True, blank=True)
    memory_card = models.CharField(max_length=254, null=True, blank=True)
    av_digital_output = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.model_name
