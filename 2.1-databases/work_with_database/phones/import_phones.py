import csv
from django.core.management.base import BaseCommand
from .models import Phone


class Command(BaseCommand):
    help = 'Import phones from csv file'
    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)
            for row in reader:
                phone = Phone(
                    id=row[0],
                    name=row[1],
                    image=row[2],
                    price=row[3],
                    release_date=row[4],
                    lte_exists=row[5]
                )
                phone.save()