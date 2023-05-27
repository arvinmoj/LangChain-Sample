import os 
import logging
from load_dotenv import load_dotenv
from langchain import PromptTemplate

#region - Base Logging -
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
#endregion - Base Logging -


load_dotenv()
OPEN_AI_TOKEN = os.environ.get("OPEN_AI_TOKEN")
os.environ["OPENAI_API_KEY"] = OPEN_AI_TOKEN


template = "What is a good name for a company that makes {product}?"

prompt = PromptTemplate(
    input_variables=["product"],
    template=template,
)

user_input = input("Enter a product: ")

completion_user = prompt.format(product=user_input)
logging.log(logging.INFO, completion_user)