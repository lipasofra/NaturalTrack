import csv
from pprint import pprint

def read_csv_1900():
    file_path = '/Users/andres/Documents/programacion/codefest/Equipo-1/backend/disasters/1900.csv'
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Read the header row
        header = [key.lower().replace(' ', '_').replace("_('000_us$)", '') for key in header]

        
        integer_fields = [
            'year',
            'seq',
            'dis_mag_value',
            'start_year',
            'start_month',
            'start_day',
            'end_year',
            'end_month',
            'end_day',
            'total_deaths',
            'no_injured',
            'no_affected',
            'no_homeless',
            'total_affected',
            'insured_damages',
            'total_damages',
            'reconstruction_costs',
        ]

        data = [
            {key: value.strip() if value != '' else 'null' for key, value in zip(header, row)}
            for row in reader
        ]

        for row in data:
            for field in integer_fields:
                if field not in row:
                    row[field] = 0
                if row[field] != 'null':
                    row[field] = int(row[field])
                if row[field] == 'null':
                    row[field] = 0

        # for row in data:
        #     for key, value in row.items():
        #         if key not in integer_fields and value != 'null':
        #             if len(value) > 255 and key != 'location' and key != 'geo_locations':
        #                 print(key)

        decimal_fields = [
            'cpi',
        ]

        for row in data:
            for field in decimal_fields:
                if field not in row:
                    row[field] = 0.0
                if row[field] != 'null':
                    row[field] = float(row[field])
                if row[field] == 'null':
                    row[field] = 0.0

        return data
    
def read_csv_1970():
    file_path = '/Users/andres/Documents/programacion/codefest/Equipo-1/backend/disasters/1970.csv'
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Read the header row

        # transform the keys to be lower case and if it has a space add a _
        header = [key.lower().replace(' ', '_').replace("_('000_us$)", '') for key in header]

        integer_fields = [
            'year',
            'seq',
            'dis_mag_value',
            'start_year',
            'start_month',
            'start_day',
            'end_year',
            'end_month',
            'end_day',
            'total_deaths',
            'no_injured',
            'no_affected',
            'no_homeless',
            'total_affected',
            'insured_damages',
            'total_damages',
            'reconstruction_costs'
        ]

        data = [
            {key: value if value != '' else 'null' for key, value in zip(header, row)}
            for row in reader
        ]

        for row in data:
            for field in integer_fields:
                if field not in row:
                    row[field] = 0
                if row[field] != 'null':
                    row[field] = int(row[field])
                if row[field] == 'null':
                    row[field] = 0

        decimal_fields = [
            'cpi',
        ]

        for row in data:
            for field in decimal_fields:
                if field not in row:
                    row[field] = 0.0
                if row[field] != 'null':
                    row[field] = float(row[field])
                if row[field] == 'null':
                    row[field] = 0.0

        field_delete = [
            'dis_no',
        ]

        for row in data:
            for field in field_delete:
                del row[field]

        return data
    

