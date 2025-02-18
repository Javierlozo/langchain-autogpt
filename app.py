# Bring in deps
from langchain_openai import OpenAI
import streamlit as st
import os
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from langchain_community.utilities import WikipediaAPIWrapper

# OpenAI settings
openai_api_key = os.getenv('OPENAI_API_KEY')

# Modern LangChain setup
llm = OpenAI(temperature=0.9)

# App Framework
st.title('Youtube GPT Creator')
prompt = st.text_input('Plug in your prompt here')

# Initialize session state for memory if it doesn't exist
if 'title_history' not in st.session_state:
    st.session_state.title_history = []
if 'script_history' not in st.session_state:
    st.session_state.script_history = []

# Prompt Templates
title_template = PromptTemplate(
    input_variables = ['topic'],
    template = 'Write me a youtube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'],
    template = 'Write me a youtube script based on this title TITLE: {title} while leveraging this wikipedia research: {wikipedia_research}'
)

output_parser = StrOutputParser()

# Create chains using the new syntax
title_chain = title_template | llm | output_parser
script_chain = script_template | llm | output_parser

wiki = WikipediaAPIWrapper()

# Show messages to the screen
if prompt:
    # Generate title
    title = title_chain.invoke({"topic": prompt})
    st.session_state.title_history.append({
        "human": HumanMessage(content=prompt),
        "ai": AIMessage(content=title)
    })
    
    # Get Wikipedia research
    wiki_research = wiki.run(prompt)
    
    # Generate script
    script = script_chain.invoke({
        "title": title,
        "wikipedia_research": wiki_research
    })
    st.session_state.script_history.append({
        "human": HumanMessage(content=title),
        "ai": AIMessage(content=script)
    })

    st.write(title)    
    st.write(script)

    with st.expander('Title History'):
        for exchange in st.session_state.title_history:
            st.write("Topic:", exchange["human"].content)
            st.write("Title:", exchange["ai"].content)
            st.write("---")

    with st.expander('Script History'):
        for exchange in st.session_state.script_history:
            st.write("Title:", exchange["human"].content)
            st.write("Script:", exchange["ai"].content)
            st.write("---")

    with st.expander('Wikipedia Research'):
        st.info(wiki_research)
