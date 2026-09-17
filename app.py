import streamlit as st
import requests
from bs4 import BeautifulSoup
import urllib.parse

# Import the official SDK library that worked in your Colab notebook
try:
    from google import genai
except ImportError:
    st.error("⚠️ The 'google-genai' library is missing. Please make sure your requirements.txt contains 'google-genai'.")

# ==============================================================================
# 1. VISUAL DNA: EXACT FRONTEND REPLICATION (CLEAN INTERFACE)
# ==============================================================================
st.set_page_config(page_title="Code-Reverse - Reverse into a prompt", page_icon="🔄", layout="centered")

st.markdown("""
    <style>
    /* Clean Minimalist Nav and Typography Layout */
    .brand-navigation { display: flex; justify-content: space-between; align-items: center; margin-bottom: 40px; }
    .brand-title { font-size: 28px; font-weight: 800; color: #1f2328; letter-spacing: -0.5px; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
    .brand-links { font-size: 14px; font-weight: 500; color: #0969da; }
    .brand-links a { text-decoration: none; color: #0969da; margin-left: 15px; }
    .main-tagline { font-size: 40px; font-weight: 800; text-align: center; color: #1f2328; margin-top: 30px; margin-bottom: 8px; letter-spacing: -1px; }
    .main-sub { font-size: 18px; text-align: center; color: #57606a; margin-bottom: 35px; }
    
    /* Center Toggles and Forms */
    .stRadio > div { justify-content: center; margin-bottom: 15px; }
    div[data-baseweb="input"] { border-radius: 6px !important; }
    .preset-label { font-size: 13px; color: #57606a; margin-top: 25px; margin-bottom: 8px; }
    
    /* Result Windows */
    .prompt-container-box { background-color: #f6f8fa; border: 1px solid #d0d7de; border-radius: 6px; padding: 20px; margin-top: 25px; }
    </style>
""", unsafe_allow_html=True)

# Predefined fallback options for the layout badges
PRESET_REPOS = ["Next.js", "Openclaw", "React", "Supabase", "Linux"]
PRESET_SITES = ["YouTube", "Pinterest", "Xbox", "Apple", "Discord"]

# ==============================================================================
# 2. LLM ENGINE USING OFFICIAL SDK (REPLACED RAW REQUESTS TO PREVENT URL MIXUPS)
# ==============================================================================
def call_gemini_ai(scanned_context):
    """
    Calls Google's official GenAI SDK library directly, mirroring your successful
    Colab connection. This protects against URL parameter concatenation errors.
    """
    api_key = st.session_state.get("api_key_input", "").strip()
    if not api_key:
        return "⚠️ Please enter your free Gemini API Key in the sidebar to generate custom live prompts!"
        
    try:
        # Initialize the client with your key, just like your Colab Step 3
        client = genai.Client(api_key=api_key)
        
        prompt_instruction = (
            "You are the backend engine of Code-Reverse. Take this raw scraped website text data "
            "and reverse-engineer it into a single, conversational user prompt. The prompt must "
            "be written in natural language, describing exactly how to build this specific project "
            "from scratch. Do not write folder diagrams or markdown structures. Write the exact "
            "prompt that a developer would copy and paste into Cursor or Claude Code to build it. "
            f"Raw Scraped Data: {scanned_context}"
        )
        
        # Run content generation with the modern gemini-2.5-flash model from your Colab test
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt_instruction
        )
        
        return response.text.strip()
        
    except Exception as e:
        return f"❌ API Key Processing Error: {str(e)}"

def extract_live_github_data(url):
    """
    Scrapes the actual page text layout of any public web target to capture its real context.
    """
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        res = requests.get(url, headers=headers, timeout=8)
        if res.status_code != 200:
            return None, f"Server rejected repository fetch loop with status code: {res.status_code}"
        
        soup = BeautifulSoup(res.text, "html.parser")
        page_text = " ".join([t.get_text().strip() for t in soup.find_all(["h1", "h2", "p", "li"]) if t.get_text()])
        return page_text[:4000], None 
    except Exception as e:
        return None, str(e)

# ==============================================================================
# 3. INTERACTIVE LAYOUT RENDERING FRAMEWORK
# ==============================================================================
# Sidebar API Configuration Panel
st.sidebar.markdown("### 🔑 API Key Configuration")
st.sidebar.markdown("Code-Reverse uses an LLM to generate custom prompts. You can get a free, no-cost key in 30 seconds at [Google AI Studio](https://google.com).")
st.sidebar.text_input("Enter Gemini API Key:", type="password", key="api_key_input")

if st.sidebar.button("Clear Application Logs", use_container_width=True):
    st.session_state.prompt_output = None
    st.rerun()

# Top Navigation Strip
st.markdown("""
    <div class="brand-navigation">
        <div class="brand-title">Code-Reverse</div>
        <div class="brand-links">
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-tagline">Reverse into a prompt</div>', unsafe_allow_html=True)
st.markdown('<div class="main-sub">Reverse engineer any codebase or website into a prompt.</div>', unsafe_allow_html=True)

if "prompt_output" not in st.session_state:
    st.session_state.prompt_output = None

# Selection Tabs
mode = st.radio("Toggle Mode", ["Codebase", "Website"], horizontal=True, label_visibility="collapsed")

# Main Text Form Search Field
placeholder = "https://github.com" if mode == "Codebase" else "https://youtube.com"
url_bar_input = st.text_input("Input Target", placeholder=placeholder, label_visibility="collapsed")

if st.button("Get Prompt", type="primary", use_container_width=True):
    if url_bar_input.strip():
        with st.spinner("Analyzing repository deployment configurations and invoking AI compiler..."):
            context_data, error = extract_live_github_data(url_bar_input)
            if error:
                st.error(f"Scraping Error: {error}")
            else:
                st.session_state.prompt_output = call_gemini_ai(context_data)
    else:
        st.warning("Please enter a valid target link address first.")

# Quick-Click Presets Selection Badges
st.markdown("<br>", unsafe_allow_html=True)
presets = PRESET_REPOS if mode == "Codebase" else PRESET_SITES
st.markdown(f'<div class="preset-label">Try example {"repos" if mode == "Codebase" else "websites"}:</div>', unsafe_allow_html=True)

badge_cols = st.columns(5)
for idx, item in enumerate(presets):
    with badge_cols[idx]:
        if st.button(item, key=f"badge_{item}", use_container_width=True):
            mock_url = f"https://github.com{item}" if mode == "Codebase" else f"https://www.{item.lower()}.com"
            with st.spinner(f"Processing preset template for {item}..."):
                context_data, _ = extract_live_github_data(mock_url)
                st.session_state.prompt_output = call_gemini_ai(f"Project Workspace Preset: {item}. Meta Data Context: {context_data}")
                st.rerun()

# ==============================================================================
# 4. FINAL RENDER OUTPUT CANVAS
# ==============================================================================
if st.session_state.prompt_output:
    st.markdown('<div class="prompt-container-box">', unsafe_allow_html=True)
    st.markdown("### 📋 Reconstructed System Prompt")
    st.code(st.session_state.prompt_output, language="markdown")
    st.markdown('</div>', unsafe_allow_html=True)
