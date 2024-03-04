import os
import asyncio
import json
from openai import AsyncOpenAI

client = AsyncOpenAI(
    # This is the default and can be omitted
    api_key='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',
)

prompt = '''
Task:
1. Analyze the job description to identify key skills, qualifications, and experiences the employer is looking for.
2. Review the user's resume content to identify relevant skills, experiences, and achievements.
3. Suggest modifications to the resume:
   - Highlight or emphasize skills and experiences that directly match the job description.
   - Tailor the summary or objective statement to reflect the focus of the job.
   - Modify bullet points under work experience to demonstrate how past roles and achievements align with the job requirements.
   - Include relevant keywords from the job description to improve ATS (Applicant Tracking System) compatibility.

Output:
Provide a modified version of the user's resume that is tailored to the job description, incorporating the identified changes and improvements.

Focus on experience and project section of the resume. Note that if the description is None, design it yourself.
'''

def get_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file = json.load(file)
    return file


async def main() -> None:
    message = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"my resume is [{get_file('user_profile_Austin.json')}]"},
            {"role": "user", "content": f"job description is [{get_file('job_description.json')}]"},
        ],
    )
    print(message.choices[0].message.content)


asyncio.run(main())