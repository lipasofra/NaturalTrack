import json
from django.core.management.base import BaseCommand
from pprint import pprint
from django.contrib.auth.models import Group, Permission
import csv
from pprint import pprint

class Command(BaseCommand):
    help = 'Import menus send dta from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)  # Read the header row
            
            # Infer the schema from the first row of data
            data_row = next(reader)
            schema = []
            for value in data_row:
                if value.isdigit():
                    column_type = int
                elif value.replace('.', '', 1).isdigit():
                    column_type = float
                else:
                    column_type = str
                schema.append((value, column_type))

            pprint(schema)



    # def get_csv_schema(file_path):
    #     with open(file_path, 'r') as csvfile:
    #         reader = csv.reader(csvfile)
    #         header = next(reader)  # Read the header row

    #         # Infer the schema from the first row of data
    #         data_row = next(reader)
    #         schema = []
    #         for value in data_row:
    #             if value.isdigit():
    #                 column_type = int
    #             elif value.replace('.', '', 1).isdigit():
    #                 column_type = float
    #             else:
    #                 column_type = str
    #             schema.append((value, column_type))

    #     return schema
