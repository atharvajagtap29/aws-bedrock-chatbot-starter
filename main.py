import streamlit as st
from Controller.bedrock_controller import invoke_bedrock_model
from Controller.session_controller import generate_session

# Initialize SessionId in session state if not already done
if 'SessionId' not in st.session_state:
    st.session_state.SessionId = generate_session()

# Initialize History in session state if not already done
if 'history' not in st.session_state:
    st.session_state.history = []

st.title("Bedrock Integration with Python Script")
st.write("BETA VERSION")

# Input Prompt
user_input = st.text_input("Enter your prompt:")

# Button to send the prompt
if st.button("Send"):
    if user_input:
        with st.spinner('Thinking...'):
            output = invoke_bedrock_model(user_input)
            
        # Add prompt and response to history
        st.session_state.history.insert(0, {
            "prompt": user_input,
            "response": output
        })
        
        st.write(f"Model output: {output}")
    else:
        st.write("Please enter a prompt.")

# Display history
st.sidebar.subheader("INTERACTION HISTORY")

# print history on console for reference
print(f'HERE IS THE SESSION HISTORY ARRAY {st.session_state.history}')

for entry in st.session_state.history:
    st.sidebar.write(f"**Prompt:** {entry['prompt']}")
    st.sidebar.write(f"**Response:** {entry['response']}")
    st.sidebar.write("---")
