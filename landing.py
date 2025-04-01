import streamlit as st

st.title("📔 Streamlit + Auth0 Production test")

st.markdown(
    "Stroke Prediction Model Using Time Series Data"
)

with st.container(border=True):
    st.image("./img/demo.gif")

st.write("\n")

if st.button(
    "✨ Sign up to our app",
    type="primary",
    key="checkout-button",
    use_container_width=True,
):
    # st.login("google")
    st.login("auth0")

with st.expander("📝 Privacy & Data Security Disclaimer"):
    st.markdown("""
This app uses Auth0 for secure authentication, meaning your login credentials (such as email addresses) are handled and stored securely by Auth0, a trusted identity management platform.

- 🔒 Secure Storage: Your authentication data is protected by Auth0’s robust security infrastructure.
- 🗓️ Data Retention: This is a test application.
- 🚫 No Data Reuse: Your credentials will not be shared, reused, or repurposed for any other application or service.

If you have any questions or concerns, feel free to [reach out](mailto:edwardpriyatnax@gmail.com)  
""")
st.link_button(
    "Find Any Bug?",
    url="https://github.com/andfanilo/streamlit-auth0-test/issues",
    icon=":material/bug_report:",
    type="tertiary",
)

st.html("./styles.html")