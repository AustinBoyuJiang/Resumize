import requests

api_key = 'f3daHtdmPZjwqNoh6zmRCw'
headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
params = {
    'linkedin_profile_url': 'https://www.linkedin.com/in/epic-eric/',
    'use_cache': 'if-recent',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)

print(response.json())
