import streamlit as st
from PIL import Image
import io
import os
from chat import process_img, generate_response, init_prompt

st.title(" 😶‍🌫️ Skin Disease AI")

if "uploaded_image" not in st.session_state:
    st.session_state.uploaded_image = None

file_uploader_placeholder = st.empty()
camera_input_placeholder = st.empty()

if st.session_state.uploaded_image is None:
    uploaded_file = file_uploader_placeholder.file_uploader("🖼️ Upload an image", type=["jpg", "png"])
    picture = camera_input_placeholder.camera_input("📸Or take a picture")

    if uploaded_file is not None:
        picture = uploaded_file
        

    if picture:
        image = Image.open(picture)
        st.session_state.uploaded_image = image
        image.save('image.jpg')

        file_uploader_placeholder.empty()
        camera_input_placeholder.empty()

if st.session_state.uploaded_image is not None:
    st.image(st.session_state.uploaded_image, caption='Uploaded Image', use_column_width=True)
    disease = process_img()

    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": init_prompt(disease)}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    def clear_chat_history():
        st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

    if prompt := st.chat_input(placeholder="Type a message"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(prompt)
                placeholder = st.empty()
                full_response = ''
                for text in response:
                    full_response += text
                    placeholder.markdown(full_response)
                placeholder.markdown(full_response)
        message = {"role": "assistant", "content": full_response}
        st.session_state.messages.append(message)