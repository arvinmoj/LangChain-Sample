import llm
import logging
from langchain import PromptTemplate

#region - Base Logging -
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
#endregion - Base Logging -

template = "What is a good name for a company that makes {product}?"

prompt = PromptTemplate(
    input_variables=["product"],
    template=template,
)
completion_user = prompt.format(product="computer")
logging.log(logging.INFO, completion_user)

llm.open_ai_llm_completion_handler(completion_user)