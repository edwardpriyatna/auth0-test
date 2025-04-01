import streamlit as st
st.title('Authentication')

if not st.experimental_user.is_logged_in:
    if st.button('Authenticate'):
        st.login('google')

st.json(st.experimental_user)
st.header(f"hello {st.experimental_user.name}")
st.image(st.experimental_user.picture)