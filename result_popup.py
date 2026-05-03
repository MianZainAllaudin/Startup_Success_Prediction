import streamlit as st
import streamlit.components.v1 as components


def render_result_popup(pred: int, confidence: float, funding_total_usd: float, funding_rounds: int):
    conf_pct   = f"{confidence * 100:.1f}%" if confidence is not None else "N/A"
    bar_width  = f"{confidence * 100:.0f}%" if confidence is not None else "0%"
    raised_str = f"${funding_total_usd/1_000_000:.1f}M"

    if pred == 1:
        verdict_bg     = "linear-gradient(135deg,rgba(56,161,105,0.14),rgba(72,187,120,0.06))"
        verdict_border = "rgba(104,211,145,0.35)"
        emoji          = "🎯"
        label          = "ACQUIRED"
        label_color    = "#68d391"
        desc           = "Strong acquisition signals detected. This startup profile aligns with successful exit patterns."
        bar_color      = "linear-gradient(90deg,#68d391,#4fd1c5)"
        conf_color     = "#68d391"
    else:
        verdict_bg     = "linear-gradient(135deg,rgba(197,48,48,0.14),rgba(229,62,62,0.06))"
        verdict_border = "rgba(252,129,129,0.35)"
        emoji          = "⚠️"
        label          = "CLOSED"
        label_color    = "#fc8181"
        desc           = "Risk factors identified. This startup may face significant closure challenges ahead."
        bar_color      = "linear-gradient(90deg,#fc8181,#f6ad55)"
        conf_color     = "#fc8181"

    components.html(f"""
    <!DOCTYPE html><html><head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@300;400;500&display=swap');
        * {{ margin:0; padding:0; box-sizing:border-box; }}
        body {{ background: transparent; font-family: 'DM Sans', sans-serif; color: #f0f4f8; }}

        .overlay {{
            position: fixed; inset: 0;
            background: rgba(8,12,20,0.85);
            backdrop-filter: blur(12px);
            display: flex; align-items: center; justify-content: center;
            z-index: 9999;
            animation: fadeIn 0.25s ease;
        }}
        @keyframes fadeIn {{ from{{opacity:0}} to{{opacity:1}} }}

        .box {{
            background: #0d1117;
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 20px;
            padding: 2.2rem;
            max-width: 520px; width: 92%;
            position: relative;
            box-shadow: 0 30px 80px rgba(0,0,0,0.65);
            animation: slideUp 0.3s cubic-bezier(.22,.68,0,1.2);
        }}
        @keyframes slideUp {{ from{{opacity:0;transform:translateY(28px)}} to{{opacity:1;transform:translateY(0)}} }}

        .close-btn {{
            position: absolute; top: 1rem; right: 1rem;
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 50%; width: 32px; height: 32px;
            display: flex; align-items: center; justify-content: center;
            cursor: pointer; font-size: 0.85rem; color: #a0aec0;
            transition: background 0.15s, color 0.15s;
        }}
        .close-btn:hover {{ background: rgba(252,129,129,0.15); color: #fc8181; }}

        .verdict {{
            background: {verdict_bg};
            border: 1px solid {verdict_border};
            border-radius: 14px; padding: 1.75rem; text-align: center;
            margin-bottom: 1.1rem;
        }}
        .v-emoji {{ font-size: 2.2rem; margin-bottom: 0.4rem; }}
        .v-label {{
            font-family: 'Syne', sans-serif; font-size: 1.8rem; font-weight: 800;
            letter-spacing: -0.02em; color: {label_color}; margin-bottom: 0.4rem;
        }}
        .v-desc {{ font-size: 0.82rem; color: #a0aec0; line-height: 1.5; }}

        .metrics {{
            display: grid; grid-template-columns: 1fr 1fr 1fr;
            gap: 0.7rem; margin-bottom: 1rem;
        }}
        .metric {{
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.07);
            border-radius: 12px; padding: 1rem 0.75rem; text-align: center;
        }}
        .m-lbl {{
            font-size: 0.58rem; text-transform: uppercase;
            letter-spacing: 0.12em; color: #a0aec0; margin-bottom: 0.4rem;
        }}
        .m-val {{
            font-family: 'Syne', sans-serif; font-size: 1.5rem; font-weight: 800;
            color: #f0f4f8; letter-spacing: -0.02em;
        }}
        .m-val.conf {{ color: {conf_color}; }}

        .bar-track {{ height: 3px; background: rgba(255,255,255,0.07); border-radius: 2px; margin-top: 0.5rem; overflow: hidden; }}
        .bar-fill {{ height: 100%; width: {bar_width}; border-radius: 2px; background: {bar_color}; }}

        .hint {{ text-align: center; margin-top: 0.9rem; font-size: 0.65rem; color: #718096; letter-spacing: 0.06em; }}
    </style>
    </head><body>
    <div class="overlay" id="modal" onclick="handleClick(event)">
        <div class="box" id="box">
            <div class="close-btn" onclick="close_()">✕</div>

            <div class="verdict">
                <div class="v-emoji">{emoji}</div>
                <div class="v-label">{label}</div>
                <div class="v-desc">{desc}</div>
            </div>

            <div class="metrics">
                <div class="metric">
                    <div class="m-lbl">Confidence</div>
                    <div class="m-val conf">{conf_pct}</div>
                    <div class="bar-track"><div class="bar-fill"></div></div>
                </div>
                <div class="metric">
                    <div class="m-lbl">Rounds</div>
                    <div class="m-val">{funding_rounds}</div>
                </div>
                <div class="metric">
                    <div class="m-lbl">Total Raised</div>
                    <div class="m-val">{raised_str}</div>
                </div>
            </div>

            <div class="hint">Click ✕ or outside the card to dismiss</div>
        </div>
    </div>
    <script>
        function close_() {{
            document.getElementById('modal').style.display = 'none';
        }}
        function handleClick(e) {{
            if (e.target === document.getElementById('modal')) close_();
        }}
    </script>
    </body></html>
    """, height=480, scrolling=False)