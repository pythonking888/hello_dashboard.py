import streamlit as st

# Page setup
st.set_page_config(page_title="Vishan's Dashboard", layout="centered")

# Custom CSS for full neon city background and bold styling
st.markdown("""
    <style>
        html, body, .stApp {
            background-image: url('https://copilot.microsoft.com/th/id/BCO.a49133b4-ddd4-48bb-850d-4ae4ab5af51c.png');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
        }

        header, .viewerBadge_container__1QSob, .main, .block-container {
            background-color: rgba(0, 0, 0, 0.85) !important;
            background-image: none !important;
            border: none !important;
        }

        .block-container {
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(255, 0, 255, 0.3);
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
tab1, tab2 = st.tabs(["🏠 Home", "📈 CAPM Calculator"])

# Tab 1: Home
with tab1:
    st.title("👋 Hi Vishan")
    st.write("This is the beginning to the end.")
    st.markdown("---")
    st.caption("Styled by the skyline • Powered by vision")

# Tab 2: CAPM Calculator
with tab2:
    st.subheader("📈 CAPM Expected Return Calculator")

    stock = st.text_input("Enter the name of the stock:")
    beta = st.number_input("Enter the stock beta:", value=1.0)
    risk_free_rate = st.number_input("Risk-free rate of return (%)", value=2.0)
    market_return = st.number_input("Expected market return (%)", value=8.0)

    if stock:
        expected_return = risk_free_rate + beta * (market_return - risk_free_rate)
        st.success(f"Using the CAPM formula, the expected return on **{stock}** is **{round(expected_return, 2)}%**")
