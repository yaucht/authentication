import re

from time import time
from os import environ

from asyncio import sleep
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, validator

import jwt

router = APIRouter()

CREDS_STORE = {
    ('boris', 'ImSoCool'),
    ('reviewer', 'BorisIsSoCool'),
}

USERNAME_PATTERN = re.compile(r'\w{2,255}')
PASSWORD_PATTERN = re.compile(r'[\w\-.@#$%^&*]{2,255}')


class Credentials(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_pattern(cls, username):
        if not USERNAME_PATTERN.fullmatch(username):
            raise ValueError('Username MUST comply the following pattern '
                             f'`{USERNAME_PATTERN}`')
        return username

    @validator('password')
    def password_pattern(cls, password):
        if not PASSWORD_PATTERN.fullmatch(password):
            raise ValueError('Password MUST comply the following pattern '
                             f'`{PASSWORD_PATTERN}`')
        return password


INVAL_CREDS = 'Given credentials are not recognized'


@router.post(
    '/authenticate',
    tags=['authenticate'],
    responses={status.HTTP_403_FORBIDDEN: {
        'description': INVAL_CREDS
    }})
async def authenticate(credentials: Credentials):
    # Simulating database delay for the UI features demo.
    await sleep(.5)
    if (credentials.username, credentials.password) in CREDS_STORE:
        iat = round(time())
        exp = iat + 60 * 60 * 24

        token = jwt.encode(
            {
                'iss': 'boris-auth',
                'sub': credentials.username,
                'iat': iat,
                'exp': exp,
            },
            environ['JWT_SECRET'],
            algorithm='HS256')

        return token
    else:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail=INVAL_CREDS)
