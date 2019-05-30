import requests


class ApiInteractions:
    @staticmethod
    def login(url, username, password):
        result = requests.get(url, auth=(username, password))
        print(result.status_code)
        print(result.headers.get("X-Seraph-LoginReason"))
        return result.status_code
