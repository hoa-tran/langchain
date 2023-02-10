import openai
import streamlit as st

st.title('🤖 Ask me anything')
placeholder_response_user_input = st.empty()
user_input = placeholder_response_user_input.text_input("**Enter your question here** 🤓", key = "user_input")
print("app_started")

streaming_response = []
completion_text = ''

placeholder_response = st.empty()

if user_input:
    placeholder_response.text("Waiting for response")
    print('getting response')

    response = openai.Completion.create(
        model = 'text-davinci-003',
        prompt = user_input,
        max_tokens = 500,
        temperature = 0,
        stream = True,
    )
 
    for r in response:
        r_text = r['choices'][0]['text']
        completion_text += r_text
        placeholder_response.markdown(completion_text)

    print("end")