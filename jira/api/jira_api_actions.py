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
        result = json.dumps(JsonJiraIssue.create_issue(issue, summary, assignee, priority))
        return result

    @staticmethod
    def get_search_payload(max_results, summary):
        return json.dumps(JsonJiraIssue.search_issue(max_results, summary))

    @staticmethod
    def create_issue_by_api(issue, endpoint, summary, assignee, priority, headers):
        result = ApiInteractions.run_http_request("POST", endpoint,
                                                  ApiInteractions.get_payload(issue,
                                                                              summary,
                                                                              assignee,
                                                                              priority),
                                                  headers)

        return result

    @staticmethod
    def search_issue_by_api(endpoint, summary, max_results, headers):
        result = ApiInteractions.run_http_request("POST", endpoint,
                                                  ApiInteractions.get_search_payload(max_results,
                                                                                     summary),
                                                  headers)

        return result

    @staticmethod
    def create_and_update_issue_by_api(issue, create_endpoint, summary, assignee, priority,
                                       new_summary, new_assignee, new_priority, headers):
        issue_url = ApiInteractions.create_issue_by_api(issue, create_endpoint, summary, assignee, priority,
                                                        headers).json().get('self')
        result = ApiInteractions.run_http_request("PUT", issue_url,
                                                  ApiInteractions.get_payload(issue,
                                                                              new_summary,
                                                                              new_assignee,
                                                                              new_priority),
                                                  headers)

        return result
