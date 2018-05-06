import nexmo
client = nexmo.Client(key = '6b9e072a', secret = 'zRGqpi8A2fCNBdzZ')
response = client.send_message({'from': '12015799675', 'to' : '18582818261', 'text':'How you feeling today ? sleep early sleep often'})
response = response['messages'][0]
if response['status'] == '0':
    print('Sent message', response['message-id'])
    print('Remaining balance is', response['remaining-balance'])
else:
    print('Error', response['error-text'])

