from django.db import models
from django.urls import reverse
import datetime
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Tvrtke(models.Model):
    naziv_tvrtke = models.CharField(max_length=50, blank=False, null=False)
    vatid = models.CharField(max_length=20, unique=True, blank=True, null=True)
    street = models.CharField(max_length=35, blank=True, null=True)
    street_number = models.CharField("Street number", max_length=10)
    zip_code = models.CharField("Postanski broj", max_length=15)
    city = models.CharField("Grad", max_length=30)
    country = models.CharField("Drzava", max_length=20)
    phone_no = PhoneNumberField("Telefon", blank=True, null=True),
    fax_no = PhoneNumberField("Fax", blank=True, null=True),
    email = models.EmailField(
        "Email adresa", max_length=254, blank=True, null=True)
    note = models.TextField("Napomena", blank=True, null=True)
    created = models.DateField(
        "Kreirano", auto_now=False, auto_now_add=True)
    modified = models.DateField(
        "Izmjenjeno", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = ("Kupci")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Kupci_detail", kwargs={"pk": self.pk})


class Kontakti(models.Model):
    tvrtka = models.ForeignKey('Tvrtke', on_delete=models.CASCADE)
    ime = models.CharField("Ime", max_length=50, blank=False, null=False)
    prezime = models.CharField("Prezime", max_length=50, blank=False, null=False)
    titula = models.CharField("Titula", max_length=20, blank=True, null=True)
    pozicija = models.CharField("Pozicija", max_length=20, blank=True, null=True)
    odjel = models.CharField("Odjel", max_length=25, blank=True, null=True)
    email = models.EmailField("Email", max_length=50, 
    blank=True, null=True)
    phone_contact = PhoneNumberField("Telefon", blank=True, null=True)
    mobile_contact = PhoneNumberField("Mobitel", blank=True, null=True)
    napomena = models.TextField("Napomena", blank=True, null=True)
    created = models.DateField("Kreirano", auto_now=False, auto_now_add=True)
    modified = models.DateField("Kreirano", auto_now=True, auto_now_add=False)

    def full_name(self):
        fullname = self.ime + ' ' + self.prezime
        return fullname

    def __str__(self):
        return 

    def __unicode__(self):
        return 

class TipTvrtke(models.Model):
    DOB = 'D'
    KUP = 'K'
    TIPOVI_TVRTKI = [
        (DOB, 'Dobavaljač'),
        (KUP, 'Kupac')
    ]
    tvrtka = models.ForeignKey("Tvrtke", verbose_name="Tip tvrtke", on_delete=models.SET_NULL, blank=True, null=True)
    tip_tvrtke = models.CharField(max_length=2, choices=TIPOVI_TVRTKI, default=KUP)

    

    def __str__(self):
        return 

    def __unicode__(self):
        return 

