import llm
import logging
from langchain import PromptTemplate, FewShotPromptTemplate

#region - Base Logging -
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
#endregion - Base Logging -

examples = [
    {"word": "happy", "antonym": "sad"},
    {"word": "tall", "antonym": "short"},
    {"word": "blue", "antonym": "red"},
    {"word": "fast", "antonym": "slow"},
    {"word": "big", "antonym": "small"},
    {"word": "green", "antonym": "yellow"},
    {"word": "strong", "antonym": "weak"},
    {"word": "soft", "antonym": "hard"},
]

example_template = """
Word: {word}
Antonym: {antonym}\n
"""

example_prompt = PromptTemplate(
    input_variables=["word", "antonym"],
    template=example_template,
)

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Give the antonym of every input",
    suffix="Word: {input}\nAntonym:",
    input_variables=["input"],
    example_separator="\n",
)

completion_user = few_shot_prompt.format(input="dark")
logging.log(logging.INFO, completion_user)
llm.open_ai_llm_completion_handler(completion_user)