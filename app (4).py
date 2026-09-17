import os
import re
import json
import urllib.request
from bs4 import BeautifulSoup
try:
    import streamlit as str_lit
except ImportError:
    str_lit = None

# -----------------------------------------------------------------------------
# Core Design System Extraction Rules
# -----------------------------------------------------------------------------
PREMIUM_MAPPINGS = {
    "pinterest.com": {
        "title": "Pinterest Design System",
        "bg_color": "#ffffff", "text_color": "#211922", "accent_color": "#e60023",
        "font_family": "Pin Sans, -apple-system, sans-serif", "border_radius": "24px",
        "hero_title": "Find your next idea to try",
        "hero_desc": "Clean, image-first consumer layout: bright, friendly, and highly approachable.",
        "nodes": [
            {"label": "Feed Container", "type": "Layout Grid"},
            {"label": "Discovery Pin Tile", "type": "Card Component"},
            {"label": "Pinterest Red CTA", "type": "Interactive Button"}
        ]
    },
    "github.com": {
        "title": "GitHub Primer Framework",
        "bg_color": "#0d1117", "text_color": "#e6edf3", "accent_color": "#1f6feb",
        "font_family": "-apple-system, BlinkMacSystemFont, sans-serif", "border_radius": "6px",
        "hero_title": "Let's build from here",
        "hero_desc": "High technical density: sharp container lines, deep backgrounds, and code structures.",
        "nodes": [
            {"label": "Repository File Tree", "type": "Data Structure"},
            {"label": "Commit Node Timeline", "type": "Version Track Component"},
            {"label": "Primer Navigation Bar", "type": "Shell Header"}
        ]
    }
}

def analyze_url(raw_url):
    """
    Universal Analyzer: Parses input URL, detects if it is a GitHub repository
    or a standard site, and dynamically reverse-engineers its core design blueprint tokens.
    """
    clean_url = raw_url.replace('https://', '').replace('http://', '').replace('www.', '').strip()
    
    # 1. Look for Exact Hardcoded Matching Profile Accuracies First
    for key, data in PREMIUM_MAPPINGS.items():
        if clean_url.startswith(key):
            return data

    # 2. Dynamic Router Case A: Target URL points to a GitHub Repository Core Tree
    if "github.com/" in raw_url or clean_url.startswith("github.com"):
        try:
            parts = [p for p in clean_url.replace("github.com/", "").split('/') if p]
            if len(parts) >= 2:
                owner, repo = parts[0], parts[1]
                api_url = f"https://api.github.com/repos/{owner}/{repo}"
                req = urllib.request.Request(api_url, headers={'User-Agent': 'GitReverse-Parser'})
                with urllib.request.urlopen(req, timeout=4) as response:
                    repo_info = json.loads(response.read().decode('utf-8'))
                
                lang = repo_info.get('language', 'JavaScript')
                desc = repo_info.get('description', 'Dynamic version control tree structure.')
                
                lang_themes = {
                    "Python": {"accent": "#3572A5", "bg": "#0f172a", "radius": "4px"},
                    "JavaScript": {"accent": "#f1e05a", "bg": "#1c1917", "radius": "8px"},
                    "TypeScript": {"accent": "#3178c6", "bg": "#0f172a", "radius": "6px"},
                    "HTML": {"accent": "#e34c26", "bg": "#ffffff", "radius": "0px"}
                }
                theme = lang_themes.get(lang, {"accent": "#2ea44f", "bg": "#0d1117", "radius": "6px"})
                
                return {
                    "title": f"Repo Space: {repo}",
                    "bg_color": theme["bg"],
                    "text_color": "#ffffff" if theme["bg"] != "#ffffff" else "#111827",
                    "accent_color": theme["accent"],
                    "font_family": "SFMono-Regular, Consolas, monospace",
                    "border_radius": theme["radius"],
                    "hero_title": f"Deconstructing /{repo}",
                    "hero_desc": f"Primary Ecosystem: {lang}. Repository Overview: {desc}",
                    "nodes": [
                        {"label": f"{lang} Dependency Core", "type": "Package Manifest File"},
                        {"label": "Source Control Layout Tree", "type": "Repository Hierarchy Module"}
                    ]
                }
        except Exception:
            pass

    # 3. Dynamic Router Case B: Target URL is a general public website destination
    try:
        target = raw_url if raw_url.startswith(('http://', 'https://')) else f"https://{raw_url}"
        req = urllib.request.Request(target, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=4) as response:
            html = response.read()
        
        soup = BeautifulSoup(html, 'html.parser')
        title_str = soup.title.string.strip() if soup.title else clean_url.split('/')[0]
        title_clean = re.split(r'[-|]', title_str)[0].strip()
        
        raw_html_str = str(html)
        hex_tokens = re.findall(r'#[a-fA-F0-9]{6}', raw_html_str)
        filtered_colors = [c.lower() for c in hex_tokens if c.lower() not in ['#ffffff', '#000000', '#111827']]
        
        accent = filtered_colors[0] if filtered_colors else "#6366f1"
        is_dark = "dark" in raw_html_str.lower() or "#000" in raw_html_str
        
        return {
            "title": f"{title_clean} Analytics Shell",
            "bg_color": "#0f172a" if is_dark else "#ffffff",
            "text_color": "#f8fafc" if is_dark else "#0f172a",
            "accent_color": accent,
            "font_family": "system-ui, -apple-system, sans-serif",
            "border_radius": "12px",
            "hero_title": title_clean,
            "hero_desc": f"Automated structural parser crawl completed successfully for public web node cluster: {clean_url}",
            "nodes": [
                {"label": "Global Branding Navbar Header", "type": "Navigation Layer"},
                {"label": "Identified Card Container Blocks", "type": "Layout Component"}
            ]
        }
    except Exception:
        # Secure Base Fallback Configuration Profile Rules
        return {
            "title": "Fallback Frame Context",
            "bg_color": "#ffffff", "text_color": "#1e293b", "accent_color": "#2563eb",
            "font_family": "sans-serif", "border_radius": "8px",
            "hero_title": "Default Parsing Space",
            "hero_desc": f"Web token extraction processing failed or timed out for link address {clean_url}.",
            "nodes": [{"label": "Base Component Box", "type": "Fallback Element Placeholder"}]
        }

# -----------------------------------------------------------------------------
# Flask Web Deployment Application Engine Mode
# -----------------------------------------------------------------------------
try:
    from flask import Flask, render_template, request, jsonify
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/api/reverse', methods=['POST'])
    def api_reverse():
        req_data = request.json or {}
        url_input = req_data.get('url', '').strip()
        if not url_input:
            return jsonify({"success": False, "message": "Null address parameter input string."}), 400
        extracted_blueprint = analyze_url(url_input)
        return jsonify({"success": True, "data": extracted_blueprint})
except Exception:
    app = None

# -----------------------------------------------------------------------------
# Streamlit Web Deployment Application Engine Mode
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    # Flask executable layer path gateway run trigger
    if app:
        import sys
        if len(sys.argv) > 1 and sys.argv[1] == '--streamlit':
            pass
        else:
            print("Starting GitReverse Web Architecture Engine on http://127.0.0.1:5000")
            app.run(debug=True, port=5000)
