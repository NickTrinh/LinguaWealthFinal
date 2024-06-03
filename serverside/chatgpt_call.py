import os
from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
GPT_KEY = os.getenv("GPT_KEY")

def Analysis():
    txt = Path(os.getcwd() + r'\serverside\full_script_file.txt').read_text()


    client = OpenAI(
        api_key = GPT_KEY,
    )

    completion = client.chat.completions.create(
        model = "gpt-4-turbo",
        messages=[{"role": "user", "content": txt + "\n Here is a conversation between a wealth manager and a client. From this\
            script, pull out these 3 information: Client Income, Client Financial Goals, Client Risk Appetite and give it to me\
            on 3 different lines. The information should be in the format of <information_name>: <information_gathered>. Also,\
            make recommendations on potential assets class that is tailored to these criteria. Give it to me in one single line\
            with the format Recommended assets: <asset_class>, <asset_class>,..."}],
    )

    with open(os.getcwd() + r'\serverside\analysis.txt', 'w') as file:
        file.write(completion.choices[0].message.content)
