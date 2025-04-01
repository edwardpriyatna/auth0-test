import streamlit as st

# Check if the user is authenticated
if st.session_state.get("auth0_authenticated", False):
    st.success("✅ Successfully logged in!")
else:
    st.title("📔 Streamlit + Auth0 Production Test")

    st.markdown("Stroke Prediction Model Using Time Series Data")

    with st.container(border=True):
        st.image("./img/demo.gif")

    st.write("\n")

    if st.button(
        "✨ Sign up to our app",
        type="primary",
        key="checkout-button",
        use_container_width=True,
    ):
        st.login("auth0")  # This triggers Auth0 authentication

    with st.expander("📝 Privacy & Data Security Disclaimer"):
        st.markdown("""
        This app uses Auth0 for secure authentication, meaning your login credentials 
        (such as email addresses) are handled and stored securely by Auth0.

        - 🔒 Secure Storage: Your authentication data is protected.
        - 🗓️ Data Retention: This is a test application.
        - 🚫 No Data Reuse: Your credentials will not be shared or repurposed.

        If you have any questions, feel free to [reach out](mailto:edwardpriyatnax@gmail.com)  
        """)
    st.link_button(
        "Find Any Bug?",
        url="https://github.com/andfanilo/streamlit-auth0-test/issues",
        icon=":material/bug_report:",
        type="tertiary",
    )

