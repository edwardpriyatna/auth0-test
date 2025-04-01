import streamlit as st

# Ensure session state keys exist
if "auth0_authenticated" not in st.session_state:
    st.session_state.auth0_authenticated = False  # Default to not authenticated
if "auth0_user_info" not in st.session_state:
    st.session_state.auth0_user_info = None  # No user info initially

# Debugging: Show current session state
st.subheader("Current Session State:")
st.write(st.session_state)
st.divider()

# Define authentication callback
def handle_auth():
    """Callback function to update session state after login"""
    if st.session_state.get("auth0_authenticated", False):
        st.success("✅ Successfully logged in!")
    else:
        st.warning("⚠️ Authentication failed. Please try again.")

# Check if the user is authenticated
if st.session_state.auth0_authenticated:
    st.success("✅ Successfully logged in!")
    
    # Display user info if available
    if st.session_state.auth0_user_info:
        user_info = st.session_state.auth0_user_info
        st.write(f"Welcome, {user_info.get('name', user_info.get('email', 'User'))}!")
    
    # Add logout button
    if st.button("Log Out"):
        st.session_state.auth0_authenticated = False  # Reset authentication
        st.session_state.auth0_user_info = None  # Clear user data
        st.rerun()

else:
    st.title("📔 Stroke Prediction Model Using Time Series Data")

    with st.container(border=True):
        try:
            st.image("./img/stroke-brain.gif", use_container_width=True)
        except Exception as e:
            st.warning(f"Could not load image: {e}")

    st.write("\n")

    # Auth0 Login Button with Callback
    if st.button("✨ Sign up / Log in via Auth0", type="primary", key="auth0-login-button", use_container_width=True):
        st.login("auth0", on_success=handle_auth)  # Pass callback function

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
