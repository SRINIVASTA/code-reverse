document.getElementById('trigger-deconstruct-btn').addEventListener('click', runUniversalParserEngine);
document.getElementById('target-url-input').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') runUniversalParserEngine();
});

function runUniversalParserEngine() {
    const rawUrlString = document.getElementById('target-url-input').value.trim();
    if (!rawUrlString) return alert("Please clarify operational goal by writing a target URL address domain or codebase directory link.");

    fetch('/api/reverse', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: rawUrlString })
    })
    .then(res => res.json())
    .then(packet => {
        if (packet.success) {
            compileAndInfectSandboxCanvas(packet.data);
        } else {
            alert("Parser runtime exception: " + packet.message);
        }
    })
    .catch(err => console.error("Error pushing extraction call to backend pipeline stack:", err));
}

function compileAndInfectSandboxCanvas(tokens) {
    const canvas = document.getElementById('sandbox-viewport-canvas');
    const nav = document.getElementById('sandbox-nav-component');
    const nodesGrid = document.getElementById('sandbox-component-nodes-grid');
    
    // Inject extracted typography and surface base backgrounds dynamically
    canvas.style.backgroundColor = tokens.bg_color;
    canvas.style.color = tokens.text_color;
    canvas.style.fontFamily = tokens.font_family;
    
    // Update data labels
    document.getElementById('sandbox-nav-title-node').innerText = tokens.title;
    document.getElementById('sandbox-hero-header-text').innerText = tokens.hero_title;
    document.getElementById('sandbox-hero-sub-paragraph').innerText = tokens.hero_desc;
    
    // Select specific control points to skin with the token values
    const primaryBtn = nav.querySelector('.sbox-btn-primary');
    const secondaryBtn = nav.querySelector('.sbox-btn-secondary');
    const searchBar = nav.querySelector('.sandbox-search-bar-mock');
    const indicatorDot = nav.querySelector('.sandbox-indicator-dot');

    indicatorDot.style.color = tokens.accent_color;
    primaryBtn.style.backgroundColor = tokens.accent_color;
    primaryBtn.style.borderRadius = tokens.border_radius;
    secondaryBtn.style.borderRadius = tokens.border_radius;
    
    // Adapt text legibility colors on action buttons depending on layout brightness profiles
    const isDarkBg = (tokens.bg_color !== '#ffffff' && tokens.bg_color !== '#fafafa' && tokens.bg_color !== '#f8f9fa');
    primaryBtn.style.color = isDarkBg ? '#000000' : '#ffffff';
    
    if (isDarkBg) {
        secondaryBtn.style.backgroundColor = 'rgba(255, 255, 255, 0.08)';
        secondaryBtn.style.color = tokens.text_color;
        searchBar.style.backgroundColor = 'rgba(255, 255, 255, 0.05)';
        searchBar.style.color = 'rgba(255, 255, 255, 0.4)';
        searchBar.style.borderRadius = tokens.border_radius === '24px' ? '30px' : tokens.border_radius;
    } else {
        secondaryBtn.style.backgroundColor = 'rgba(0, 0, 0, 0.06)';
        secondaryBtn.style.color = tokens.text_color;
        searchBar.style.backgroundColor = 'rgba(0, 0, 0, 0.04)';
        searchBar.style.color = 'rgba(0, 0, 0, 0.5)';
        searchBar.style.borderRadius = tokens.border_radius === '24px' ? '30px' : tokens.border_radius;
    }

    // Refresh structural node cards block elements layout display view loop array
    nodesGrid.innerHTML = '';
    tokens.nodes.forEach(node => {
        const cardElement = document.createElement('div');
        cardElement.className = 'architecture-node-card';
        cardElement.style.borderRadius = tokens.border_radius;
        cardElement.style.backgroundColor = isDarkBg ? 'rgba(255, 255, 255, 0.03)' : '#ffffff';
        cardElement.style.borderColor = isDarkBg ? 'rgba(255, 255, 255, 0.08)' : 'rgba(0, 0, 0, 0.08)';
        
        // Dynamic nested micro layout components construction
        cardElement.innerHTML = `
            <span class="node-tag" style="background-color: ${tokens.accent_color}25; color: ${tokens.accent_color}">
                ${node.type}
            </span>
            <h3 style="color: ${tokens.text_color}">${node.label}</h3>
            <p style="color: ${tokens.text_color}; opacity: 0.7;">Discovered asset module running inside extracted runtime tree profiles context layout configurations.</p>
        `;
        nodesGrid.appendChild(cardElement);
    });
}
