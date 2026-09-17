import streamlit as st
from app import analyze_url

# Configure the Streamlit webpage layout
st.set_page_config(page_title="GitReverse Monitor", layout="wide")
st.title("🔄 GitReverse Architecture Tokens Viewer")

# User entry input bar
url_target = st.text_input(
    "Enter Web URL or GitHub Path:", 
    placeholder="://github.com"
)

if url_target:
    # Trigger the universal layout parser function
    tokens = analyze_url(url_target)
    
    # Render layout properties into metric columns cleanly
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Branding Shell Name", tokens["title"])
    col2.metric("Canvas Color Token", tokens["bg_color"])
    col3.metric("Primary Accent UI Token", tokens["accent_color"])
    col4.metric("Border Radius Rule", tokens["border_radius"])
    
    st.subheader(tokens["hero_title"])
    st.info(tokens["hero_desc"])
    
    # Inject live sandboxed markup view display inside Streamlit canvas
    st.markdown(f"""
    <div style='background-color:{tokens["bg_color"]}; color:{tokens["text_color"]}; padding:30px; border-radius:{tokens["border_radius"]}; border:1px solid rgba(128,128,128,0.2);'>
        <h3>Live Architecture Token Simulation Frame Content</h3>
        <p>Font Family applied: <code>{tokens["font_family"]}</code></p>
        <button style='background-color:{tokens["accent_color"]}; color:white; border:none; padding:10px 20px; border-radius:{tokens["border_radius"]}; font-weight:bold; cursor:pointer;'>
            Dynamic Computed Button Layout Action
        </button>
    </div>
    """, unsafe_allow_html=True)
