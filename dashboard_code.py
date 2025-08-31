import streamlit as st

# Page setup
st.set_page_config(page_title="Vishan's Dashboard", layout="centered")

# Custom CSS for neon city background and bold styling
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
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(255, 0, 255, 0.3);
        }

        h1, h2, h3, h4, h5, h6 {
            color
