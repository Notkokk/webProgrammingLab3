import requests

class Client():
    header = None
    def __init__(self, host):
        self._session=requests.Session()
        self._host=host
        payload = {'key': 'value'}
        respond=requests.get(host, params=payload)
        print(respond.url)
        print(respond.headers)
        print(respond.request.headers)

    def set_header(self, header):
        self.header = header

    def get(self, path, query):
        return requests.get(self._host + path, headers=self.header, params=query)

    def post(self, path, query):
        return requests.post(self._host + path, headers=self.header, params=query)

    def __del__(self):
        self._session.close()

if __name__ == '__main__':
    client = Client("https://httpbin.org")
    client.set_header({"user-agent": "test_client"})
    response_1 = client.get(path="/get", query={"key_1": "value_1"})
    if response_1 is not None:
        print("ok")
    response = client.post(path="/status/400", query={"key_2": "value_2"})
    if response is not None:
        print("ok")