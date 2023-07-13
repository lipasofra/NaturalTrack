# Natural Track
## Equipo 1
_This is a project made for Globant AICodefest 2023_<br />
***This project was one of the two FINALIST in Colombia***

### Members:
* Lina Soler
* Andrés Soler
* Carlos Escobar
* Daniel Mercado
* Cristian Pimienta

## About the project
This is a webapp where you can obtain different forms of data related to natural disasters around the globe..
Is divided in two categories:
1. For general people who wants fast and easy answers about a specific question. This uses a text field where user can type a question and a IA tool would bring the related answer according to the data we have.
* This section brings another text field where you can enter your email to obtain a random fact about global disasters in your email
2. For more especialized users who seek in-depth insights into data analysis. This section bring an embed tool with filters and graphs about globa natural disasters (same data based of the first section).
* This section also has a filter integrated with AI, where the user can type a prompt about data.

Can be found video and pictures of the app in [here](https://drive.google.com/drive/folders/1z057wunoBALP0EGrnFtPyDk2zP3eaov2?usp=sharing)
## Technologies
This app uses React.js in frontend and Python in backend. Both communicates with the backend API (so first section could be used directly from API). <br />
The embed is build in HEX. And can be found in [here](https://app.hex.tech/2f4305db-d567-4b07-8c33-652d7eb206c5/app/ed7149ad-9ca0-4662-a838-a0ec735ec38b/latest). <br />
And the data was obtained from [kaggle](https://www.kaggle.com/datasets/brsdincer/all-natural-disasters-19002021-eosdis)

## Run it
For the frontend `npm i` and `npm run start`.<br />
For backend `pip install -r requirements.txt` and `python manage.py runserver`.<br />
(Having the techonologies required installed previously)<br />
Take in account the template of the environment variables: the API_KEY to the AI tool integration and the USER and PASSWORD for email sending.
