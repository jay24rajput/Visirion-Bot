GITHUB_API = 'https://api.github.com'


import requests
import getpass
import json
from urllib.parse import urljoin


def main():
    #
    # User Input
    #
    username = input('Username: ')
    password = getpass.getpass('Password: ')
    #
    # Compose Request
    #
    url = urljoin(GITHUB_API, 'authorizations')
    payload = {}
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
    print('Your new token is',token)

if __name__ == '__main__':
    main()
