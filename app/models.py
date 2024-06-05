from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class sportovec(models.Model):
    jmeno = models.CharField(max_length=80, verbose_name='Jméno sportovce', help_text='Zadejte jméno sportovce')
    prijmeni = models.CharField(max_lenght=80, verbose_name='Příjmení sportovce', help_text='Zadejte příjmení sportovce')
    narodnost = models.CharField(max_lenght=50, verbose_name='Národnost sportovce', help_text='Zadejte národnost sportovce')
    narozeni = models.DateField(blank=True, null=True, verbose_name='Datum narození sportovce')
    vaha = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(1000), MinValueValidator(35)], verbose_name='Váha sportovce v kg')
    vyska = models.PositiveIntegerField(blank=True,null=True, validators=[MaxValueValidator(250), MinValueValidator(130)], verbose_name='Výška sportovce v cm')
