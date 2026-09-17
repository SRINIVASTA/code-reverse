import streamlit as st
import requests
from bs4 import BeautifulSoup
import urllib.parse

# ==============================================================================
# 1. VISUAL DNA: CLEAN INTERFACE LAYOUT
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
st.markdown('<div class="tagline">Turn any public GitHub URL, Portfolio, or Web App Link into an AI prompt instantly.</div>', unsafe_allow_html=True)

# ==============================================================================
# 2. MAIN INPUT BAR INTERFACE
# ==============================================================================
url_bar_input = st.text_input(
    "Paste complete GitHub Repository, live Portfolio, or Web App address here:", 
    value="https://carbon-foot-70.firebaseapp.com/",
    placeholder="e.g., https://github.com or https://your-app.firebaseapp.com/"
)

# ==============================================================================
# 3. ADVANCED UNIVERSAL EXTRACTION ENGINE
# ==============================================================================
def extract_universal_details(url):
    cleaned = url.strip()
    if not cleaned.startswith(("http://", "https://")):
        cleaned = "https://" + cleaned
        
    try:
        parsed = urllib.parse.urlparse(cleaned)
        domain_name = parsed.netloc
        
        # Scenario A: Live GitHub Pages Web Links
        if ".github.io" in domain_name:
            owner_name = domain_name.split(".github.io")[0].upper()
            repo_name = f"{owner_name.lower()}.github.io"
            return owner_name, repo_name, "GitHub Pages Portfolio System Framework Layout", "Frontend View Layer Stack"

        # Scenario B: Standard Source Code Repositories on GitHub
        elif "github.com" in domain_name:
            path_segments = [seg for seg in parsed.path.split("/") if seg]
            if len(path_segments) >= 2:
                owner_name = path_segments[0].upper()
                repo_name = path_segments[1]
                return owner_name, repo_name, f"GitHub hosted source repository code assets mapping config.", "Comprehensive Full-Stack Code Architecture"

        # Scenario C: Generic Cloud Hosted Web Applications (Firebase, Vercel, Netlify, etc.)
        else:
            # Dynamically grab the website page title to use as the project signature name
            try:
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
                res = requests.get(cleaned, headers=headers, timeout=5)
                soup = BeautifulSoup(res.text, "html.parser")
                page_title = soup.title.string.strip() if soup.title else domain_name
            except:
                page_title = domain_name
                
            # Create standardized fallback placeholders matching the link characteristics
            project_signature = page_title.split("|")[0].strip()
            owner_placeholder = domain_name.split(".")[0].upper()
            
            return owner_placeholder, project_signature, f"Live deployed cloud web application hosted via infrastructure routing node {domain_name}.", "Production Application Stack Infrastructure"
            
    except Exception as e:
        pass
    return None, None, None, None

owner_extracted, repo_extracted, target_context, target_stack = extract_universal_details(url_bar_input)

# ==============================================================================
# 4. PROMPT ASSEMBLY & COMPILATION RADAR GRID
# ==============================================================================
if st.button("Get Prompt Blueprint", type="primary", use_container_width=True):
    if owner_extracted and repo_extracted:
        with st.spinner("Analyzing target metadata vectors and compiling blueprint blocks..."):
            
            # Formulate the compiled reverse-engineering prompt structure smoothly
            compiled_prompt = f"""You are an elite software engineering agent and system architect. Your objective is to recreate the complete, foundational system architecture of the project '{repo_extracted}' modeled from the deployment signature of '{owner_extracted}' from scratch.

### 1. Functional Specifications
- **Target Profile Focus:** Reconstruct a live application matching the architectural design constraints, structure, look and feel, and functional workflows of the target web asset at {url_bar_input}.
- **Context Classification:** {target_context}
- **Tech Stack Baseline:** Analyze underlying configuration scripts to render clean structural view layouts, semantic presentation containers, fluid responsive design components, and manage reactive user interactions over modern runtime event hooks.
- **Project Scope Tier:** {target_stack}

### 2. Implementation Rules
- Map out a clean, production-ready directory structure that supports atomic file separation guidelines.
- Write functional boilerplate code blocks to execute the primary user workflows and UI lifecycle events fluidly.
- Provide comprehensive step-by-step terminal instructions to configure, compile, and initialize this environment on a local machine.
"""
            
            # Print the generated text inside the browser view canvas box
            st.markdown('<div class="prompt-container-box">', unsafe_allow_html=True)
            st.markdown("### 📋 Reconstructed System Prompt Blueprint")
            st.caption("Copy this text and paste it into an AI tool like ChatGPT, Cursor, or Claude to build the project:")
            st.code(compiled_prompt, language="markdown")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a valid active URL link address target endpoint above to proceed.")
