GITHUB_API = 'https://api.github.com'


import requests
import getpass
import json
from urllib.parse import urljoin


def main():
    #
    # User Input
    #
    username = input('Github username: ')
    password = getpass.getpass('Github password: ')
    note = input('Note (optional): ')
    #
    # Compose Request
    #
    url = urljoin(GITHUB_API, 'authorizations')
    payload = {}
    if note:
        payload['note'] = note
    res = requests.post(
        url,
        auth = (username, password),
        data = json.dumps(payload),
        )
    #
    # Parse Response
    #
    j = json.loads(res.text)
    token = j['token']
    print('Token', token)

if __name__ == '__main__':
    main()