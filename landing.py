import streamlit as st

# Print entire secrets dictionary
st.write("Secrets loaded:", st.secrets)
st.title("📔 Streamlit + Auth0 Production test")

# Check if the user is already logged in
if "auth_token" in st.session_state:
    st.write("You are logged in!")
else:
    if st.button("Login with Auth0"):
        # Trigger login process, e.g., st.login("auth0")
        # Here you'd normally integrate with your auth system
        st.write("Redirecting to Auth0...")
        # After successful login, set the auth token
        st.session_state.auth_token = "fake_token"  # Use the real token here
        st.write("Successfully logged in!")

st.markdown(
    "Hello DataFan, help me benchmark [Auth0](https://auth0.com/) for a future video by connecting with Google or creating an Email/Password account with verification 😁"
)

st.write("\n")

if st.button(
    "✨ Sign up to the DataFan Store",
    type="primary",
    key="checkout-button",
    use_container_width=True,
):
    # st.login("google")
    st.login("auth0")

if st.session_state.get("auth_status") == "logged_in":
    st.write("Successfully Logged In!")

with st.expander("📝 Privacy & Data Security Disclaimer"):
    st.markdown("""
This app uses Auth0 for secure authentication, meaning your login credentials (such as email addresses) are handled and stored securely by Auth0, a trusted identity management platform.

- 🔒 Secure Storage: Your authentication data is protected by Auth0’s robust security infrastructure.
- 🗓️ Data Retention: This is a test application. All user data, including email addresses, will be permanently deleted by March 31st when the video is released.
- 🚫 No Data Reuse: Your credentials will not be shared, reused, or repurposed for any other application or service.

If you have any questions or concerns, feel free to [reach out](mailto:contant@andfanilo.com)  
""")
st.link_button(
    "Find Any Bug?",
    url="https://github.com/andfanilo/streamlit-auth0-test/issues",
    icon=":material/bug_report:",
    type="tertiary",
)

st.html("./styles.html")