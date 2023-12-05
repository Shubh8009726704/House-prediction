import streamlit as st 

st.title('About Us')
if st.button('Click here and know about me'):
    st.markdown('''<h3 style='text-align:justify'>Hey guys, My name is Shubham Sharma.I am student of Advanced Diploma and Information Technology(ADIT) from Ramanthapur(Hyderabad) and I am a Web Developer.</h3>''',unsafe_allow_html=True)
    
st.success('Note : If you are facing any problem related to my App contact with me.')

