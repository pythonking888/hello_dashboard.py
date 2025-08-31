import streamlit as st

# Page setup
st.set_page_config(page_title="Vishan's Dashboard", layout="centered")

# Apply full-page background and styling
st.markdown("""
<style>
    html, body, .stApp {
        background-image: url('https://copilot.microsoft.com/th/id/BCO.1f16e2e3-6407-4807-8fe0-9c6f1e0489cc.png');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }

    header, .viewerBadge_container__1QSob, .main, .block-container {
        background-color: transparent !important;
        background-image: none !important;
        border: none !important;
        box-shadow: none !important;
    }

    .stTextInput > div > input,
    .stNumberInput > div > input,
    .stMarkdown,
    .stSuccess,
    .stSubheader,
    label,
    .stCaption {
        color: #ffffff !important;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #00ffff;
        font-weight: 800;
        text-shadow: 0 0 8px #00ffff;
    }

    .stTabs [role="tablist"] {
        background-color: transparent;
        border-bottom: 2px solid #00ffff;
    }

    .stTabs [role="tab"] {
        color: #ffffff !important;
        background-color: rgba(0, 255, 255, 0.1);
        border: 1px solid #00ffff;
        margin-right: 0.5rem;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }

    .stTabs [aria-selected="true"] {
        background-color: #00ffff !important;
        color: #000000 !important;
        font-weight: bold;
        box-shadow: 0 0 10px #00ffff;
    }
</style>
""", unsafe_allow_html=True)

# Create tabs
home, capm = st.tabs(["🏠 Home", "📈 CAPM Calculator"])

# Tab 1: Home
with home:
    st.title("👋 Hi Vishan")
    st.write("This is the beginning to the end.")
    st.markdown("---")
    st.caption("Styled by the skyline • Powered by vision")

# Tab 2: CAPM Calculator
with capm:
    st.subheader("📈 CAPM Expected Return Calculator")

    stock = st.text_input("Enter the name of the stock:")
    beta = st.number_input("Enter the stock beta:", value=1.0)
    risk_free_rate = st.number_input("Risk-free rate of return (%)", value=2.0)
    market_return = st.number_input("Expected market return (%)", value=8.0)

    if stock:
        expected_return = risk_free_rate + beta * (market_return - risk_free_rate)
        st.success(f"Using the CAPM formula, the expected return on **{stock}** is **{round(expected_return, 2)}%**")
