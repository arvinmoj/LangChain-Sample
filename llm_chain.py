import llm
import logging
from  dotenv import load_dotenv
import os
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

#region - Base Logging -
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
#endregion - Base Logging -

#region - Load Environment Variables -
load_dotenv()
OPEN_AI_TOKEN = os.environ.get("OPEN_AI_TOKEN")
#endregion - Load Environment Variables -

llm_open_ai = OpenAI(model="text-davinci-003", openai_api_key=OPEN_AI_TOKEN)

template = "What is a good name for a company that makes {product}?"

prompt = PromptTemplate(
    input_variables=["product"],
    template=template,
)

chain = LLMChain(llm = llm_open_ai , 
                  prompt = prompt)

completion_user= chain.run("computer")
logging.log(logging.INFO, completion_user)