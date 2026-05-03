import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd

from result_popup import render_result_popup


def _hero():
    components.html("""
    <!DOCTYPE html><html><head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@800&family=DM+Sans:wght@300;400&display=swap');
        * { margin:0; padding:0; box-sizing:border-box; }
        body { background: transparent; font-family: 'DM Sans', sans-serif; color: #f0f4f8; }
        .hero {
            text-align: center; padding: 2rem 2rem 1rem;
            position: relative; overflow: hidden;
        }
        .glow {
            position: absolute; top: -60px; left: 50%; transform: translateX(-50%);
            width: 600px; height: 260px;
            background: radial-gradient(ellipse at center top, rgba(99,179,237,0.09) 0%, transparent 70%);
            pointer-events: none;
        }
        .pill {
            display: inline-flex; align-items: center; gap: 6px;
            background: rgba(99,179,237,0.08); border: 1px solid rgba(99,179,237,0.22);
            border-radius: 20px; padding: 5px 14px;
            font-size: 0.67rem; letter-spacing: 0.12em; text-transform: uppercase;
            color: #63b3ed; font-weight: 700; margin-bottom: 1rem;
        }
        .title {
            font-family: 'Syne', sans-serif;
            font-size: 2.6rem; font-weight: 800;
            letter-spacing: -0.03em; line-height: 1.1;
            background: linear-gradient(135deg, #f0f4f8 30%, #63b3ed 65%, #4fd1c5 100%);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            background-clip: text; margin: 0 0 0.6rem;
        }
        .sub {
            font-size: 0.95rem; color: #a0aec0; font-weight: 300;
            max-width: 460px; margin: 0 auto; line-height: 1.6;
        }
    </style>
    </head><body>
    <div class="hero">
        <div class="glow"></div>
        <div class="pill">Startup Intelligence Platform</div>
        <div class="title">Predict Your Exit</div>
        <div class="sub">Fill in your startup's profile and hit Analyze, our ML engine returns an instant acquisition-probability verdict.</div>
    </div>
    </body></html>
    """, height=200, scrolling=False)


def _section_header(icon, label, bg):
    components.html(f"""
    <!DOCTYPE html><html><head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700&display=swap');
        * {{ margin:0; padding:0; box-sizing:border-box; }}
        body {{ background: transparent; }}
        .sh {{
            display: flex; align-items: center; gap: 10px;
            padding-bottom: 0.6rem;
            border-bottom: 1px solid rgba(255,255,255,0.08);
        }}
        .icon {{
            width: 28px; height: 28px; border-radius: 6px;
            background: {bg};
            display: flex; align-items: center; justify-content: center;
            font-size: 0.85rem;
        }}
        .lbl {{
            font-family: 'Syne', sans-serif; font-size: 0.8rem; font-weight: 700;
            color: #f0f4f8; letter-spacing: 0.05em; text-transform: uppercase;
        }}
    </style>
    </head><body>
    <div class="sh">
        <div class="icon">{icon}</div>
        <span class="lbl">{label}</span>
    </div>
    </body></html>
    """, height=52, scrolling=False)


def _input_css():
    st.markdown("""
    <style>
    /* ── Uniform dark input boxes ── */
    .stNumberInput input,
    .stTextInput input,
    .stNumberInput > div > div > input,
    .stTextInput > div > div > input {
        background-color: rgba(13,17,23,0.95) !important;
        background: rgba(13,17,23,0.95) !important;
        border: 1px solid rgba(255,255,255,0.10) !important;
        border-radius: 6px !important;
        color: #f0f4f8 !important;
        font-size: 0.9rem !important;
        caret-color: #63b3ed !important;
    }
    .stNumberInput input:focus,
    .stTextInput input:focus {
        border-color: #63b3ed !important;
        box-shadow: 0 0 0 2px rgba(99,179,237,0.15) !important;
        outline: none !important;
    }

    /* stepper +/- buttons */
    .stNumberInput button {
        background: rgba(13,17,23,0.95) !important;
        border: 1px solid rgba(255,255,255,0.10) !important;
        color: #a0aec0 !important;
        border-radius: 6px !important;
    }
    .stNumberInput button:hover {
        background: rgba(99,179,237,0.12) !important;
        color: #f0f4f8 !important;
    }

    /* Selectbox — keep consistent */
    .stSelectbox > div > div {
        background: rgba(13,17,23,0.95) !important;
        border: 1px solid rgba(255,255,255,0.10) !important;
        border-radius: 6px !important;
        color: #f0f4f8 !important;
    }
    .stSelectbox > div > div:focus-within {
        border-color: #63b3ed !important;
        box-shadow: 0 0 0 2px rgba(99,179,237,0.15) !important;
    }

    /* Labels */
    .stNumberInput label, .stTextInput label,
    .stSelectbox label, .stSlider label,
    .stCheckbox label {
        color: #a0aec0 !important;
        font-size: 0.78rem !important;
        font-weight: 500 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.07em !important;
    }

    /* Checkbox */
    .stCheckbox {
        background: rgba(13,17,23,0.6) !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 6px !important;
        padding: 0.5rem 0.75rem !important;
        margin-bottom: 0.35rem !important;
    }
    .stCheckbox:hover {
        border-color: rgba(99,179,237,0.2) !important;
        background: rgba(99,179,237,0.04) !important;
    }
    .stCheckbox label {
        text-transform: none !important;
        letter-spacing: 0 !important;
        font-weight: 400 !important;
        color: #a0aec0 !important;
        font-size: 0.85rem !important;
    }

    /* Section subheadings */
    .stMarkdown strong {
        color: #a0aec0 !important;
        font-size: 0.75rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.08em !important;
    }
    </style>
    """, unsafe_allow_html=True)


