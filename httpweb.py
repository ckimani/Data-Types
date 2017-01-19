import requests
while True:
	command = input('command? ').strip() 
	#input command
	if command == 'Get':
		response = requests.get('http://www.hangout.co.ke/')
		if response.status_code != 200:
    			raise ApiError('GET/concerts/ {}'.format(response.status_code))
		for concert in response.json():
    			print('{} {}'.format(concert['name'], concert['summary']))
	elif command =='POST':

		concert = {"name": "", "description": "" }

		response = requests.post('http://www.hangout.co.ke/', json=place)
		if response.status_code != 201:
    			raise ApiError('POST /concerts/ {}'.format(response.status_code))
		print('Created concert.name: {}'.format(response.json()["id"]))
