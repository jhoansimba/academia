import requests
def getTime():
    response = requests.get('http://worldtimeapi.org/api/ip', params={})
    print('Response: ', response.json())
    return response.json()