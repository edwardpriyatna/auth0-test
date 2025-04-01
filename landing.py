import streamlit as st

st.title("📔 Stroke Prediction Model Using Time Series Data")

if not st.experimental_user.is_logged_in:
    if st.button("✨ Sign up / Log in via Auth0", type="primary", use_container_width=True):
        st.login("auth0")  # Triggers Auth0 authentication

else:
    st.success("✅ Successfully logged in!")
    st.header(f"Hello, {st.experimental_user.name} 👋")
    if st.experimental_user.picture:
        st.image(st.experimental_user.picture, width=100)
    
    # Debugging: View user data
    st.json(st.experimental_user)

    # Logout button
    if st.button("Log Out"):
        st.logout()

