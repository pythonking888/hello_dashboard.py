import streamlit as st

# Page setup
st.set_page_config(page_title="Vishan's Dashboard", layout="centered")

# Create tabs
tab1, tab2, tab3 = st.tabs(["🏠 Home", "📚 Learn Together", "📈 CAPM Calculator"])

# Tab 1: Home
with tab1:
    st.title("👋 Hi Vishan")
    st.write("This is the beginning to the end.")

# Tab 2: CAPM Calculator
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
import streamlit as st

# Page setup
st.set_page_config(page_title="Styled Dashboard", layout="centered")

# Custom CSS for dark background and white tabs
st.markdown("""
    <style>
        .stApp {
            background-color: #0f0f0f;
            color: #ffffff;
        }
        .stTabs [role="tablist"] {
            background-color: #1a1a1a;
            border-radius: 8px;
            padding: 0.5rem;
        }
        .stTabs [role="tab"] {
            color: #ffffff !important;
            background-color: #333333;
            border: 1px solid #555555;
            border-radius: 6px;
            margin-right: 0.5rem;
            padding: 0.5rem 1rem;
        }
        .stTabs [aria-selected="true"] {
            background-color: #ffffff !important;
            color: #000000 !important;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2 = st.tabs(["🏠 Home", "📈 Forex"])

# Tab 1: Home
with tab1:
    st.title("Welcome to the Styled Dashboard")
    st.write("This tab has a dark background and white-highlighted tabs.")

# Tab 2: Forex
with tab2:
    st.subheader("FOREX Market Overview")
    st.write("Here you can explore currency trends and trading insights.")

