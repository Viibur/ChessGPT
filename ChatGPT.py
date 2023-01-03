import requests
import variables

def chatGPTRequest(userInput):
    requestBody = {
        "model": "text-davinci-003",
        "prompt": f"{userInput}",
        "max_tokens": 128,
        "temperature": 0.7,
    }
    answer = requests.post(variables.chatGPTPostUrl, headers={"Authorization": "Bearer " + variables.API_KEY},
                           json=requestBody)
    return answer.json()['choices'][0]['text']
