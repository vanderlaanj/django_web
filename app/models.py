from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Sportovec(models.Model):
    jmeno = models.CharField(max_length=80, verbose_name='Jméno sportovce', help_text='Zadejte jméno sportovce')
    prijmeni = models.CharField(max_length=80, verbose_name='Příjmení spoertovce', help_text="Zadejte jméno sportovce")
    narodnost = models.CharField(max_length=50, verbose_name='Národnost sportovce', help_text='Zadejte národnost sportovce')
    narozeni = models.DateField(blank=True, null=True, verbose_name='Datum narození sportovce')
    vaha = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(1000), MinValueValidator(35)], verbose_name='Váha sportovce v kg')
    vyska = models.PositiveIntegerField(blank=True,null=True, validators=[MaxValueValidator(250), MinValueValidator(130)], verbose_name='Výška sportovce v cm')
    tym = models.ForeignKey('tym',verbose_name='Tým sportovce', on_delete=models.CASCADE)

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = 'Sportovec'
        verbose_name_plural = 'Sportovci'

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'

class Tym(models.Model):
    nazev = models.CharField(max_length=100, verbose_name='Název týmu')
    sport = models.CharField(max_length=50,verbose_name='Název sportu')
    zalozeni = models.DateField(blank=True,null=True, verbose_name='Datum založení týmu')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Tým'
        verbose_name_plural = 'Tým'

    def __str__(self):
        return f'{self.nazev}'

class Akce(models.Model):
    datum = models.DateField(blank=False,null=False, verbose_name='Datum konání')
    cas = models.TimeField(blank=False,null=False,verbose_name='čas konání')
    misto = models.CharField(max_length=100,verbose_name='Místo konání')
    ucastnici = models.ManyToManyField(Sportovec)

    class Meta:
        ordering = ['datum']
        verbose_name = 'Akce'
        verbose_name_plural = 'Akce'

    def __str__(self):
        return f'{self.datum}'

