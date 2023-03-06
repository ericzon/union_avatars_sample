import os
from dotenv import load_dotenv
import union_avatar_client as ua_client

load_dotenv()

dir_path = os.path.dirname(os.path.realpath(__file__))
face_path = os.path.join(dir_path, 'my_img.jpg')
print(f'face_path: {face_path}')

auth_response = ua_client.get_auth()
token = auth_response['access_token']

# BODY
bodies_response =ua_client.get_bodies(token)
best_bodies = filter(lambda item: 'V1_male_casual_production' in item['name'], bodies_response)
body_id = list(best_bodies)[0]['id']
print('body_id',body_id)

# HEAD
head = ua_client.generate_head(token, face_path)
print('head keys ->', head.keys())
head_id = head['id']
# head_id = 'fa73cc9e-5896-4016-83aa-5ec5bf4176ad'
print('head_id', head_id)

# AVATAR

avatar = ua_client.create_avatar(token, 'Eric_01', body_id, head_id)
print(f'Avatar: {avatar}')
