import streamlit as st

# Page setup
st.set_page_config(page_title="Vishan's Futuristic Dashboard", layout="centered")

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

        header, .viewerBadge_container__1QSob, .main {
            background-color: rgba(0, 0, 0, 0.85) !important;
            background-image: none !important;
            border: none !important;
        }

        .block-container {
            background-color: rgba(0, 0, 0, 0.85);
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
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
            box-shadow: 0 0 10px
