import requests
from bs4 import BeautifulSoup

# specify the URL of the website to be scraped
url = 'https://unprotected-shoestore.maxfrancis.me/'

# create a session object to persist cookies across requests
session = requests.Session()

# send a GET request to the website and store the response
response = session.get(url)

# create a BeautifulSoup object by passing in the response text and specify the parser
soup = BeautifulSoup(response.text, 'html.parser')

# find the login form on the webpage
form = soup.find('form', {'id': 'login-form'})

# extract the CSRF token from the form data
csrf_token = form.find('input', {'name': 'csrf_token'})['value']

# create a dictionary to store the login data
data = {
    'csrf_token': csrf_token,
    'username': 'your-username',
    'password': 'your-password',
    'submit': 'Login'
}

# send a POST request to the login page with the login data
login_url = url + 'login'
response = session.post(login_url, data=data)

# check if the login was successful
if 'Logout' in response.text:
    print('Login successful')
else:
    print('Login failed')

# try to access a restricted page on the website
restricted_url = url + 'restricted'
response = session.get(restricted_url)

# check if the access was successful
if 'You do not have permission' in response.text:
    print('Access denied')
else:
    print('Access granted')
