import os
import logging
import langchain
from dotenv import load_dotenv
from langchain.llms import OpenAI

#region - Base Logging -
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
#endregion - Base Logging -

#region - Load Environment Variables -
load_dotenv()
OPEN_AI_TOKEN = os.environ.get("OPEN_AI_TOKEN")
#endregion - Load Environment Variables -

logging.log(logging.INFO, "Starting Langchain")

llm_open_ai = OpenAI(model="text-davinci-003", openai_api_key=OPEN_AI_TOKEN)

def open_ai_llm_completion_handler(prompt):
    completion_open_ai = llm_open_ai(prompt)
    logging.log(logging.INFO, completion_open_ai)
    return completion_open_ai