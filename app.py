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
st.markdown('<div class="tagline">Turn any public URL or repository into a rich visual-creator UI prompt instantly.</div>', unsafe_allow_html=True)

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
        
        # Scrape page markup elements to deduce actual design context dynamically
        page_title = domain_name
        headings_found = []
        links_count = 0
        
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
            res = requests.get(cleaned, headers=headers, timeout=5)
            soup = BeautifulSoup(res.text, "html.parser")
            
            if soup.title and soup.title.string:
                page_title = soup.title.string.strip()
            
            # Gather top contextual keyword anchors from headers
            for h in soup.find_all(["h1", "h2", "h3"])[:4]:
                text = h.get_text().strip()
                if text and len(text) < 60:
                    headings_found.append(text)
                    
            links_count = len(soup.find_all("a"))
        except:
            pass

        # Set fallback descriptors if headings are empty
        if not headings_found:
            headings_found = ["Interactive Control Center Dashboard", "Analytics Telemetry Grid"]

        # Parse naming parameters cleanly
        project_signature = page_title.split("|")[0].split("-")[0].strip()
        owner_name = domain_name.split(".")[0].upper()
        
        if ".github.io" in domain_name:
            owner_name = domain_name.split(".github.io")[0].upper()
            project_signature = f"{owner_name.lower()}.github.io Portfolio"

        return {
            "owner": owner_name,
            "project": project_signature,
            "domain": domain_name,
            "headings": headings_found,
            "links_count": links_count if links_count > 0 else 12
        }
            
    except Exception as e:
        return None

extracted_meta = extract_universal_details(url_bar_input)

# ==============================================================================
# 4. VISUAL PROMPT ASSEMBLY MATRIX (MATCHES SECOND PRESENTATION STYLE)
# ==============================================================================
if st.button("Get Prompt Blueprint", type="primary", use_container_width=True):
    if extracted_meta:
        with st.spinner("Analyzing target metadata vectors and compiling visual-creator blocks..."):
            
            primary_heading = extracted_meta["headings"][0]
            sub_headings_list = "\n".join([f"- Show elements or sections dedicated to: '{h}'" for h in extracted_meta["headings"][1:]])
            
            # Compile the descriptive visual-forward system prompt block
            compiled_prompt = f"""Build me a '{extracted_meta["project"]}' style web app homepage that feels bright, friendly, and very visual, inspired by the deployment profile of '{extracted_meta["owner"]}'. I want a clean canvas, bold rounded sans-serif typography, a polished high-contrast text scaling hierarchy, and a distinct, vibrant accent color dedicated to the main interactive actions. 

The page layout must feel simple, welcoming, and intuitive to navigate. Start by designing a sticky navigation header component that includes the unique '{extracted_meta["project"]}' brand mark, a responsive search input bar, and prominent rounded call-to-action buttons for user onboarding.

The primary user experience should focus completely on interactive visual discovery and data representation. Construct a highly responsive, clean dashboard or grid layout full of engagement indicators, tailored specifically to handle:
- Main Focus area: '{primary_heading}'
{sub_headings_list}

Make the entire interface feel polished, approachable, and effortless to browse. All components—including cards, interactive form fields, and widgets—must features soft rounded corners, low-chrome outlines, and a generous balance of clean whitespace so the primary content structures stand out. Ensure the application is fully responsive and smooth, utilizing subtle hover scaling animations and consistent component margins to simulate a premium consumer product application interface.

Reference Destination for Layout Signature: {url_bar_input} (Parsed with approximately {extracted_meta["links_count"]} internal interaction nodes).
"""
            
            # Print the generated text inside the browser view canvas box
            st.markdown('<div class="prompt-container-box">', unsafe_allow_html=True)
            st.markdown("### 📋 Reconstructed Visual-Creator Prompt")
            st.caption("Copy this text and paste it into an AI tool like ChatGPT, Cursor, or Claude Code to build the frontend layout:")
            st.code(compiled_prompt, language="markdown")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a valid active URL link address target endpoint above to proceed.")
