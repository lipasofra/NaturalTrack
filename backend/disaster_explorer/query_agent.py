#%%
import pandas as pd
from langchain.agents import create_pandas_dataframe_agent, load_tools
from langchain import OpenAI
from dotenv import find_dotenv, load_dotenv
import os
import re
load_dotenv(find_dotenv())


def run_query(query, openai_key=None, csv_path='/Users/andres/Documents/programacion/codefest/Equipo-1/backend/disasters/1900.csv'):
    llm = OpenAI(
        openai_api_key=openai_key if openai_key is not None else os.getenv("OPENAI_API_KEY"),
        model_name="gpt-3.5-turbo",
    )
    tools = load_tools(
        ["llm-math", "open-meteo-api", "requests_all", "terminal", "python_repl"],
        llm=llm,
    )

    df = pd.read_csv(csv_path)

    agent = create_pandas_dataframe_agent(
        llm=llm,
        df=df,
        tools=tools,
        verbose=True,
    )

    prompt_template = """
    You are a helpful assistant that that can answer questions \
    in an a step by step way, making sure to have the right answer. \
    Let's work out the following problem: \
        
    {prompt}. 
    Now, as a researcher, you are tasked with investigating the provided response options, \
    list the flaws and faulty logic, as well as the correct statements of each answer option.\
    Let's work out step in a step by step way to be sure we have all the errors and correct statements. \
    Then, after discussing the reseached options, as a resolver, you are tasked with 1) finding which of \
    the answer the reseacher though of was best, 2) improving that answer, and 3) returning the improved answer in full. \
    Let's work this out in a step by step way to be sure we have the right answer. \
    At the end, return a user friendly answer as per the initial question following the result result of step 3. \
    """    

    try:
        response= agent.run(prompt_template.format(prompt=query))
        
    except Exception as e:
             response = str(e)
             if response.startswith("Could not parse LLM output: `"):
                  response = response.removeprefix("Could not parse LLM output: `").removesuffix("`")
    
    return response



def run_query_disaster_alone(query, disaster_dict, openai_key=None):
    llm = OpenAI(
        openai_api_key=openai_key if openai_key is not None else os.getenv("OPENAI_API_KEY"),
        model_name="gpt-3.5-turbo",
    )
    tools = load_tools(
        ["llm-math", "open-meteo-api", "requests_all", "terminal", "python_repl"],
        llm=llm,
    )

    df = object_to_dataframe(disaster_dict)

    agent = create_pandas_dataframe_agent(
        llm=llm,
        df=df,
        tools=tools,
        verbose=True,
    )

    prompt_template = """
    You are a helpful assistant that that can answer questions \
    in an a step by step way, making sure to have the right answer. \
    Let's work out the following problem: \
        
    {prompt}. 
    Now, as a researcher, you are tasked with investigating the provided response options, \
    list the flaws and faulty logic, as well as the correct statements of each answer option.\
    Let's work out step in a step by step way to be sure we have all the errors and correct statements. \
    Then, after discussing the reseached options, as a resolver, you are tasked with 1) finding which of \
    the answer the reseacher though of was best, 2) improving that answer, and 3) returning the improved answer in full. \
    Let's work this out in a step by step way to be sure we have the right answer. \
    At the end, return a user friendly answer as per the initial question following the result result of step 3. \
    """    

    try:
        response= agent.run(prompt_template.format(prompt=query))
        
    except Exception as e:
             response = str(e)
             if response.startswith("Could not parse LLM output: `"):
                  response = response.removeprefix("Could not parse LLM output: `").removesuffix("`")
    
    return response
# %%


def object_to_dataframe(obj):
    data = {
        field.name: getattr(obj, field.name)
        for field in obj._meta.fields
    }
    return pd.DataFrame([data])
