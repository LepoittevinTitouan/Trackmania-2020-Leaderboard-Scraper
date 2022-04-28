import settings
import requests
from requests.auth import HTTPBasicAuth


def GetAuthentication():
    url = "https://public-ubiservices.ubi.com/v3/profiles/sessions"
    headers = {
        'Host': 'public-ubiservices.ubi.com',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Content-Length': '0',
        'Ubi-AppId': '86263886-327a-4328-ac69-527f0d20a237',
        'user-agent': 'zrtLeaderboardScrapper'
    }
    result = requests.post(url, headers=headers, auth=HTTPBasicAuth(settings.login, settings.password))

    result = result.json()

    settings.pseudo = result['nameOnPlatform']

    token = result['ticket']

    url = "https://prod.trackmania.core.nadeo.online/v2/authentication/token/ubiservices"
    body = {
        'audience': 'NadeoLiveServices'
    }
    headers = {
        'Host': 'prod.trackmania.core.nadeo.online',
        'authorization': 'ubi_v1 t=' + token,  # Temp token
        'content-type': 'application/json',
        'user-agent': 'zrtLeaderboardScrapper'
    }

    result = requests.post(url, headers=headers, json=body)

    result = result.json()

    settings.accessToken = result["accessToken"]
    settings.refreshToken = result["refreshToken"]


def GetTokenRefresh():
    url = "https://prod.trackmania.core.nadeo.online/v2/authentication/token/refresh"
    body = {
        'audience': 'NadeoLiveServices'
    }
    headers = {
        'Host': 'prod.trackmania.core.nadeo.online',
        'Authorization': 'nadeo_v1 t=' + settings.refreshToken,
        'content-type': 'application/json',
        'user-agent': 'zrtLeaderboardScrapper'
    }
    result = requests.post(url, headers=headers, json=body)
    result = result.json()

    settings.accessToken = result["accessToken"]
    settings.refreshToken = result["refreshToken"]
