import streamlit as st
import streamlit.components.v1 as components


def render_welcome():
    components.html("""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@300;400;500&display=swap');
        * { margin:0; padding:0; box-sizing:border-box; }
        body { background: transparent; font-family: 'DM Sans', sans-serif; color: #f0f4f8; }

        .root {
            display: flex; flex-direction: column; align-items: center;
            padding: 2rem 2rem 1rem; position: relative; overflow: hidden;
        }
        .glow-top {
            position: absolute; top: -80px; left: 50%; transform: translateX(-50%);
            width: 700px; height: 400px;
            background: radial-gradient(ellipse at center top, rgba(99,179,237,0.11) 0%, rgba(79,209,197,0.06) 40%, transparent 70%);
            pointer-events: none;
        }
        .glow-br {
            position: absolute; bottom: -60px; right: -60px;
            width: 400px; height: 400px;
            background: radial-gradient(circle, rgba(79,209,197,0.07) 0%, transparent 70%);
            pointer-events: none;
        }

        .orbit-wrap { position: relative; width: 110px; height: 110px; margin-bottom: 2rem; }
        .orbit-ring {
            width: 110px; height: 110px; border-radius: 50%;
            border: 1px solid rgba(99,179,237,0.25);
            position: absolute; top:0; left:0;
            animation: spin 9s linear infinite;
        }
        .orbit-ring::before {
            content: ''; position: absolute;
            top: -4px; left: 50%; transform: translateX(-50%);
            width: 8px; height: 8px;
            background: #63b3ed; border-radius: 50%;
            box-shadow: 0 0 14px #63b3ed;
        }
        .orbit-core {
            position: absolute; top: 50%; left: 50%;
            transform: translate(-50%, -50%); font-size: 2.4rem;
        }
        @keyframes spin { to { transform: rotate(360deg); } }

        .eyebrow {
            display: inline-flex; align-items: center; gap: 8px;
            background: rgba(99,179,237,0.09); border: 1px solid rgba(99,179,237,0.28);
            border-radius: 40px; padding: 6px 18px;
            font-size: 0.65rem; letter-spacing: 0.16em; text-transform: uppercase;
            color: #63b3ed; font-weight: 700; margin-bottom: 1.4rem;
        }
        .e-dot {
            width: 5px; height: 5px; border-radius: 50%;
            background: #4fd1c5; box-shadow: 0 0 6px #4fd1c5;
            animation: pulse 2s ease-in-out infinite;
        }
        @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.35} }

        .title {
            font-family: 'Syne', sans-serif;
            font-size: clamp(2.8rem, 6vw, 5rem); font-weight: 800;
            letter-spacing: -0.04em; line-height: 1;
            background: linear-gradient(135deg, #f0f4f8 20%, #63b3ed 55%, #4fd1c5 80%, #68d391 100%);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            background-clip: text; margin-bottom: 1rem; text-align: center;
        }
        .tagline {
            font-size: 1rem; color: #a0aec0; font-weight: 300; line-height: 1.65;
            max-width: 500px; margin: 0 auto 2.8rem; text-align: center;
        }

        .stats {
            display: grid; grid-template-columns: repeat(3, 1fr);
            gap: 0.85rem; max-width: 480px; width: 100%; margin-bottom: 2.5rem;
        }
        .stat {
            background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07);
            border-radius: 12px; padding: 1.1rem 0.75rem; text-align: center;
            transition: border-color 0.2s, background 0.2s;
        }
        .stat:hover { background: rgba(99,179,237,0.06); border-color: rgba(99,179,237,0.22); }
        .stat-num {
            font-family: 'Syne', sans-serif; font-size: 1.55rem; font-weight: 800;
            letter-spacing: -0.03em; color: #f0f4f8; line-height: 1; margin-bottom: 4px;
        }
        .stat-lbl { font-size: 0.62rem; color: #a0aec0; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 600; }
        .features {
            display: grid; grid-template-columns: repeat(3, 1fr);
            gap: 0.75rem; max-width: 780px; width: 100%; margin-bottom: 2.5rem;
        }
        .feat {
            background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06);
            border-radius: 14px; padding: 1.4rem 1.15rem; text-align: left;
            position: relative; overflow: hidden; transition: border-color 0.2s, background 0.2s;
        }
        .feat:hover { background: rgba(255,255,255,0.04); border-color: rgba(99,179,237,0.22); }
        .feat::before {
            content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
            background: linear-gradient(90deg, transparent, rgba(99,179,237,0.35), transparent);
        }
        .feat-icon { font-size: 1.4rem; margin-bottom: 0.7rem; display: block; }
        .feat-title { font-family: 'Syne', sans-serif; font-size: 0.82rem; font-weight: 700; color: #f0f4f8; margin-bottom: 0.35rem; }
        .feat-desc { font-size: 0.73rem; color: #a0aec0; line-height: 1.55; }
        .tech-bar {
            display: flex; align-items: center; justify-content: center; gap: 1.5rem;
            padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.07);
            max-width: 680px; width: 100%;
        }
        .tech-item { display: flex; align-items: center; gap: 6px; font-size: 0.65rem; color: #a0aec0; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600; }
        .tech-dot { width: 4px; height: 4px; border-radius: 50%; background: #4fd1c5; }
    </style>
    </head>
    <body>
    <div class="root">
        <div class="glow-top"></div>
        <div class="glow-br"></div>

        <div class="orbit-wrap">
            <div class="orbit-ring"></div>
            <div class="orbit-core">🚀</div>
        </div>

        <div class="eyebrow">
            <span class="e-dot"></span>
            AI-Powered Startup Intelligence
            <span class="e-dot"></span>
        </div>

        <div class="title">LaunchLyft</div>

        <div class="tagline">
            Predict acquisition outcomes before they happen.<br>
            Enter your startup's profile, our Gradient Boosting engine
            returns an instant, data-backed verdict.
        </div>

        <div class="stats">
            <div class="stat"><div class="stat-num">40+</div><div class="stat-lbl">Features</div></div>
            <div class="stat"><div class="stat-num">GBM</div><div class="stat-lbl">Algorithm</div></div>
            <div class="stat"><div class="stat-num">CB</div><div class="stat-lbl">Dataset</div></div>
        </div>

        <div class="features">
            <div class="feat">
                <span class="feat-icon">💰</span>
                <div class="feat-title">Funding Analysis</div>
                <div class="feat-desc">Rounds, amounts, investor count, VC &amp; Angel signals — all weighted.</div>
            </div>
            <div class="feat">
                <span class="feat-icon">📈</span>
                <div class="feat-title">Growth Timeline</div>
                <div class="feat-desc">First-to-last funding velocity, founding age, and traction milestones.</div>
            </div>
            <div class="feat">
                <span class="feat-icon">🌐</span>
                <div class="feat-title">Market Context</div>
                <div class="feat-desc">Category, geography, and network relationships shape every prediction.</div>
            </div>
        </div>

        <div class="tech-bar">
            <span class="tech-item"><span class="tech-dot"></span>Scikit-learn</span>
            <span class="tech-item"><span class="tech-dot"></span>Gradient Boosting</span>
            <span class="tech-item"><span class="tech-dot"></span>Crunchbase Data</span>
            <span class="tech-item"><span class="tech-dot"></span>Binary Classification</span>
        </div>
    </div>
    </body>
    </html>
    """, height=780, scrolling=False)

    col1, col2, col3 = st.columns([1.5, 1, 1.5])
    with col2:
        if st.button("Launch Predictor", type="primary", use_container_width=True):
            st.session_state.page = "predictor"
            st.rerun()