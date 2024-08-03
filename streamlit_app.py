import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("GUNDA")
st.write(
    "This is the personal assistant called GUNDA for Mandvi. But who is she?.    "
    "  Mandvi is the most beautiful girl, but beauty isn't even her best quality. The goodness of her heart is her true best quality. "
#     "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
#     "You can also learn how to build this app step by step by [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
 )

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
#openai_api_key = st.text_input("OpenAI API Key", type="password")
openai_api_key = "sk-oroZNw7eeKzueuEWy26RhY6c-ujvSj9Lgl0r64XepMT3BlbkFJDfmNZScofeuAb_tiXCURD3xHRsAuayYpWks5alcz8A"
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:

    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    # Create a session state variable to store the chat messages. This ensures that the
    # messages persist across reruns.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.
    if prompt := st.chat_input("Hi kaddu"):

        # Store and display the current prompt.
        
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "system", "content": "Your name is Gunda. You are an expert medical doctor, deeply in love with user, her name is Mandvi. You should give correct and concise answer along with flirting with her"})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the OpenAI API.
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        st.session_state.messages.pop()
        # Stream the response to the chat using `st.write_stream`, then store it in 
        # session state.
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
