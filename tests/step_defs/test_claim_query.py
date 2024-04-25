import pytest
import requests
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver

scenarios('../features/')

@given('User get access token')
def get_access_token():
    driver = webdriver.Chrome()
    driver.get('http://www.google.com')
# test edit
@pytest.fixture()
@when('User send request claim query')
def send_claim_query():
    query = """
        {
          countries {
            code
            name
          }
        }
    """

    response = requests.post("http://countries.trevorblades.com/", json={'query': query})
    print(response.text)
    return response

@then('Response should be 200 Success')
def assert_response(send_claim_query):
    assert send_claim_query.status_code == 200