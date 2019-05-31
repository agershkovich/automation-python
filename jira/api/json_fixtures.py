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
