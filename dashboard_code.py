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
        import streamlit as st

# Page setup
st.set_page_config(page_title="China at Night Dashboard", layout="centered")

# Custom CSS for full neon city background and bold styling
st.markdown("""
    <style>
        .block-container {
            padding: 2rem;
        }
    </style>
""", unsafe_allow_html=True)
