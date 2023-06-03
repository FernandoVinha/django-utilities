from django.db import models
import requests
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class Country(models.Model):
    abbreviation = models.CharField(max_length=20)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    @staticmethod
    def get_countries():
        url = "https://restcountries.com/v3.1/all"

        try:
            response = requests.get(url)
            response.raise_for_status()

            if response.status_code == 200:
                countries = response.json()
                return [(country["cca2"], country["name"]["common"]) for country in countries]

        except requests.RequestException as e:
            print(f"Erro ao obter países: {e}")
            # Ou você pode registrar a exceção em um arquivo de log

        return None


@receiver(post_migrate)
def populate_countries(sender, **kwargs):
    Country.objects.get_or_create(abbreviation="AC", name="Ancapistan")
    country_list = Country.get_countries()

    if country_list:
        countries = [
            Country.objects.get_or_create(abbreviation=abbreviation, name=name)[0]
            for abbreviation, name in country_list
        ]
        Country.objects.bulk_create(countries)
