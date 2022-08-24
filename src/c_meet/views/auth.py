from flask import request, redirect, url_for
from flask import Blueprint
from oauthlib.oauth2 import WebApplicationClient
import os
import requests
import json
from flask_login import (login_user, logout_user)

from c_meet.models.users import User

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
GOOGLE_USERINFO_URL = "https://openidconnect.googleapis.com/v1/userinfo"

client = WebApplicationClient(GOOGLE_CLIENT_ID)

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    request_uri = client.prepare_request_uri(
        GOOGLE_AUTH_URL,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@auth.route("/login/callback")
def login_callback():
    code = request.args.get("code")

    token_url, headers, body = client.prepare_token_request(
        GOOGLE_TOKEN_URL,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code,
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    client.parse_request_body_response(json.dumps(token_response.json()))

    uri, headers, body = client.add_token(GOOGLE_USERINFO_URL)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    if userinfo_response.json().get("email_verified"):
        google_id = userinfo_response.json()["sub"]
        icon = userinfo_response.json()["picture"]
    else:
        return

    user = User(google_id=google_id, name="Guest", icon=icon)
    if not User.search_google_id(google_id):
        User.create(user)

    user = User.search_google_id(google_id)
    login_user(user)

    return redirect(url_for("user.me"))


@auth.route('/logout')
def logout():
    logout_user()
    return "ログアウトしました"
