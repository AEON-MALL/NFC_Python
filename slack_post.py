import requests

def slack_post(student_number):
    TOKEN = 'xoxb-3987434582260-4008777263888-CYYAJfPKHpoG1uCkJ68uW5Q8'
    CHANNEL = 'test'

    url = "https://slack.com/api/chat.postMessage"
    headers = {"Authorization": "Bearer "+TOKEN}
    data = {
        'channel': CHANNEL,
        'text': student_number
    }
    requests.post(url,headers=headers,data=data)