import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
#import open_ai

@st.experimental_memo
def get_llm():
    return OpenAI(temperature=0.9)


def gen_text(txt_prompt: str) -> str:
    llm = get_llm() #openai_api_key=open_ai.api_key)
    prompt = PromptTemplate(
        input_variables=["event"],
        template="What is a good blog post title for the {event}?",
    )
    chain = LLMChain(llm=llm, prompt=prompt)

    second_prompt = PromptTemplate(
        input_variables=["title"],
        template="What is a good blog post that describe what is good to do regarding {title}?",
    )
    chain_two = LLMChain(llm=llm, prompt=second_prompt)

    overall_chain = SimpleSequentialChain(chains=[chain, chain_two], verbose=True)
    
    return overall_chain.run(txt_prompt)


def main():
    st.title('🤖 Article draft generator')
    form = st.form(key='my_form')
    subject_input = form.text_input(label="**What is the topic?** 🤓")
    submit_button = form.form_submit_button(label='**Submit**')
    if submit_button:
        draft = gen_text(subject_input)
        st.write(draft)


if __name__ == "__main__":
    main() 
