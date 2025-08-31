import streamlit as st

# Page setup
st.set_page_config(page_title="Vishan's Dashboard", layout="centered")

# Title and intro
st.title("👋 Hi Vishan")
st.write("This is the beginning to the end.")

# Interactive prompt
st.subheader("Should we learn together?")
response = st.radio(
    "Choose your answer:",
    ["Yes, let's do it!", "Maybe later", "Not today"]
)

# Response handling
if response == "Yes, let's do it!":
    st.success("Awesome! Let's dive into something exciting together. 🚀")
elif response == "Maybe later":
    st.info("No worries—I'll be here when you're ready. 😊")
elif response == "Not today":
    st.warning("Totally fine. Everyone needs a break sometimes. 💤")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
