import json
from django.core.management.base import BaseCommand
from pprint import pprint
from django.contrib.auth.models import Group, Permission
import csv
from apps.main.models import disasters19002021, disasters19702021, Disasters
from utils import read_csv
from pprint import pprint

class Command(BaseCommand):
    help = 'Import disasters from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='name of the file')

    def handle(self, *args, **options):
        if options['file'] == '1900':
            data = read_csv.read_csv_1900()

            # delete data from table
            disasters19002021.objects.all().delete()
            print('deleted data')
            
            for row in data:
                disasters19002021.objects.create(**row)
        elif options['file'] == '1970':
            data = read_csv.read_csv_1970()

            # delete data from table
            disasters19702021.objects.all().delete()
            print('deleted data')

            for row in data:
                disasters19702021.objects.create(**row)

        else:
            data = read_csv.read_csv_1900()

            Disasters.objects.all().delete()
            print('deleted data')

            for row in data:
                Disasters.objects.create(**row)

            data = read_csv.read_csv_1970()

            for row in data:
                Disasters.objects.create(**row)


        

