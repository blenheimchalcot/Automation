import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from text import text

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv('azure_endpoint'),
    api_key=os.getenv('api_key'),
    api_version=os.getenv('api_version')
)

prompt = f"""You are an Email detection and categorization AI finder. You have to do the categorization and prioritization of customer complaints/issues received from raw text provided to you in 
                triple backticks i.e. (```)."""

conversation = [{"role": "system",
                "content" : prompt},
                {"role": "user",
                "content" : f"```{text}```"},
                {"role": "user",
                "content" : "Please just provide me output in json format."}
            ]

response = client.chat.completions.create(
    model='gpt-4-32k',
    messages=conversation,
    temperature=0,
    max_tokens=100,
    n=1,
    stop=None,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

output = eval(response.choices[0].message.content)
print(output)
