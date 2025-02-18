from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
import os

def generate_title(topic):
    llm = OpenAI(temperature=0.9)
    template = PromptTemplate(
        input_variables=['topic'],
        template='Write me a youtube video title about {topic}'
    )
    chain = template | llm
    return chain.invoke({"topic": topic})

def generate_script(title, research):
    llm = OpenAI(temperature=0.9)
    template = PromptTemplate(
        input_variables=['title', 'wikipedia_research'],
        template='Write me a youtube script based on this title TITLE: {title} while leveraging this wikipedia research: {wikipedia_research}'
    )
    chain = template | llm
    return chain.invoke({"title": title, "wikipedia_research": research}) 