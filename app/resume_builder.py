import requests
import json

PROXYCURL_API_KEY = 'f3daHtdmPZjwqNoh6zmRCw'


def get_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file = json.load(file)
    return file


def get_user_profile(url):
    headers = {'Authorization': 'Bearer ' + PROXYCURL_API_KEY}
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    params = {
        'linkedin_profile_url': url,
    }
    response = requests.get(api_endpoint, params=params, headers=headers)
    return response.json()

def process_user_profile(profile):
    # Define the keys you want to keep
    keys_to_keep = ["full_name", "city", "summary", "education", "experiences", "skills"]

    email = profile.get("personal_emails")[0] if profile.get("personal_emails") else ""
    number = profile.get("personal_numbers")[0] if profile.get("personal_numbers") else ""
    province = profile.get("state")
    country = profile.get("country_full_name")
    projects = profile.get("accomplishment_projects")
    honors_and_awards = profile.get("accomplishment_honors_awards")
    publications = profile.get("accomplishment_publications")

    info = {key: profile[key] for key in keys_to_keep if key in profile}

    info["email"] = email
    info["number"] = number
    info["province"] = province
    info["country"] = country
    info["projects"] = projects
    info["honors_and_awards"] = honors_and_awards
    info["publications"] = publications

    for edu in info["education"]:
        if edu["description"] == "None":
            edu["description"] = ""
        edu["supplements"] = ""
        if edu["field_of_study"] != "None":
            edu["supplements"] = f"field of study: {edu.get('field_of_study')}"
        if edu["activities_and_societies"] != "None":
            if edu["supplements"] != "":
                edu["supplements"] += "\n"
            edu["supplements"] += f"activities and societies: {edu.get('activities_and_societies')}"
        del edu["field_of_study"]
        del edu["activities_and_societies"]
        del edu["school_linkedin_profile_url"]
        del edu["logo_url"]
        del edu["grade"]

    for exp in info["experiences"]:
        if exp["description"] == "None":
            exp["description"] = ""
        del exp["company_linkedin_profile_url"]
        del exp["logo_url"]
    return info

def get_user_info(url):
    profile = get_user_profile(url)
    info = process_user_profile(profile)
    return info


def get_job_profile(url):
    headers = {'Authorization': 'Bearer ' + PROXYCURL_API_KEY}
    api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/job'
    params = {
        'url': url,
    }
    response = requests.get(api_endpoint, params=params, headers=headers)
    return response.json()


def process_job_profile(profile):
    info = {}
    info["description"] = profile["job_description"]
    info["industry"] = profile["industry"]
    info["company_name"] = profile["company"]["name"]
    info["title"] = profile["title"]
    return info


def get_job_info(url):
    profile = get_job_profile(url)
    info = process_job_profile(profile)
    return info


user = "https://www.linkedin.com/in/emrulhasanemon/"
jobs = [
    "https://www.linkedin.com/jobs/view/3838243574",
    "https://www.linkedin.com/jobs/view/3819419885",
    "https://www.linkedin.com/jobs/view/3816078721",
]


if __name__ == '__main__':
    # profile = get_file("user_profile_Austin.json")
    # info = process_user_profile(profile)
    # print(info)
    profile = get_file("job_info.json")
    info = process_job_profile(profile)
    print(info)
