import requests
while True:
	command = raw_input('command? ').strip() 
	#input command
	if command == 'Get':
		response = requests.get('https://andela.com/')
		if response.status_code != 200:
			#negate HTTP error code
    			raise ApiError('GET/resources/ {}'.format(response.status_code))
		for concert in response.json():
    			print('{} {}'.format(resource['name'], resource['summary']))
	elif command =='POST':

		resources = {"name": "", "description": "" }

		response = requests.post('https://andela.com/', json=place)
		if response.status_code != 201:
			#negate request fulfilled
    			raise ApiError('POST /resources/ {}'.format(response.status_code))
		print('Created resource.name: {}'.format(response.json()["id"]))
