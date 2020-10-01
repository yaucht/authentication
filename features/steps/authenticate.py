import requests

from behave import *


@given('recognizable credentials')
def step_impl(context):
    context.credentials = ('boris', 'ImSoCool')


@given('unrecognizable credentials')
def step_impl(context):
    context.credentials = ('valid', 'butUnrecognizable')


@given('we use {username} and {password}')
def step_impl(context, username, password):
    context.credentials = (username, password)


@when('we request a token')
def step_impl(context):
    context.response = requests.post('http://authentication/authenticate',
                                     json={
                                         'username': context.credentials[0],
                                         'password': context.credentials[1],
                                     })


@then('service will respond with {status:d} status code')
def step_impl(context, status):
    assert context.response.status_code == status


@then('we will get a JWT')
def step_impl(context):
    token = context.response.text
    assert len(token.split('.')) == 3
