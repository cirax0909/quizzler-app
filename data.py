import requests
AMOUNT = 10
TYPE = 'boolean'
parameters = {
    "amount": AMOUNT,
    "type": TYPE,
}
request = requests.get(url="https://opentdb.com/api.php", params=parameters)
response = request.json()
question_data = response['results']

