from chatbot import generate_response
import streamlit as st
from streamlit_chat import message
import openai
import config


# Assign API key (REPLACE WITH YOUR OPENAI API KEY)
openai.api_key = config.openai_key


def generate_response(prompt, max_token=50, outputs=3): 
    """Generates a response to the given user prompt"""

    # generate response with openai library 
    response = openai.Completion.create( 
        model="text-davinci-003", 
        prompt=prompt, 
        max_tokens=max_token, 
        n=outputs 
    ) 

    # extract text from the dictionary
    response_text = response['choices'][0]['text'].strip('\n')

    return response_text

# Create the title and
st.set_page_config(page_title="Rhyming Chatbot")

# create the header and the line underneath it
header_html = "<h1 style='text-align: center; margin-bottom: 1px;'>🤖 The Rhyming Chatbot 🤖</h1>"
line_html = "<hr style='border: 2px solid green; margin-top: 1px; margin-bottom: 0px;'>"
st.markdown(header_html, unsafe_allow_html=True)
st.markdown(line_html, unsafe_allow_html=True)

# create lists to store user queries and generated responses
if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []


# create input field for user queries
user_input = st.chat_input("How can I help?")

# generate response when a user prompt is submitted
if user_input:
    output = generate_response(prompt=user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)


# show queries and responses in the user interface
if st.session_state["generated"]:

    for i in range(len(st.session_state["generated"])):
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
        message(st.session_state["generated"][i], key=str(i))