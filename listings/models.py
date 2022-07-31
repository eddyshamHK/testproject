from django.db import models
from datetime import datetime
from realtors.models import Realtor
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_nonzero(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s is smaller than 0. Input cannot be negative!'),
            params={'value': value},
        )

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    descriptionListing = models.TextField(blank=True)
    price = models.IntegerField(validators=[validate_nonzero])
    bedrooms = models.IntegerField(validators=[validate_nonzero])
    bathrooms = models.DecimalField(
        validators=[validate_nonzero], max_digits=2, decimal_places=1)
    garage = models.IntegerField(validators=[validate_nonzero])
    sqft = models.IntegerField(validators=[validate_nonzero])
    lot_size = models.DecimalField(
        validators=[validate_nonzero], max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
