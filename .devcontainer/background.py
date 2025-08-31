import streamlit as st

# Set dark theme manually (Streamlit Cloud uses your repo's config)
st.set_page_config(
    page_title="Vishan's Futuristic Dashboard",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark styling (optional enhancement)
st.markdown("""
    <style>
        body {
            background-color: #0f0f0f;
            color: #ffffff;
        }
        .stApp {
            background-color: #0f0f0f;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

# Title and intro
st.title("🧠 Welcome to the Future, Vishan")
st.write("This dashboard runs on dark matter and Python logic.")

# Futuristic art
st.image("https://copilot.microsoft.com/th/id/BCO.82fbaee8-f4d2-4046-abfa-e73613f52af2.png", caption="Futuristic Python Vibes", use_column_width=True)

# Interactive prompt
st.markdown("### Should we learn together?")
response = st.radio("Choose your answer:", ["Yes, let's do it!", "Maybe later", "Not today"])

if response == "Yes, let's do it!":
    st.success("Initiating neural sync... 🚀")
elif response == "Maybe later":
    st.info("Temporal delay accepted. Awaiting next signal. 🕒")
else:
    st.warning("Mission aborted. Recharging core. 💤")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit • Powered by Python • Styled for the future")
