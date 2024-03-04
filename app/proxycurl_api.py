import requests

API_KEY = 'f3daHtdmPZjwqNoh6zmRCw'

def user_profile(url):
    headers = {'Authorization': 'Bearer ' + API_KEY}
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    params = {
        'linkedin_profile_url': url,
    }
    response = requests.get(api_endpoint, params=params, headers=headers)
    return response.json()

def job_profile(url):
    headers = {'Authorization': 'Bearer ' + API_KEY}
    api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/job'
    params = {
        'url': url,
    }
    response = requests.get(api_endpoint, params=params, headers=headers)
    return response.json()
