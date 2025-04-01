import streamlit as st

# --- Add this for debugging ---
st.subheader("Current Session State:")
st.write(st.session_state)
st.divider()
# -----------------------------

# Check if the user is authenticated
if st.session_state.get("auth0_authenticated", False):
    # --- CONTENT SHOWN *ONLY* WHEN LOGGED IN ---
    st.success("✅ Successfully logged in!")
    # Optionally display user info if available
    if "auth0_user_info" in st.session_state:
        user_info = st.session_state.auth0_user_info
        st.write(f"Welcome, {user_info.get('name', user_info.get('email', 'User'))}!")
        # st.write("User Info:") # Uncomment to see all user data
        # st.write(user_info)   # Uncomment to see all user data

    # Add other content for logged-in users here
    # st.header("Your Stroke Prediction Dashboard")
    # ...

    # Add a logout button for logged-in users
    if st.button("Log Out"):
        st.logout() # Use st.logout() for Auth0

else:
    # --- CONTENT SHOWN *ONLY* WHEN *NOT* LOGGED IN ---
    st.title("📔 Stroke Prediction Model Using Time Series Data")

    with st.container(border=True):
        try:
            st.image("./img/stroke-brain.gif",use_container_width =True)
        except Exception as e:
            st.warning(f"Could not load ./img/demo.gif: {e}") # More informative error

    st.write("\n")

    if st.button(
        "✨ Sign up / Log in via Auth0", # Clarified button text
        type="primary",
        key="auth0-login-button",
        use_container_width=True,
    ):
        st.login("auth0") # This triggers Auth0 authentication

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
        url="https://github.com/andfanilo/streamlit-auth0-test/issues", # Make sure this repo is relevant
        icon=":material/bug_report:",
        type="tertiary",
    )

# Optional Footer (always shown)
# st.caption("App v1.0")