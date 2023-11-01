import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone_data in phones:
            phone = Phone()
            phone.name = phone_data['name']
            phone.image = phone_data['image']
            phone.price = phone_data['price']
            phone.release_date = phone_data['release_date']
            phone.lte_exists = phone_data['lte_exists']
            phone.slug = phone_data['slug']
            phone.save()
