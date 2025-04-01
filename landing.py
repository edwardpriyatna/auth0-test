import streamlit as st

# Check if the user is authenticated using the key set by st.login("auth0")
if st.session_state.get("auth0_authenticated", False):
    # --- CONTENT SHOWN *ONLY* WHEN LOGGED IN ---
    st.success("✅ Successfully logged in!")
    # You can add more content here that should only be visible
    # to logged-in users.
    # For example:
    # st.write(f"Welcome, {st.session_state.get('auth0_user_email', 'User')}!") # Assuming email is available
    # st.header("Your Dashboard")
    # ... other authenticated user content ...

else:
    # --- CONTENT SHOWN *ONLY* WHEN *NOT* LOGGED IN ---
    st.title("📔 Streamlit + Auth0 Production Test")
    st.markdown("Stroke Prediction Model Using Time Series Data")

    with st.container(border=True):
        # Make sure the image path is correct relative to your script's location
        # If the script and the 'img' folder are in the same directory:
        try:
            st.image("./img/demo.gif")
        except FileNotFoundError:
            st.warning("Warning: demo.gif not found at ./img/demo.gif")
        except Exception as e:
            st.error(f"Error loading image: {e}")


    st.write("\n") # Adds a little vertical space

    # The login button itself should only be shown if the user is NOT logged in
    if st.button(
        "✨ Sign up / Log in via Auth0", # Clarified button text
        type="primary",
        key="auth0-login-button", # Using a descriptive key is good practice
        use_container_width=True,
    ):
        # This command initiates the Auth0 login flow.
        # After successful login, Streamlit sets specific session state keys
        # (like "auth0_authenticated") and reruns the script.
        st.login("auth0")

    # The disclaimer and bug report link are also part of the "logged out" view
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

# --- CONTENT SHOWN REGARDLESS OF LOGIN STATUS (Optional) ---
# If you had any content that should *always* appear (like a footer),
# you would put it here, outside the if/else block.
# st.caption("App Version 1.0")