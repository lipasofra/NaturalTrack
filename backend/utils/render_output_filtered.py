from apps.main.models import Disasters
import random
from pprint import pprint
from disaster_explorer.query_agent import run_query_disaster_alone

def render_message_data():

    year_range = [1900, 2021]
    
    # get a random year between 1900 and 2021
    year = random.randint(year_range[0], year_range[1])

    # get a random disaster from the database
    disaster = Disasters.objects.filter(year=year).order_by('?').first()

    
    response = run_query_disaster_alone(
        query='give me an important analysis of this disaster',
        disaster_dict=disaster,
    )

    print(response)


    
