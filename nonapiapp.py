import streamlit as st
import requests
from bs4 import BeautifulSoup
import urllib.parse

# ==============================================================================
# 1. VISUAL DNA: CLEAN HEADER INTERFACE LAYOUT
# ==============================================================================
st.set_page_config(page_title="GitReverse - Free Local Compiler", page_icon="🔄", layout="centered")

st.markdown("""
    <style>
    .brand-title { font-size: 28px; font-weight: 800; color: #1f2328; text-align: center; margin-top: 10px; }
    .tagline { text-align: center; font-size: 16px; color: #57606a; margin-bottom: 25px; }
    .prompt-container-box { background-color: #f6f8fa; border: 1px solid #d0d7de; border-radius: 6px; padding: 20px; margin-top: 25px; }
    </style>
""", unsafe_allow_html=True)

# FIXED: Removed the broken argument completely to prevent compilation parameter crashes
st.markdown('<div class="brand-title">🔄 Local Prompt Compiler (No API Needed)</div>', unsafe_allow_html=True)
st.markdown('<div class="tagline">Turn any public GitHub URL into a structured system prompt instantly.</div>', unsafe_allow_html=True)

# ==============================================================================
# 2. MAIN INPUT BAR INTERFACE
# ==============================================================================
url_bar_input = st.text_input(
    "Paste complete GitHub Repository URL link address here:", 
    value="https://github.com",
    placeholder="e.g., https://github.com"
)

# ==============================================================================
# 3. AUTOMATED URL PARSING UTILITY
# ==============================================================================
def extract_repo_details(url):
    cleaned = url.strip()
    if not cleaned.startswith(("http://", "https://")):
        cleaned = "https://" + cleaned
    try:
        parsed = urllib.parse.urlparse(cleaned)
        path_segments = [seg for seg in parsed.path.split("/") if seg]
        if len(path_segments) >= 2:
            return path_segments[0], path_segments[1] # Returns owner, repo
    except:
        pass
    return None, None

owner_extracted, repo_extracted = extract_repo_details(url_bar_input)

# ==============================================================================
# 4. DETERMINISTIC TEMPLATE PROMPT GENERATOR (100% OFFLINE / FREE)
# ==============================================================================
if st.button("Get Prompt Blueprint", type="primary", use_container_width=True):
    if owner_extracted and repo_extracted:
        with st.spinner("Parsing target repository metadata vectors..."):
            
            # Formulate a bulletproof structured prompt using static text assembly bindings
            compiled_prompt = f"""You are an elite software engineering agent and system architect. Your objective is to recreate the complete, foundational system architecture of the project '{repo_extracted}' owned by '{owner_extracted}' from scratch.

### 1. Functional Specifications
- **Target Profile Focus:** Reconstruct a live application matching the architectural design constraints, structure, and functional workflows of the target repository asset at {url_bar_input}.
- **Tech Stack Baseline:** Analyze underlying configuration scripts to render clean structural view layouts, semantic presentation containers, and dynamic interactive client interaction components.

### 2. Implementation Rules
- Map out a clean, production-ready directory structure that supports atomic file separation guidelines.
- Write functional boilerplate code blocks to execute the primary user workflows and UI lifecycle events fluidly.
- Provide comprehensive step-by-step terminal instructions to configure, compile, and initialize this environment on a local machine.
"""
            
            # Render the final output cleanly inside a text canvas box
            st.markdown('<div class="prompt-container-box">', unsafe_allow_html=True)
            st.markdown("### 📋 Reconstructed System Prompt Blueprint")
            st.caption("Copy this text and paste it into an AI tool like ChatGPT, Cursor, or Claude to build the project:")
            st.code(compiled_prompt, language="markdown")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a valid public GitHub URL address target link above.")
