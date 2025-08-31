import streamlit as st

# Page configuration
st.set_page_config(
    page_title="FOREX Dashboard",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS to set background image and dark overlay
st.markdown("""
    <style>
        .stApp {
            background-image: url("https://copilot.microsoft.com/th/id/BCO.b0fb40e7-2e58-4f3b-b681-83f774415895.png");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: #ffffff;
        }
        .block-container {
            background-color: rgba(0, 0, 0, 0.6);
            padding: 2rem;
            border-radius: 10px;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #00ffcc;
        }
    </style>
""", unsafe_allow_html=True)

# Main content
st.title("🌍 FOREX Market Dashboard")
st.write("Welcome to your global trading command center.")

st.markdown("### 💱 Currency Insights")
st.write("Explore exchange rates, market trends, and trading signals.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Stream