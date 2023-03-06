import os
import requests
import base64

def get_auth():
	url = 'https://api.unionavatars.com/login'
	headers = {
	  'Content-Type': 'application/x-www-form-urlencoded'
	}
	data = {
	    'username': os.getenv('USERNAME'),
	    'password': os.getenv('PASSWORD')
	}

	response = requests.post(url, headers=headers, data=data )
	return response.json()

def get_bodies(token):
	url = 'https://api.unionavatars.com/bodies'
	headers = {
	  'Authorization': f'Bearer {token}',
	  'Content-Type': 'application/json'
	}

	response = requests.get(url, headers=headers)
	return response.json()

def generate_head(token, file_path, name = 'Default_head'):
	url = 'https://api.unionavatars.com/heads'
	headers = {
		'Authorization': f'Bearer {token}',
		'Content-Type': 'application/json'
	}

	data = {
      'name': name,
		'selfie_img': encode_file(file_path)
	}

	response = requests.post(url, headers=headers, data=data)
	print('head status code: ',response.status_code)
	return response.json()

def encode_file(file_path):
	encoded_string = ''
	with open(file_path, 'rb') as img:
		encoded_string = base64.b64encode(img.read()).decode('utf-8')
	return encoded_string

def create_avatar(token, name, body_id, head_id, format = 'glb'):
	url = 'https://api.unionavatars.com/avatars'
	headers = {
      'Authorization': f'Bearer {token}',
      'Content-Type': 'application/json'
	}

	data = {
      'name': name,
      'body_id': body_id,
      'head_id': head_id,
      'create_thumbnail': True,
      'output_format': format
  	}

	response = requests.post(url, headers=headers, data=data)
	return response.json()
