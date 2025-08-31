import streamlit as st

# Page setup
st.set_page_config(page_title="Vishan's Dashboard", layout="centered")

# Create tabs
tab1, tab2, tab3 = st.tabs(["🏠 Home", "📚 Learn Together", "📈 CAPM Calculator"])

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

# Tab 3: CAPM Calculator
with tab3:
    st.subheader("📈 CAPM Expected Return Calculator")

    stock = st.text_input("Enter the name of the stock:")
    beta = st.number_input("Enter the stock beta:", value=1.0)
    risk_free_rate = st.number_input("Risk-free rate of return (%)", value=2.0)
    market_return = st.number_input("Expected market return (%)", value=8.0)

    if stock:
        expected_return = risk_free_rate + beta * (market_return - risk_free_rate)
        st.success(f"Using the CAPM formula, the expected return on **{stock}** is **{round(expected_return, 2)}%**")
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