def _build_feature_row(
    latitude, longitude,
    founded_year, first_funding_year, last_funding_year,
    funding_total_usd, funding_rounds, avg_participants,
    milestones, relationships, is_top500,
    has_VC, has_angel,
    has_roundA, has_roundB, has_roundC, has_roundD,
    funding_duration_days, funding_age_days,
    is_CA, is_NY, is_MA, is_TX, is_otherstate,
    category,
):
    funding_per_round  = np.log1p(funding_total_usd / max(funding_rounds, 1))
    active_round_count = int(has_roundA) + int(has_roundB) + int(has_roundC) + int(has_roundD)
    has_equity         = int(has_VC or has_angel)
    log_funding        = np.log1p(funding_total_usd)
    all_cats = ['software','web','mobile','enterprise','advertising',
                'gamesvideo','ecommerce','biotech','consulting','other']
    row = {
        'latitude': latitude, 'longitude': longitude,
        'age_first_funding_year': first_funding_year - founded_year,
        'age_last_funding_year':  last_funding_year  - founded_year,
        'age_first_milestone_year': 0.0, 'age_last_milestone_year': 0.0,
        'relationships': relationships, 'funding_rounds': funding_rounds,
        'funding_total_usd': log_funding, 'milestones': milestones,
        'is_CA': is_CA, 'is_NY': is_NY, 'is_MA': is_MA,
        'is_TX': is_TX, 'is_otherstate': is_otherstate,
        'is_software': int(category=='software'), 'is_web': int(category=='web'),
        'is_mobile': int(category=='mobile'), 'is_enterprise': int(category=='enterprise'),
        'is_advertising': int(category=='advertising'), 'is_gamesvideo': int(category=='gamesvideo'),
        'is_ecommerce': int(category=='ecommerce'), 'is_biotech': int(category=='biotech'),
        'is_consulting': int(category=='consulting'), 'is_othercategory': int(category=='other'),
        'has_VC': int(has_VC), 'has_angel': int(has_angel),
        'has_roundA': int(has_roundA), 'has_roundB': int(has_roundB),
        'has_roundC': int(has_roundC), 'has_roundD': int(has_roundD),
        'avg_participants': avg_participants, 'is_top500': int(is_top500),
        'founded_year': founded_year, 'first_funding_year': first_funding_year,
        'last_funding_year': last_funding_year,
        'funding_duration_days': funding_duration_days, 'funding_age_days': funding_age_days,
        'funding_per_round': funding_per_round, 'active_round_count': active_round_count,
        'has_equity': has_equity,
    }
    for c in all_cats:
        row[f'cat_{c}'] = int(category == c)
    return row


def _predict(row_dict, model_pkg):
    feature_names = model_pkg['feature_names']
    model         = model_pkg['model']
    input_df      = pd.DataFrame([row_dict])
    for col in feature_names:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[feature_names]
    pred = model.predict(input_df)[0]
    confidence = None
    if hasattr(model, 'predict_proba'):
        proba      = model.predict_proba(input_df)[0]
        confidence = proba[pred]
    return int(pred), confidence


