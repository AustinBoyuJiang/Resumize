import os
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    # This is the default and can be omitted
    api_key='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',
)


async def main() -> None:
    message = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-3.5-turbo",
    )
    print(message.choices[0].message.content or "", end="")


asyncio.run(main())