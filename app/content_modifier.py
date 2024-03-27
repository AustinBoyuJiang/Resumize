import os
import asyncio
import json
from openai import OpenAI


def get_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file = json.load(file)
    return file


client = OpenAI(
    api_key='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',
)


def gpt(messages):
    message = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.3,
        messages=messages,
    )
    return message.choices[0].message.content


sections_to_modify = ["education", "experiences", "projects", "honors_and_awards", "publications"]

user_info = get_file("processed_user_profile_Austin.json")
job_info = get_file("job_info.json")

instruction_messages = get_file("gpt_messages.json")
instruction_messages.insert(1, {"role": "system", "content": f"job_to_apply:{job_info}"})

messages = instruction_messages.copy()
messages.append({"role": "user", "content": f"personal statement to modify:{user_info['summary']}"})
user_info["summary"] = gpt(messages)

for section in sections_to_modify:
    for item in user_info[section]:
        messages = instruction_messages.copy()
        messages.append({"role": "user", "content": f"{section} description to modify:{item}"})
        item["description"] = gpt(messages)

print(user_info)
