import streamlit as st
import requests
from bs4 import BeautifulSoup
import urllib.parse

# 1. Base UI Configuration Settings Layer
st.set_page_config(page_title="Universal Prompt Compiler", page_icon="🔄", layout="centered")

st.markdown("""
    <style>
    .brand-title { font-size: 28px; font-weight: 800; color: #1f2328; text-align: center; margin-top: 10px; }
    .tagline { text-align: center; font-size: 16px; color: #57606a; margin-bottom: 25px; }
    .prompt-container-box { background-color: #f6f8fa; border: 1px solid #d0d7de; border-radius: 6px; padding: 20px; margin-top: 25px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="brand-title">🔄 Universal Prompt Compiler</div>', unsafe_allow_html=True)
st.markdown('<div class="tagline">Turn any website or repository into a high-fidelity visual-creator AI prompt instantly.</div>', unsafe_allow_html=True)

# 2. User Input Field
url_bar_input = st.text_input(
    "Paste complete GitHub Repository, live Portfolio, or Web App address here:", 
    value="https://firebaseapp.com",
    placeholder="e.g., https://github.com or https://firebaseapp.com"
)

# 3. Dynamic Parser Logic Block
def extract_visual_design_tokens(url):
    cleaned = url.strip()
    if not cleaned.startswith(("http://", "https://")):
        cleaned = "https://" + cleaned
        
    try:
        parsed = urllib.parse.urlparse(cleaned)
        domain_name = parsed.netloc
        
        page_title = domain_name
        scraped_features = []
        
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
            res = requests.get(cleaned, headers=headers, timeout=5)
            soup = BeautifulSoup(res.text, "html.parser")
            
            if soup.title and soup.title.string:
                page_title = soup.title.string.strip()
            
            # COMPLETELY CLEAN FIELD HOOK (No quotes, no trailing tags)
            for heading in soup.find_all(["h1", "h2", "h3"])[:4]:
                h_text = heading.get_text().strip()
                if h_text and len(h_text) < 60:
                    if h_text not in scraped_features:
                        scraped_features.append(h_text)
        except:
            pass

        clean_title = page_title
        if "|" in clean_title:
            clean_title = clean_title.split("|")[0].strip()
        if "-" in clean_title:
            clean_title = clean_title.split("-")[0].strip()
            
        if clean_title == domain_name or not clean_title:
            clean_title = "Production Workspace App"

        # Theme Assignment Logic Variables
        if "firebase" in domain_name or "app" in domain_name:
            accent_color = "unmistakable Firebase Amber Orange"
            text_color = "deep charcoal gray text"
            layout_style = "a responsive, clean 3 column dashboard grid layout full of telemetry elements"
            fallback = ["Fast data synchronization pipelines", "Preview structural changes", "Automated deployment tracking"]
        elif "github.io" in domain_name or "portfolio" in domain_name:
            accent_color = "premium electric slate blue"
            text_color = "crisp dark ink obsidian text"
            layout_style = "a responsive, clean bento box asymmetric portfolio layout grid full of work highlights"
            fallback = ["Personal biography showcase", "Interactive skills capability matrix", "Clean contact messaging input form"]
        else:
            accent_color = "vibrant open source green"
            text_color = "light code focused gray text set against a dark steel theme"
            layout_style = "a crisp, structured multi pane file browser configuration grid"
            fallback = ["Dynamic directory file tree navigator", "Latest commits timeline log tracker", "Syntax highlighted documentation panel frames"]

        final_features = scraped_features if scraped_features else fallback
        while len(final_features) < 3:
            final_features.append("Dynamic interactive control workflows and sync modules loop")

        return {
            "project_name": clean_title,
            "accent": accent_color,
            "text": text_color,
            "grid_layout": layout_style,
            "features_list": final_features[:3]
        }
    except:
        return None

visual_tokens = extract_visual_design_tokens(url_bar_input)

# 4. Human-Style Prompt Compiler Rendering Output Block
if st.button("Get Prompt Blueprint", type="primary", use_container_width=True):
    if visual_tokens:
        with st.spinner("Processing design tokens..."):
            
            feats = visual_tokens["features_list"]
            
            # Compiled using plain text formatting lines to avoid string breaks
            line1 = f"Build me a {visual_tokens['project_name']} style web app homepage that feels bright, friendly, and very visual.\n"
            line2 = f"I want a clean white canvas, bold rounded sans serif type, {visual_tokens['text']}, and that {visual_tokens['accent']} for the main actions.\n"
            line3 = f"The page should feel simple and welcoming, with a header that includes the logo mark, navigation, a search bar, and clear Log in and Sign up buttons.\n\n"
            line4 = f"The main experience should be about visual discovery. Show {visual_tokens['grid_layout']} that feels full of inspiration, with layout sections built around:\n"
            line5 = f"- {feats[0]}\n- {feats[1]}\n- {feats[2]}\n\n"
            line6 = f"Add a big hero message like discovering ideas to try, and make the whole layout feel polished, approachable, and easy to browse.\n"
            line7 = f"Cards should have subtle borders, lots of white space, and minimal chrome so the content stands out. Make it responsive and smooth with hover states.\n\n"
            line8 = f"Reference Destination Source: {url_bar_input}"
            
            final_prompt = line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8
            
            st.markdown('<div class="prompt-container-box">', unsafe_allow_html=True)
            st.markdown("### 📋 Reconstructed Visual-Creator Prompt")
            st.caption("Copy this text and paste it into an AI tool like ChatGPT, Cursor, or Claude Code:")
            st.code(final_prompt, language="markdown")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a valid active URL link address target endpoint above to proceed.")
