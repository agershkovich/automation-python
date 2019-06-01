import json

import requests

from jira.api.json_fixtures import JsonJiraIssue


class ApiInteractions:
    @staticmethod
    def login_by_api(url, username, password):
        return requests.get(url, auth=(username, password))

    @staticmethod
    def run_http_request(method, url, payload, headers):
        result = requests.request(method, url, data=payload, headers=headers)
        return result

    @staticmethod
    def get_payload(issue, summary, assignee, priority):
        return json.dumps(JsonJiraIssue.create_issue(issue, summary, assignee, priority))

    @staticmethod
    def get_search_payload(max_results, summary):
        return json.dumps(JsonJiraIssue.search_issue(max_results, summary))
