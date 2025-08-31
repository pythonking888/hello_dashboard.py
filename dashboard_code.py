import streamlit as st

# Page setup
st.set_page_config(page_title="Vishan's Dashboard", layout="centered")

# Create tabs
tab1, tab2, tab3 = st.tabs(["🏠 Home", "📈 CAPM Calculator"])

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
        st.markdown("""
    <style>
import streamlit as st

# Page setup
st.set_page_config(page_title="FOREX Futuristic Dashboard", layout="centered")

# Custom CSS for full background, bold fonts, and vibrant contrast
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

        .block-container {
            background-color: rgba(0, 0, 0, 0.85);
    
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
        }

        h1, h2, h3, h4, h5, h6 {
            color: #00ffff;
            font-weight: 800;
            text-shadow: 0 0 5px #00ffff;
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

# Tabs
tab1, tab2 = st.tabs(["🏠 Home", "📈 Forex"])

# Tab 1: Home
with tab1:
    st.title("🚀 Welcome to the New World Order")
    st.write("This dashboard is your gateway to global currency intelligence.")

# Tab 2: Forex
with tab2:
    st.subheader("💱 Market Signals")
    st.write("Explore trends, candlestick patterns, and futuristic analytics.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit • Styled for the future • FOREX ready")

