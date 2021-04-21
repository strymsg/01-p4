# POC for api requests
# most tests extracted from https://realpython.com/python-requests/

import requests
from requests.exceptions import HTTPError

def do_request(arg):
    # Use a breakpoint in the code line below to debug your script.
    pass

if __name__ == '__main__':
    print("BASIC HTTP  GET REQUEST...")
    for url in ['https://api.github.com', 'https://api.github.com/invalid']:
        try:
            response = requests.get(url)
            # If the response was successful, no Exception will be raised
            print(">> raise_for_status()")
            response.raise_for_status()
            print('>> Response content:')
            print(response.content)
            print('>> response to string')
            response.encoding = 'utf-8'
            print(response.text)
            print('>> response.json()')
            print(response.json())
            print('>> response.headers')
            print(type(response.headers))
            print(response.headers)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            print('Success!')

        print("Headers and params requests")
        try:
            response = requests.get(
                'https://api.github.com/search/repositories',
                params={'q': 'requests+language:python'},
                headers={'Accept': 'application/vnd.github.v3.text-match+json'},
            )
            print('>> response.json()')
            print(type(response.json()))
        except HTTPError as http_err:
            print(f'HTTP Error ocurred: {http_err}')

        print('HTTP Methods with body')
        try:
            print('POST')
            response = requests.post('https://httpbin.org/post', data={'key': 'value'})
            print(response.json())
            print('POST using json')
            # automatically serializes
            response = requests.post('https://httpbin.org/post', json={'key': 'value'})
            json_response = response.json()
            print('>> response.json()')
            print(json_response)
            print('>> json_response["data"]')
            print(json_response['data'])
            print('PUT')
            response = requests.put('https://httpbin.org/put', data={'key': 'value'})
            print(response.json())
        except HTTPError as http_err:
            print(f'HTTP Error ocurred: {http_err}')

        print("HMore Http pethods")
        try:
            requests.delete('https://httpbin.org/delete')
            requests.head('htt  ps://httpbin.org/get')
            requests.patch('https://httpbin.org/patch', data={'key': 'value'})
            requests.options('https://httpbin.org/get')
        except HTTPError as http_err:
            print(f"HTTP Error ocurred: {http_err}")

        # TODO: Authentication
