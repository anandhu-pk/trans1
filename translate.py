import streamlit as st
from googletrans import Translator as tran

st.header('Translator Model')
input=st.text_area("enter text",value="")
option=st.selectbox('To which language you wish to translate this text to?',("Malayalam","Hindi","Tamil"))

if st.button("Translate"):
    translator=tran()
    translation=translator.translate(input,dest=option)
    st.write(translation.text)
