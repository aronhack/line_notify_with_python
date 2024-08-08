
import requests


def get_token(redirect_uri, client_id, secret, code):
    url = 'https://notify-bot.line.me/oauth/token'
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': secret
    }
    r = requests.post(url, params=payload)
    return r.text


def send_line_notification(message, access_token):
    url = 'https://notify-api.line.me/api/notify'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    payload = {'message': message}

    response = requests.post(url, headers=headers, params=payload)
    return response
