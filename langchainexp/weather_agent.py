# weather_agent.py
# Import things that are needed generically

from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain import LLMChain
from langchain.prompts import PromptTemplate
import os
import sys
os.environ["OPENAI_API_KEY"]= "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"
os.environ["SERPAPI_API_KEY"] = "dac7e5f766e8cd88cc74d6050765add91aae32c7cd90175a3ef6d7fbed04ac78"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
os.environ["COHERE_API_KEY"] = "3vwcW4Gu0m5XWaT5bx4PBJ8IiQ5rT11rSsMijTBu"

# import custom tools
from weather_tool import Weather

llm = OpenAI(temperature=0)

prompt = PromptTemplate(
    input_variables=[],
    template="Answer the following questions as best you can."
)

# Load the tool configs that are needed.
llm_weather_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True
)

tools = [
    Weather
]

# Construct the react agent type.
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

agent.run("What about the weather today in Genova, Italy")