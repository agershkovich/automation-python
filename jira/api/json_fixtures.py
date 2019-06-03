class JsonJiraIssue:

    @staticmethod
    def create_issue(issue, summary, assignee, priority):
        json = {
            "fields": {
                "project":
                    {
                        "key": "WEBINAR"
                    },
                "summary": summary,
                "description": "Creating of an issue",
                "assignee": {"name": assignee},
                "priority": {"name": priority},
                "issuetype": {"name": issue}
            }

        }
        return json

    @staticmethod
    def search_issue(max_results, summary):
        json = {
            "jql": "project = WEBINAR and assignee = currentUser() and summary~" + summary,
            "startAt": 0,
            "maxResults": max_results
        }
        return json
