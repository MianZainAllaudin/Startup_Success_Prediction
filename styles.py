GLOBAL_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

    :root {
        --bg-deep:       #080c14;
        --bg-card:       rgba(255,255,255,0.04);
        --bg-card-hover: rgba(255,255,255,0.07);
        --border:        rgba(255,255,255,0.08);
        --border-glow:   rgba(99,179,237,0.35);
        --accent-blue:   #63b3ed;
        --accent-teal:   #4fd1c5;
        --accent-amber:  #f6ad55;
        --accent-green:  #68d391;
        --accent-red:    #fc8181;
        --text-primary:  #f0f4f8;
        --text-secondary:#a0aec0;
        --text-muted:    #4a5568;
        --font-display:  'Syne', sans-serif;
        --font-body:     'DM Sans', sans-serif;
        --radius-lg:     16px;
        --radius-md:     10px;
        --radius-sm:     6px;
    }

    html, body, [class*="css"] {
        font-family: var(--font-body) !important;
        background-color: var(--bg-deep) !important;
        color: var(--text-primary) !important;
    }
    .stApp { background: var(--bg-deep) !important; }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d1117 0%, #080c14 100%) !important;
        border-right: 1px solid var(--border) !important;
    }
    [data-testid="stSidebar"] > div { padding: 2rem 1.25rem; }

    .sidebar-logo {
        display: flex; align-items: center; gap: 10px;
        margin-bottom: 2rem; padding-bottom: 1.5rem;
        border-bottom: 1px solid var(--border);
    }
    .sidebar-logo-icon {
        width:36px;height:36px;
        background:linear-gradient(135deg,#63b3ed,#4fd1c5);
        border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;
    }
    .sidebar-logo-text {
        font-family:var(--font-display)!important;font-size:1.25rem;font-weight:800;
        color:var(--text-primary)!important;letter-spacing:-0.02em;
    }
    .sidebar-logo-badge {
        font-size:0.6rem;background:linear-gradient(135deg,#63b3ed22,#4fd1c522);
        border:1px solid var(--border-glow);color:var(--accent-teal);
        padding:2px 7px;border-radius:20px;letter-spacing:0.08em;
        text-transform:uppercase;font-weight:600;margin-top:1px;
    }
    .sidebar-section-label {
        font-size:0.65rem;font-weight:700;letter-spacing:0.15em;text-transform:uppercase;
        color:var(--text-muted);margin:1.5rem 0 0.75rem;
    }
    .model-status {
        display:flex;align-items:center;gap:8px;
        background:rgba(104,211,145,0.08);border:1px solid rgba(104,211,145,0.25);
        border-radius:var(--radius-md);padding:0.6rem 0.9rem;margin-bottom:1.25rem;
    }
    .model-status-dot {
        width:7px;height:7px;border-radius:50%;background:var(--accent-green);
        box-shadow:0 0 8px var(--accent-green);animation:pulse 2s ease-in-out infinite;flex-shrink:0;
    }
    @keyframes pulse { 0%,100%{opacity:1}50%{opacity:0.4} }
    .model-status-label { font-size:0.78rem;color:var(--accent-green);font-weight:500; }
    .metric-chip {
        display:flex;justify-content:space-between;align-items:center;
        padding:0.5rem 0.75rem;background:var(--bg-card);
        border:1px solid var(--border);border-radius:var(--radius-sm);margin-bottom:0.4rem;
    }
    .metric-chip-label{font-size:0.75rem;color:var(--text-secondary);}
    .metric-chip-value{font-size:0.8rem;color:var(--accent-blue);font-weight:600;}
    .factor-tag {
        display:inline-flex;align-items:center;gap:5px;
        background:rgba(99,179,237,0.07);border:1px solid rgba(99,179,237,0.2);
        border-radius:20px;padding:3px 10px;font-size:0.7rem;
        color:var(--accent-blue);margin:2px;font-weight:500;
    }

    /* ── Section headers ── */
    .section-header {
        display:flex;align-items:center;gap:10px;margin-bottom:1.25rem;
        padding-bottom:0.75rem;border-bottom:1px solid var(--border);
    }
    .section-icon {
        width:30px;height:30px;border-radius:var(--radius-sm);
        display:flex;align-items:center;justify-content:center;font-size:0.9rem;
    }
    .icon-blue  {background:rgba(99,179,237,0.15);}
    .icon-teal  {background:rgba(79,209,197,0.15);}
    .icon-amber {background:rgba(246,173,85,0.15);}
    .section-title {
        font-family:var(--font-display)!important;font-size:0.85rem;font-weight:700;
        color:var(--text-primary);letter-spacing:0.02em;text-transform:uppercase;
    }

    /* ── Glass card ── */
    .glass-card {
        background:var(--bg-card);border:1px solid var(--border);
        border-radius:var(--radius-lg);padding:1.5rem;backdrop-filter:blur(20px);
        transition:border-color 0.2s,background 0.2s;height:100%;
    }
    .glass-card:hover{background:var(--bg-card-hover);border-color:rgba(99,179,237,0.18);}

    /* ── Inputs – fix white-box text visibility ── */
    .stNumberInput input,
    .stTextInput input {
        background: rgba(13,17,23,0.95) !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        border-radius: var(--radius-sm) !important;
        color: #f0f4f8 !important;
        font-family: var(--font-body) !important;
        font-size: 0.9rem !important;
        padding: 0.45rem 0.75rem !important;
        caret-color: var(--accent-blue) !important;
    }
    .stNumberInput > div > div > input,
    .stTextInput > div > div > input {
        background-color: rgba(13,17,23,0.95) !important;
        color: #f0f4f8 !important;
    }
    .stNumberInput input::placeholder,
    .stTextInput input::placeholder { color: #a0aec0 !important; }
    .stNumberInput input:focus,
    .stTextInput input:focus {
        border-color: var(--accent-blue) !important;
        box-shadow: 0 0 0 2px rgba(99,179,237,0.15) !important;
        outline: none !important;
    }

    /* stepper +/- buttons */
    .stNumberInput button {
        background: rgba(255,255,255,0.06) !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        color: var(--text-primary) !important;
        border-radius: var(--radius-sm) !important;
    }

    /* Labels */
    .stNumberInput label, .stSlider label, .stCheckbox label,
    .stSelectbox label, .stTextInput label {
        font-family:var(--font-body)!important;font-size:0.78rem!important;
        font-weight:500!important;color:var(--text-secondary)!important;
        text-transform:uppercase;letter-spacing:0.07em;margin-bottom:2px!important;
    }

    /* Selectbox */
    .stSelectbox > div > div {
        background: rgba(255,255,255,0.06) !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        border-radius: var(--radius-sm) !important;
        color: #f0f4f8 !important;
    }
    .stSelectbox > div > div:focus-within {
        border-color:var(--accent-blue)!important;
        box-shadow:0 0 0 2px rgba(99,179,237,0.15)!important;
    }

    /* Slider */
    .stSlider [data-baseweb="slider"] div[role="slider"] {
        background:var(--accent-blue)!important;
        border:2px solid var(--bg-deep)!important;
        box-shadow:0 0 12px rgba(99,179,237,0.4)!important;
    }

    /* Checkbox */
    .stCheckbox {
        background:rgba(255,255,255,0.02);border:1px solid var(--border);
        border-radius:var(--radius-sm);padding:0.55rem 0.75rem!important;
        margin-bottom:0.35rem!important;transition:border-color 0.15s,background 0.15s;
    }
    .stCheckbox:hover{border-color:rgba(99,179,237,0.2);background:rgba(99,179,237,0.04);}
    .stCheckbox label {
        font-size:0.82rem!important;color:var(--text-secondary)!important;
        text-transform:none!important;letter-spacing:0!important;font-weight:400!important;
    }

    /* ── Primary Button ── */
    .stButton > button {
        width:100%;padding:0.85rem 2rem!important;
        background:linear-gradient(135deg,#2b6cb0,#2c7a7b)!important;
        border:1px solid rgba(99,179,237,0.3)!important;
        border-radius:var(--radius-md)!important;color:white!important;
        font-family:var(--font-display)!important;font-size:0.9rem!important;
        font-weight:700!important;letter-spacing:0.05em!important;
        text-transform:uppercase!important;cursor:pointer!important;
        transition:all 0.2s!important;
        box-shadow:0 4px 24px rgba(43,108,176,0.3)!important;
    }
    .stButton > button:hover {
        background:linear-gradient(135deg,#3182ce,#319795)!important;
        border-color:rgba(99,179,237,0.5)!important;
        box-shadow:0 6px 32px rgba(43,108,176,0.45)!important;
        transform:translateY(-1px)!important;
    }
    .stButton > button:active { transform:translateY(0)!important; }

    hr { border:none!important;border-top:1px solid var(--border)!important;margin:2rem 0!important; }

    /* ── Result / Confidence cards ── */
    .result-acquired {
        background:linear-gradient(135deg,rgba(56,161,105,0.12),rgba(72,187,120,0.06));
        border:1px solid rgba(104,211,145,0.3);border-radius:var(--radius-lg);
        padding:2rem;text-align:center;position:relative;overflow:hidden;
    }
    .result-closed {
        background:linear-gradient(135deg,rgba(197,48,48,0.12),rgba(229,62,62,0.06));
        border:1px solid rgba(252,129,129,0.3);border-radius:var(--radius-lg);
        padding:2rem;text-align:center;position:relative;overflow:hidden;
    }
    .result-emoji{font-size:2.5rem;margin-bottom:0.5rem;}
    .result-label{font-family:var(--font-display)!important;font-size:1.8rem;font-weight:800;letter-spacing:-0.02em;margin-bottom:0.5rem;}
    .result-label-acquired{color:var(--accent-green);}
    .result-label-closed  {color:var(--accent-red);}
    .result-desc{font-size:0.85rem;color:var(--text-secondary);line-height:1.5;}

    .confidence-card {
        background:var(--bg-card);border:1px solid var(--border);
        border-radius:var(--radius-lg);padding:1.5rem;text-align:center;
    }
    .confidence-pct {
        font-family:var(--font-display)!important;font-size:2.5rem;font-weight:800;
        color:var(--accent-blue);letter-spacing:-0.03em;line-height:1;
    }
    .confidence-bar-track{height:4px;background:var(--border);border-radius:2px;margin-top:1rem;overflow:hidden;}
    .confidence-bar-fill{height:100%;border-radius:2px;background:linear-gradient(90deg,#63b3ed,#4fd1c5);}
    .kpi-card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-md);padding:1rem 1.25rem;text-align:center;}
    .kpi-value{font-family:var(--font-display)!important;font-size:1.3rem;font-weight:700;color:var(--text-primary);letter-spacing:-0.02em;}
    .kpi-label{font-size:0.68rem;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.1em;margin-top:3px;}

    .divider-label {
        display:flex;align-items:center;gap:12px;margin:2.5rem 0 1.75rem;
        color:var(--text-muted);font-size:0.68rem;text-transform:uppercase;
        letter-spacing:0.14em;font-weight:600;
    }
    .divider-label::before,.divider-label::after{content:'';flex:1;height:1px;background:var(--border);}

    /* ── Modal / Popup overlay ── */
    .modal-overlay {
        position:fixed;inset:0;background:rgba(8,12,20,0.88);
        backdrop-filter:blur(10px);z-index:9999;
        display:flex;align-items:center;justify-content:center;
        animation:fadeIn 0.25s ease;
    }
    @keyframes fadeIn{from{opacity:0}to{opacity:1}}
    .modal-box {
        background:#0d1117;border:1px solid rgba(255,255,255,0.1);
        border-radius:20px;padding:2.5rem;max-width:560px;width:92%;
        position:relative;box-shadow:0 30px 80px rgba(0,0,0,0.6);
        animation:slideUp 0.3s cubic-bezier(.22,.68,0,1.2);
    }
    @keyframes slideUp{from{opacity:0;transform:translateY(28px)}to{opacity:1;transform:translateY(0)}}
    .modal-close {
        position:absolute;top:1.1rem;right:1.1rem;
        background:rgba(255,255,255,0.06);border:1px solid var(--border);
        border-radius:50%;width:32px;height:32px;
        display:flex;align-items:center;justify-content:center;
        cursor:pointer;font-size:0.85rem;color:var(--text-muted);
        transition:background 0.15s,color 0.15s;
    }
    .modal-close:hover{background:rgba(252,129,129,0.15);color:var(--accent-red);}

    /* ── Footer ── */
    .app-footer {
        text-align:center;padding:2.5rem 0 1rem;border-top:1px solid var(--border);
        margin-top:3rem;color:var(--text-muted);font-size:0.75rem;letter-spacing:0.04em;
    }
    .footer-brand{font-family:var(--font-display)!important;font-weight:700;color:var(--text-secondary);letter-spacing:-0.01em;}

    /* ── Hide Streamlit chrome ── */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    [data-testid="stDecoration"] { display: none !important; }
    [data-testid="stHeader"] { background: transparent !important; border-bottom: none !important; }
    .stDeployButton { display: none !important; }
    [data-testid="stAppDeployButton"] { display: none !important; }

    /* ── Sidebar toggle buttons (Streamlit 1.57) ── */
    [data-testid="stExpandSidebarButton"] {
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        pointer-events: auto !important;
    }
    [data-testid="stExpandSidebarButton"] button {
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        background: rgba(99,179,237,0.12) !important;
        border: 1px solid rgba(99,179,237,0.25) !important;
        color: #63b3ed !important;
        border-radius: 8px !important;
    }
    [data-testid="stSidebarCollapseButton"] {
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
    }
    [data-testid="stSidebarCollapseButton"] button {
        display: flex !important;
        visibility: visible !important;
        color: var(--text-secondary) !important;
    }

    .stSpinner>div{border-color:var(--accent-blue) transparent transparent!important;}
    .stAlert{background:rgba(255,255,255,0.03)!important;border:1px solid var(--border)!important;border-radius:var(--radius-md)!important;color:var(--text-secondary)!important;}
    ::-webkit-scrollbar{width:6px;}
    ::-webkit-scrollbar-track{background:var(--bg-deep);}
    ::-webkit-scrollbar-thumb{background:#2d3748;border-radius:3px;}
    ::-webkit-scrollbar-thumb:hover{background:#4a5568;}
</style>
"""

WELCOME_CSS = """
<style>
/* ── Welcome page specific ── */
.welcome-root {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 4rem 2rem;
    position: relative;
    overflow: hidden;
}

/* Ambient glows */
.welcome-root::before {
    content: '';
    position: fixed;
    top: -20%;
    left: 50%;
    transform: translateX(-50%);
    width: 800px;
    height: 500px;
    background: radial-gradient(ellipse at center top,
        rgba(99,179,237,0.09) 0%,
        rgba(79,209,197,0.05) 40%,
        transparent 70%);
    pointer-events: none;
    z-index: 0;
}
.welcome-root::after {
    content: '';
    position: fixed;
    bottom: -10%;
    right: -10%;
    width: 500px;
    height: 500px;
    background: radial-gradient(circle, rgba(79,209,197,0.06) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
}

.welcome-inner {
    position: relative;
    z-index: 1;
    max-width: 900px;
    width: 100%;
    text-align: center;
}

/* Animated orbit ring */
.orbit-container {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    position: relative;
    margin-bottom: 2.5rem;
}
.orbit-ring {
    width: 100px; height: 100px;
    border-radius: 50%;
    border: 1px solid rgba(99,179,237,0.2);
    position: relative;
    animation: spin 8s linear infinite;
}
.orbit-ring::before {
    content: '';
    position: absolute;
    top: -3px; left: 50%; transform: translateX(-50%);
    width: 6px; height: 6px;
    background: var(--accent-blue);
    border-radius: 50%;
    box-shadow: 0 0 12px var(--accent-blue);
}
@keyframes spin { from{transform:rotate(0deg)} to{transform:rotate(360deg)} }

.orbit-core {
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    font-size: 2.2rem;
    animation: none;
}

/* Eyebrow pill */
.welcome-eyebrow {
    display: inline-flex; align-items: center; gap: 8px;
    background: rgba(99,179,237,0.08);
    border: 1px solid rgba(99,179,237,0.25);
    border-radius: 40px;
    padding: 6px 16px;
    font-size: 0.68rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--accent-blue);
    font-weight: 700;
    margin-bottom: 1.5rem;
}
.eyebrow-dot {
    width: 5px; height: 5px; border-radius: 50%;
    background: var(--accent-teal);
    box-shadow: 0 0 6px var(--accent-teal);
    animation: pulse 2s ease-in-out infinite;
}

/* Hero title */
.welcome-title {
    font-family: var(--font-display) !important;
    font-size: clamp(3rem, 7vw, 5.5rem);
    font-weight: 800;
    letter-spacing: -0.04em;
    line-height: 1;
    background: linear-gradient(135deg, #f0f4f8 20%, #63b3ed 55%, #4fd1c5 80%, #68d391 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0 0 1rem;
}
.welcome-tagline {
    font-size: clamp(1rem, 2vw, 1.2rem);
    color: var(--text-secondary);
    font-weight: 300;
    line-height: 1.6;
    max-width: 540px;
    margin: 0 auto 3rem;
    letter-spacing: 0.01em;
}

/* Stats grid */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    max-width: 700px;
    margin: 0 auto 3.5rem;
}
.stat-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 1.25rem 1rem;
    transition: border-color 0.2s, background 0.2s;
}
.stat-card:hover {
    background: rgba(99,179,237,0.05);
    border-color: rgba(99,179,237,0.2);
}
.stat-num {
    font-family: var(--font-display) !important;
    font-size: 1.6rem;
    font-weight: 800;
    letter-spacing: -0.03em;
    color: var(--text-primary);
    line-height: 1;
    margin-bottom: 4px;
}
.stat-lbl {
    font-size: 0.65rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-weight: 600;
}

/* Feature cards */
.feature-strip {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.75rem;
    max-width: 800px;
    margin: 0 auto 3.5rem;
}
.feature-card {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 14px;
    padding: 1.5rem 1.25rem;
    text-align: left;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s, background 0.2s;
}
.feature-card:hover {
    background: rgba(255,255,255,0.04);
    border-color: rgba(99,179,237,0.2);
}
.feature-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(99,179,237,0.3), transparent);
}
.feature-icon {
    font-size: 1.4rem;
    margin-bottom: 0.75rem;
    display: block;
}
.feature-title {
    font-family: var(--font-display) !important;
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 0.4rem;
    letter-spacing: 0.01em;
}
.feature-desc {
    font-size: 0.75rem;
    color: var(--text-muted);
    line-height: 1.5;
}

/* CTA button wrapper */
.cta-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.75rem;
}
.cta-hint {
    font-size: 0.7rem;
    color: var(--text-muted);
    letter-spacing: 0.08em;
}

/* Animated gradient border on CTA */
.cta-btn-wrapper {
    position: relative;
    display: inline-block;
    border-radius: 12px;
    padding: 1px;
    background: linear-gradient(135deg, #63b3ed, #4fd1c5, #68d391, #63b3ed);
    background-size: 300% 300%;
    animation: gradientShift 4s ease infinite;
}
@keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.cta-btn-inner {
    background: #0d1117;
    border-radius: 11px;
    padding: 0;
}

/* Tech badge bar */
.tech-bar {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1.5rem;
    margin-top: 4rem;
    padding-top: 2rem;
    border-top: 1px solid var(--border);
}
.tech-item {
    display: flex; align-items: center; gap: 6px;
    font-size: 0.68rem;
    color: var(--text-muted);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    font-weight: 600;
}
.tech-dot {
    width: 4px; height: 4px;
    border-radius: 50%;
    background: var(--accent-teal);
}
</style>
"""