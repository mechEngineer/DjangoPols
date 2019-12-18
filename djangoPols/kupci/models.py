from django.db import models
from django.urls import reverse
import datetime
from django.utils import timezone
from phonenumber_field.modelsfields import PhoneNumberField


# Create your models here.

class Kupci(models.Model):
    naziv_tvrtke = models.CharField(max_length=50, blank=False, null=False)
    vatid = models.CharField(max_length=20, unique=True, blank=True, null=True)
    street = models.CharField(max_length=35, blank=True, null=True)
    street_number = models.CharField("Street number", max_length=10)
    zip_code = models.CharField(_("Postanski broj"), max_length=15)
    city = models.CharField(_("Grad"), max_length=30)
    country = models.CharField(_("Drzava"), max_length=20)
    phone_no = models.PhoneNumberField(_("Telefon"), blank=True, null=True),
    fax_no = models.PhoneNumberField(_("Fax"), blank=True, null=True),
    email = models.EmailField(
        _("Email adresa"), max_length=254, blank=True, null=True)
    note = models.TextField(_("Napomena"), blank=True, null=True)
    created = models.DateField(
        _("Kreirano"), auto_now=False, auto_now_add=True)
    modified = models.DateField(
        _("Izmjenjeno"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("Kupci")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Kupci_detail", kwargs={"pk": self.pk})