def render_predictor(model_package):
    # Inject consistent input styles
    _input_css()

    # Back button
    if st.button("← Back to Home", key="back_btn"):
        st.session_state.page = "welcome"
        st.rerun()

    _hero()

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        _section_header("💰", "Funding", "rgba(99,179,237,0.15)")
        funding_total_usd = st.number_input("Total Funding (USD)", min_value=0, value=1_000_000, step=100_000)
        funding_rounds    = st.slider("Funding Rounds", 1, 10, 2)
        avg_participants  = st.number_input("Avg. Investors per Round", min_value=0.0, value=2.0, step=0.5)

        st.markdown("**Investment Type**")
        has_VC    = st.checkbox("VC Funding",    value=True)
        has_angel = st.checkbox("Angel Funding", value=False)

        st.markdown("**Funding Rounds**")
        has_roundA = st.checkbox("Series A", value=False)
        has_roundB = st.checkbox("Series B", value=False)
        has_roundC = st.checkbox("Series C", value=False)
        has_roundD = st.checkbox("Series D", value=False)

    with col2:
        _section_header("📅", "Timeline & Growth", "rgba(79,209,197,0.15)")
        founded_year          = st.number_input("Founded Year",       min_value=1980, max_value=2025, value=2010)
        first_funding_year    = st.number_input("First Funding Year", min_value=1980, max_value=2025, value=2011)
        last_funding_year     = st.number_input("Last Funding Year",  min_value=1980, max_value=2025, value=2013)
        funding_duration_days = st.number_input("Funding Duration (days)", min_value=0, value=365, step=30)
        funding_age_days      = st.number_input("Days: Founded → First Funding", min_value=0, value=300, step=30)

        st.markdown("&nbsp;", unsafe_allow_html=True)
        _section_header("🏆", "Traction", "rgba(246,173,85,0.15)")
        milestones    = st.slider("Milestones Achieved",   0, 10, 2)
        relationships = st.slider("Network Relationships", 0, 30, 5)
        is_top500     = st.checkbox("Top 500 Startup", value=False)

    with col3:
        _section_header("📍", "Location & Category", "rgba(99,179,237,0.15)")
        state = st.selectbox("US State", ["CA", "NY", "MA", "TX", "Other"])
        is_CA = int(state=="CA"); is_NY = int(state=="NY"); is_MA = int(state=="MA")
        is_TX = int(state=="TX"); is_otherstate = int(state=="Other")

        category = st.selectbox("Startup Category", [
            "software","web","mobile","enterprise","advertising",
            "gamesvideo","ecommerce","biotech","consulting","other"
        ])

        st.markdown("&nbsp;", unsafe_allow_html=True)
        _section_header("🌐", "Coordinates", "rgba(79,209,197,0.15)")
        latitude  = st.number_input("Latitude",  value=37.7700, format="%.4f")
        longitude = st.number_input("Longitude", value=-122.4200, format="%.4f")

    st.markdown('<div style="height:1.5rem;"></div>', unsafe_allow_html=True)
    b1, b2, b3 = st.columns([1, 2, 1])
    with b2:
        predict_clicked = st.button("Analyze Startup", type="primary", use_container_width=True)

    if predict_clicked:
        if model_package is None:
            st.error("Model not loaded. Run the training notebook first.")
        else:
            row = _build_feature_row(
                latitude, longitude,
                founded_year, first_funding_year, last_funding_year,
                funding_total_usd, funding_rounds, avg_participants,
                milestones, relationships, is_top500,
                has_VC, has_angel, has_roundA, has_roundB, has_roundC, has_roundD,
                funding_duration_days, funding_age_days,
                is_CA, is_NY, is_MA, is_TX, is_otherstate, category,
            )
            with st.spinner("Analyzing startup signals…"):
                pred, confidence = _predict(row, model_package)
            render_result_popup(pred, confidence, funding_total_usd, funding_rounds)

    if not model_package and not predict_clicked:
        st.info("**Demo Mode** — No model found. Run `LaunchLyft_Notebook.ipynb` to generate `launchlyft_model.pkl`.")

    st.markdown("""
    <div style="text-align:center;padding:2rem 0 1rem;border-top:1px solid rgba(255,255,255,0.07);
                margin-top:3rem;color:#718096;font-size:0.75rem;letter-spacing:0.04em;">
        <span style="font-weight:700;color:#a0aec0;">LaunchLyft</span>
        &nbsp;·&nbsp; AI Course Project &nbsp;·&nbsp;
        Built with Streamlit &amp; Scikit-learn &nbsp;·&nbsp; Data: Crunchbase
    </div>
    """, unsafe_allow_html=True)