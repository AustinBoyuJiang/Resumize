import openai

# Set your API key here
openai.api_key = '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'

def generate_chat_response(prompt, model="gpt-3.5-turbo", max_tokens=10):
    """
    Generate a response using OpenAI GPT chat model.

    :param prompt: The prompt to send to GPT.
    :param model: The chat model to use, default is "gpt-3.5-turbo".
    :param max_tokens: The maximum length of the response.
    :return: The generated text.
    """
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content'].strip()

# Example usage
prompt = "Translate the following English text to French: 'Hello, how are you?'"
generated_text = generate_chat_response(prompt)
print(generated_text)
