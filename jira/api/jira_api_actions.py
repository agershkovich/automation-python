import json

import requests

from jira.api.json_fixtures import JsonJiraIssue


class ApiInteractions:
    @staticmethod
    def login_by_api(url, username, password):
        result = requests.get(url, auth=(username, password))
        print(result.request)
        # print(result.headers.get("X-Seraph-LoginReason"))
        return result.status_code

    @staticmethod
    def create_issue_by_api(url, payload, headers):
        result = requests.request("POST", url, data=payload, headers=headers)
        return result.status_code

    @staticmethod
    def get_payload(issue, summary, assignee, priority):
        payload = json.dumps(JsonJiraIssue.create_issue(issue, summary, assignee, priority))
        return payload
