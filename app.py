# Bring in deps
from langchain.llms import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper
from flask import Flask


app = Flask(__name__)

openai_api_key = os.getenv('OPENAI_API_KEY')

# App Framework
st.title('Youtube GPT Creator')
prompt = st.text_input('Plug in your promp here')

# Prompt Templates
title_template = PromptTemplate(
    input_variables = ['topic'],
    template = 'Write me a youtube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'],
    template = 'Write me a youtube script base on this title TITLE: {title} while leveraging this wikipedia reserch: {wikipedia_research}'
)

# Memory
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')

# llms
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key="title", memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)

wiki = WikipediaAPIWrapper()

# Show messages to the screen
if prompt:
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt)
    script = script_chain.run(title=title, wikipedia_research=wiki_research)

    st.write(title)    
    st.write(script)

    with st.expander('Title History'):
        st.info(title_memory.buffer)

    with st.expander('Script History'):
        st.info(script_memory.buffer)

    with st.expander('Wikipedia History'):
        st.info(wiki_research)
