import base64

import requests


class Fofa_Api():
    def get_data(self, keyword):
        keyword = base64.b64encode(keyword.encode())
        your_key = '23e24abc1866a533121c369b66b5280c'
        url = f'https://fofa.info/api/v1/search/all?&key={your_key}&qbase64={keyword}'
        res = requests.get(url).json()
        print(res['results'])
