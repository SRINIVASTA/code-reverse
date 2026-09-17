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
st.markdown('<div class="tagline">Turn any website, web app, or repository into a rich visual-style AI developer prompt.</div>', unsafe_allow_html=True)

# ==============================================================================
# 2. MAIN INPUT BAR INTERFACE
# ==============================================================================
url_bar_input = st.text_input(
    "Paste complete GitHub Repository, live Portfolio, or Web App address here:", 
    value="https://firebaseapp.com",
    placeholder="e.g., https://github.com or https://firebaseapp.com"
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
        
        page_title = domain_name
        headings_found = []
        inferred_keywords = []
        
        # Scrape page markup elements to deduce actual design context dynamically
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
            res = requests.get(cleaned, headers=headers, timeout=5)
            soup = BeautifulSoup(res.text, "html.parser")
            
            if soup.title and soup.title.string:
                page_title = soup.title.string.strip()
            
            # Gather top contextual keyword anchors from headers
            for h in soup.find_all(["h1", "h2", "h3"])[:4]:
                text = h.get_text().strip()
                if text and len(text) < 60 and text not in headings_found:
                    headings_found.append(text)
            
            # Look for general descriptive tokens to extract features automatically
            text_blocks = " ".join([p.get_text().lower() for p in soup.find_all(["p", "span"])[:10]])
            for word in ["dashboard", "feed", "calculator", "chart", "map", "profile", "portfolio", "timeline", "grid", "form", "analytics"]:
                if word in text_blocks and word not in inferred_keywords:
                    inferred_keywords.append(word)
        except:
            pass

        # Setup intelligent clean fallbacks based on domain categorization patterns if scraping fails
        if ".github.io" in domain_name:
            owner_name = domain_name.split(".github.io")[0].upper()
            project_signature = page_title.split("|")[0].split("-")[0].strip() if page_title != domain_name else f"{owner_name} Portfolio"
            features = ["Personal projects bio showcase", "Interactive skills badges grid", "Contact form wrapper container"]
            theme = "clean minimalist light/dark slate look, subtle accents, roomy whitespace lines, and smooth slide transitions"
        elif "github.com" in domain_name:
            path_segments = [seg for seg in parsed.path.split("/") if seg]
            owner_name = path_segments[0].upper() if len(path_segments) > 0 else "Developer"
            project_signature = path_segments[1] if len(path_segments) > 1 else "Repository Source"
            features = ["Dynamic system module routing file views", "Boilerplate execution loops setups", "Clean markdown documentation blocks handles"]
            theme = "technical code-focused dark look, crisp monospaced tracking widgets, and subtle status tier badges indicators"
        else:
            owner_name = domain_name.split(".")[0].upper()
            project_signature = page_title.split("|")[0].split("-")[0].strip()
            
            # Map dynamic components out of scraped headings/keywords
            features = headings_found if headings_found else ["Interactive calculation control modules", "Data metrics monitoring visualization tracking grid"]
            if inferred_keywords:
                features.extend([f"Dynamic components processing a real-time {k} interface loop" for k in inferred_keywords[:2]])
            
            theme = "modern high-concurrency cloud dashboard look, soft rounded asset corners, crisp card frames outlines, and vibrant action indicators"

        return {
            "owner": owner_name,
            "project": project_signature,
            "domain": domain_name,
            "features": features[:4],
            "theme_vibe": theme
        }
            
    except Exception as e:
        return None

extracted_meta = extract_universal_details(url_bar_input)

# ==============================================================================
# 4. VISUAL PROMPT ASSEMBLY MATRIX (MATCHES COMPACT SECOND STYLE RULES)
# ==============================================================================
if st.button("Get Prompt Blueprint", type="primary", use_container_width=True):
    if extracted_meta:
        with st.spinner("Analyzing target parameters and compiling visual-creator prompt..."):
            
            # Format feature arrays cleanly into natural text instructions points
            feature_bullet_points = "\n".join([f"- {f}" for f in extracted_meta["features"]])
            
            # Compile the descriptive visual-forward system prompt block
            compiled_prompt = f"""Build me a '{extracted_meta["project"]}' style web app homepage that feels bright, friendly, and very visual, inspired by the interface framework profile of '{extracted_meta["owner"]}'. I want a clean canvas, bold rounded sans-serif typography, a polished high-contrast text scaling hierarchy, and a distinct, vibrant accent color dedicated to the main interactive actions. 

The page layout must feel simple, welcoming, and intuitive to navigate. Start by designing a sticky navigation header component that includes the unique '{extracted_meta["project"]}' brand mark, a responsive search input bar, and prominent rounded call-to-action buttons for user onboarding.

The primary user experience should focus completely on interactive visual discovery and data representation. Construct a highly responsive, clean dashboard or grid layout full of engagement indicators, tailored specifically to handle:
{feature_bullet_points}

Make the entire interface feel polished, approachable, and effortless to browse. All components—including cards, interactive form fields, and widgets—must features soft rounded corners, low-chrome outlines, and a generous balance of clean whitespace so the primary content structures stand out. Ensure the application is fully responsive and smooth, utilizing subtle hover scaling animations and consistent component margins to simulate a premium consumer product application interface.

Reference Target Architecture Source: {url_bar_input} (Deducing design system tokens matching {extracted_meta["theme_vibe"]}).
"""
            
            # Print the generated text inside the browser view canvas box
            st.markdown('<div class="prompt-container-box">', unsafe_allow_html=True)
            st.markdown("### 📋 Reconstructed Visual-Creator Prompt")
            st.caption("Copy this text and paste it into an AI tool like ChatGPT, Cursor, or Claude Code to build the frontend layout:")
            st.code(compiled_prompt, language="markdown")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a valid active URL link address target endpoint above to proceed.")
