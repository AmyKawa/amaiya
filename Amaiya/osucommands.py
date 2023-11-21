import requests

#client_id = (assume defined)
#client_secret = (assume defined)

def get_access_token(client_id, client_secret):
	data = {
		'client_id': client_id,
		'client_secret': client_secret,
		'grant_type': 'client_credentials',
		'scope': 'public'
	}
	
	response = requests.post('https://osu.ppy.sh/oauth/token', data=data)
	
	if response.status_code == 200:
		return response.json().get('access_token')
	else:
		raise Exception(f"Could not get access token, status code: {response.status_code}")

global token 
token = get_access_token(client_id, client_secret)

def get_user_data(access_token, username):
	headers = {'Authorization': f'Bearer {access_token}'}
	response = requests.get(f'https://osu.ppy.sh/api/v2/users/{username}/osu', headers=headers)
	if response.status_code == 200:
		user_data = response.json()
		return user_data
	else:
		raise Exception("Failed to get user data")

def user_exists(access_token, username):
	headers = {'Authorization': f'Bearer {access_token}'}
	response = requests.get(f'https://osu.ppy.sh/api/v2/users/{username}/osu', headers=headers)
	if response.status_code == 200:
		user_data = response.json()
		return True
	else:
		return False
		
#--------------------------------------------

def get_user_id(access_token, username):
	headers = {'Authorization': f'Bearer {access_token}'}
	response = requests.get(f'https://osu.ppy.sh/api/v2/users/{username}/osu', headers=headers)
	if response.status_code == 200:
		user_data = response.json()
		return user_data['id']
	else:
		raise Exception("Failed to get user data")
		
def get_user_pfp(access_token, username):
	headers = {'Authorization': f'Bearer {access_token}'}
	response = requests.get(f'https://osu.ppy.sh/api/v2/users/{username}/osu', headers=headers)
	if response.status_code == 200:
		data = response.json()
		return data['avatar_url']
	else:
		raise Exception("Failed to get player data")

def get_user_banner(access_token, username):
	headers = {'Authorization': f'Bearer {access_token}'}
	response = requests.get(f'https://osu.ppy.sh/api/v2/users/{username}/osu', headers=headers)
	if response.status_code == 200:
		data = response.json()
		return data['cover_url']
	else:
		raise Exception("Failed to get player data")

def get_user_kudosu(access_token, username):
	headers = {'Authorization': f'Bearer {access_token}'}
	response = requests.get(f'https://osu.ppy.sh/api/v2/users/{username}/osu', headers=headers)
	if response.status_code == 200:
		data = response.json()
		return data['kudosu']
	else:
		raise Exception("Failed to get player data")

