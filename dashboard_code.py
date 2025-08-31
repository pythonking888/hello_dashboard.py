import streamlit as st

st.set_page_config(page_title="Vishan's Dashboard", layout="centered")

# Tabs setup
tab1, tab2 = st.tabs(["🏠 Home", "📚 Learn Together"])

# Tab 1: Home
with tab1:
    st.title("👋 Hi Vishan")
    st.write("This is the beginning to the end.")

# Tab 2: Learn Together
with tab2:
    st.subheader("Should we learn together?")
    response = st.radio(
        "Choose your answer:",
        ["Yes, let's do it!", "Maybe later", "Not today"]
    )

    if response == "Yes, let's do it!":
        st.success("Awesome! Let's dive into something exciting together. 🚀")
    elif response == "Maybe later":
        st.info("No worries—I'll be here when you're ready. 😊")
    elif response == "Not today":
        st.warning("Totally fine. Everyone needs a break sometimes. 💤")
