import requests
from modelAuth import Auth


def auth_token():
    def getAuth():
        url = "https://esignhub.docsol.id:8443/adimobile/billing/oauth/token"
        form_data = {
            "client_id": "frontend",
            "grant_type": "password",
            "username": "ADMCLIENT@CFI",
            "password": "AdIns2022",
        }

        response = requests.post(url, data=form_data)

        if response.status_code == 200:
            data = response.json()
            authModel = Auth(
                data["access_token"],
                data["token_type"],
                data["refresh_token"],
                data["expires_in"],
                data["scope"],
            )
            return authModel.access_token
        else:
            print("Error:", response.status_code)

    return getAuth()
