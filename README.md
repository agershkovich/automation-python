# automation-python
This repo was created for learning purposes

# run tests
pytest -v jira/tests/jira_pages_test.py 

#run allure tests
pytest --alluredir=./jira/tests-reports ./jira/tests
allure serve ./jira/tests-reports

