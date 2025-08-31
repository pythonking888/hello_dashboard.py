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

# Page setup
st.set_page_config(page_title="Monochrome Dashboard", layout="centered")

# Custom CSS for black background and white tabs
st.markdown("""
    <style>
        .stApp {
            background-color: #000000;
            color: #ffffff;
        }
        .stTabs [role="tablist"] {
            background-color: #000000;
            border-bottom: 1px solid #ffffff;
        }
        .stTabs [role="tab"] {
            color: #ffffff !important;
            background-color: #000000;
            border: 1px solid #ffffff;
            border-radius: 0;
            margin-right: 0.5rem;
            padding: 0.5rem 1rem;
        }
        .stTabs [aria-selected="true"] {
            background-color: #ffffff !important;
            color: #000000 !important;
            font-weight: bold;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff;
        }
        .block-container {
            padding: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2 = st.tabs(["🏠 Home", "📈 Forex"])

# Tab 1: Home
with tab1:
    st.title("🖤 Monochrome Dashboard")
    st.write("Welcome to your black & white command center.")

# Tab 2: Forex
with tab2:
    st.subheader("FOREX Market Overview")
    st.write("Explore currency trends and trading insights in minimalist style.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit • Styled in black & white")
