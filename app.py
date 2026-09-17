import streamlit as st
import requests
from bs4 import BeautifulSoup
import urllib.parse

# ==============================================================================
# 1. VISUAL DNA: PROMPT COMPILER THEME OVERRIDES
# ==============================================================================
st.set_page_config(page_title="Universal Prompt Compiler", page_icon="🔄", layout="centered")

st.markdown("""
    <style>
    .brand-title { font-size: 28px; font-weight: 800; color: #1f2328; text-align: center; margin-top: 10px; }
    .tagline { text-align: center; font-size: 16px; color: #57606a; margin-bottom: 25px; }
    .prompt-container-box { background-color: #f6f8fa; border: 1px solid #d0d7de; border-radius: 6px; padding: 20px; margin-top: 25px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="brand-title">🔄 Universal Prompt Compiler</div>', unsafe_allow_html=True)
st.markdown('<div class="tagline">Turn any website or repository into a high-fidelity visual-style AI developer prompt.</div>', unsafe_allow_html=True)

# ==============================================================================
# 2. MAIN INPUT BAR INTERFACE
# ==============================================================================
url_bar_input = st.text_input(
    "Paste complete GitHub Repository, live Portfolio, or Web App address here:", 
    value="https://firebaseapp.com",
    placeholder="e.g., https://github.com or https://firebaseapp.com"
)

# ==============================================================================
# 3. ADVANCED DESIGN TOKEN TRANSLATOR ENGINE
# ==============================================================================
def extract_visual_design_tokens(url):
    cleaned = url.strip()
    if not cleaned.startswith(("http://", "https://")):
        cleaned = "https://" + cleaned
        
    try:
        parsed = urllib.parse.urlparse(cleaned)
        domain_name = parsed.netloc
        
        page_title = domain_name
        scraped_features = []
        
        # Live DOM Crawl Pipeline to capture contextual page headers
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
            res = requests.get(cleaned, headers=headers, timeout=5)
            soup = BeautifulSoup(res.text, "html.parser")
            
            if soup.title and soup.title.string:
                page_title = soup.title.string.strip()
            
            # Extract actual H1/H2 text chunks to use as core feature instructions
            for heading in soup.find_all(["h1", "h2", "h3"])[:4]:
                h_text = heading.get_text().strip()
                if h_text and len(h_text) ', unsafe_allow_html=True)
            st.markdown("### 📋 Reconstructed Visual-Creator Prompt")
            st.caption("Copy this text and paste it into an AI tool like ChatGPT, Cursor, or Claude Code to build the frontend layout:")
            st.code(compiled_prompt, language="markdown")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a valid active URL link address target endpoint above to proceed.")
