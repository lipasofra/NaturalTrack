#%%
import pandas as pd
df = pd.read_csv('sample_data/disasters_1970_2021.csv')
import plotly.express as px

#%%
df = df[df['Disaster Type'] == 'Earthquake']
#fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", zoom=3)

#%%

import plotly.express as px

fig = px.choropleth_mapbox(df, locations='fips', color='unemp',
                           lat="Latitude", lon="Longitude",
                           #color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

# %%

import pandas as pd
import numpy as np
import requests

#%%
import requests

def get_all_countries():
    url = "https://restcountries.com/v2/all"
    response = requests.get(url)
    data = response.json()

    country_lat_long = {}

    for country in data:
        name = country['name']
        latlng = country.get('latlng', [])
        if len(latlng) == 2:
            country_lat_long[name] = tuple(latlng)

    return country_lat_long

countries = get_all_countries()
print(countries)

#%%
def add_lat_long(df, countries):
    # Check if 'Country' is in dataframe columns
    if 'Country' not in df.columns:
        raise ValueError("DataFrame must contain a 'Country' column.")

    # Create separate lists for lat and long
    df['lat'] = df['Country'].apply(lambda x: countries[x][0] if x in countries else np.nan)
    df['long'] = df['Country'].apply(lambda x: countries[x][1] if x in countries else np.nan)
    
    return df


#%%

def add_lat_long(df):
    def get_lat_lon(country):
        response = requests.get(f"https://restcountries.com/v2/name/{country}")
        if response.status_code == 200:
            data = response.json()
            if data:
                latlng = data[0]['latlng']
                return pd.Series((latlng[0], latlng[1]))

    df[['Latitude', 'Longitude']] = df['Country'].apply(get_lat_lon)
    return df


# %%
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")

# List of countries. It's a big list, so I'm only showing a few here, but you can replace this list with all countries.
list_of_countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", 
                     "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", 
                     "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", 
                     "Burkina Faso", "Burundi", "Côte d'Ivoire", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", 
                     "Chad", "Chile", "China", "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica", "Croatia", "Cuba", 
                     "Cyprus", "Czechia", "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", 
                     "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", 
                     "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", 
                     "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Holy See", "Honduras", "Hungary", "Iceland", "India", 
                     "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", 
                     "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", 
                     "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", 
                     "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", 
                     "Mozambique", "Myanmar (formerly Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", 
                     "Niger", "Nigeria", "North Korea", "North Macedonia (formerly Macedonia)", "Norway", "Oman", "Pakistan", "Palau", 
                     "Palestine State", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", 
                     "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", 
                     "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", 
                     "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", 
                     "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", 
                     "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", 
                     "United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Zambia", 
                     "Zimbabwe"]

country_lat_long = {}

for country in list_of_countries:
    location = geolocator.geocode(country)
    if location:
        country_lat_long[country] = (location.latitude, location.longitude)

print(country_lat_long)

# %%

import requests

url = "https://restcountries.com/v2/all"
response = requests.get(url)
data = response.json()
#%%

country_lat_long = {}

for country in data:
    name = country['name']
    latlng = country.get('latlng', [])
    if len(latlng) == 2:
        country_lat_long[name] = tuple(latlng)


#countries = get_all_countries()
#print(countries)

# %%
