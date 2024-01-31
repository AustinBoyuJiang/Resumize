import requests

def get_linkedin_profile(access_token, profile_url):
    # LinkedIn API endpoint for profile details
    api_url = "https://api.linkedin.com/v2/me"

    # Headers with the authorization token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # Make the request
    response = requests.get(api_url, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Example usage
access_token = 'your_access_token_here'  # You need to obtain this via OAuth
profile_info = get_linkedin_profile(access_token, "https://www.linkedin.com/in/austin-boyu-jiang/")
if profile_info:
    print(profile_info)
else:
    print("Failed to retrieve profile information.")
