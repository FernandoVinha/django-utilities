from django.db import models
import requests
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.files.base import ContentFile
import os


class Coin(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    precision = models.PositiveSmallIntegerField()
    _type = models.CharField(max_length=50)

    def __str__(self):
        return self.code

    @staticmethod
    def populate_currencies():
        if Coin.objects.exists():
            # Moedas já populadas, retornar
            return

        url = "https://bisq.markets/api/currencies"

        try:
            # Fazer a requisição HTTP
            response = requests.get(url)
            response.raise_for_status()  # Lançar exceção se ocorrer erro HTTP

            # Extrair os dados das moedas
            json_dict = response.json()

            # Criar objetos Coin com base nos dados
            coins = [
                Coin(code=value['code'], name=value['name'], precision=value['precision'], _type=value['_type'])
                for key, value in json_dict.items()
            ]

            Coin.objects.bulk_create(coins)  # Criar objetos no banco de dados de forma mais eficiente

        except (requests.RequestException, ValueError) as e:
            # Lidar com erros de conexão ou resposta inválida
            print(f"Erro ao popular moedas: {e}")
            # Ou você pode registrar a exceção em um arquivo de log


@receiver(post_migrate)
def on_post_migrate(sender, **kwargs):
    Coin.populate_currencies()
