from pathlib import Path
import joblib
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import authlib

st.title("📔 Streamlit + Auth0 Production test")

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
    st.login("google")

with st.sidebar:
    st.header(f"Logged in with {st.experimental_user.email}")
    if st.button("🔓 Logout"):
        st.logout()
    with st.expander(
        "Checkout your `st.experimental_user` local ID Token from the Identity Provider, securely stored in a cookie that expires in 30 days"
    ):
        st.json(st.experimental_user)
    st.link_button(
        "Find Any Bug?",
        url="https://github.com/andfanilo/streamlit-auth0-test/issues",
        icon=":material/bug_report:",
        type="tertiary",
    )