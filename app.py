"""
LaunchLyft — Startup Success Predictor
Streamlit App

Run with: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="LaunchLyft — Startup Success Predictor",
    page_icon="🚀",
    layout="wide",
)

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #1565C0;
        text-align: center;
        margin-bottom: 0;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        border-left: 4px solid #1565C0;
    }
    .acquired-box {
        background: linear-gradient(135deg, #e8f5e9, #c8e6c9);
        border: 2px solid #4CAF50;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
    }
    .closed-box {
        background: linear-gradient(135deg, #ffebee, #ffcdd2);
        border: 2px solid #f44336;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
    }
    .insight-box {
        background: #fff3e0;
        border-left: 4px solid #FF9800;
        border-radius: 8px;
        padding: 1rem;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ─── Header ──────────────────────────────────────────────────────────────────
st.markdown('<p class="main-title">🚀 LaunchLyft</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI-Powered Startup Success Predictor · Built with Machine Learning</p>', unsafe_allow_html=True)
st.divider()

# ─── Load Model ──────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    """Load the trained model package."""
    if os.path.exists('launchlyft_model.pkl'):
        return joblib.load('launchlyft_model.pkl')
    return None

model_package = load_model()

# ─── Sidebar: About ──────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🧠 About LaunchLyft")
    st.info(
        "LaunchLyft uses machine learning trained on **Crunchbase startup data** "
        "to predict whether a startup is likely to be **Acquired** or **Closed**.\n\n"
        "**Key factors considered:**\n"
        "- Funding amount & rounds\n"
        "- VC / Angel investment\n"
        "- Funding timeline & duration\n"
        "- Startup category\n"
        "- Geographic location (US state)\n"
        "- Milestones & relationships"
    )

    if model_package:
        st.success(f"✅ Model loaded: **{model_package['model_name']}**")
        metrics = model_package.get('metrics', {})
        if metrics:
            st.markdown("**Model Performance:**")
            for k, v in metrics.items():
                st.write(f"  • {k}: `{v}`")
    else:
        st.warning("⚠️ Model file not found. Please train the model first (run the notebook).")

# ─── Main Input Form ─────────────────────────────────────────────────────────
st.subheader("📝 Enter Startup Details")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**💰 Funding Information**")
    funding_total_usd = st.number_input(
        "Total Funding (USD)", min_value=0, value=1000000, step=100000,
        help="Total funding raised in USD"
    )
    funding_rounds = st.slider("Number of Funding Rounds", 1, 10, 2)
    has_VC = st.checkbox("Has VC Funding", value=True)
    has_angel = st.checkbox("Has Angel Funding", value=False)
    has_roundA = st.checkbox("Series A", value=False)
    has_roundB = st.checkbox("Series B", value=False)
    has_roundC = st.checkbox("Series C", value=False)
    has_roundD = st.checkbox("Series D", value=False)
    avg_participants = st.number_input(
        "Avg. Funding Participants", min_value=0.0, value=2.0, step=0.5
    )

with col2:
    st.markdown("**📅 Timeline**")
    founded_year = st.number_input("Founded Year", min_value=1980, max_value=2025, value=2010)
    first_funding_year = st.number_input("First Funding Year", min_value=1980, max_value=2025, value=2011)
    last_funding_year = st.number_input("Last Funding Year", min_value=1980, max_value=2025, value=2013)
    funding_duration_days = st.number_input(
        "Funding Duration (days)", min_value=0, value=365, step=30,
        help="Days between first and last funding"
    )
    funding_age_days = st.number_input(
        "Days from Founded to First Funding", min_value=0, value=300, step=30
    )

    st.markdown("**📊 Milestones & Network**")
    milestones = st.slider("Milestones Achieved", 0, 10, 2)
    relationships = st.slider("Number of Relationships", 0, 30, 5)
    is_top500 = st.checkbox("Top 500 Startup", value=False)

with col3:
    st.markdown("**🌍 Location (US State)**")
    state = st.selectbox("State", ["CA", "NY", "MA", "TX", "Other"])
    is_CA = int(state == "CA")
    is_NY = int(state == "NY")
    is_MA = int(state == "MA")
    is_TX = int(state == "TX")
    is_otherstate = int(state == "Other")

    st.markdown("**🏭 Category**")
    category = st.selectbox("Startup Category", [
        "software", "web", "mobile", "enterprise", "advertising",
        "gamesvideo", "ecommerce", "biotech", "consulting", "other"
    ])
    is_software   = int(category == "software")
    is_web        = int(category == "web")
    is_mobile     = int(category == "mobile")
    is_enterprise = int(category == "enterprise")
    is_advertising = int(category == "advertising")
    is_gamesvideo  = int(category == "gamesvideo")
    is_ecommerce   = int(category == "ecommerce")
    is_biotech     = int(category == "biotech")
    is_consulting  = int(category == "consulting")
    is_othercategory = int(category == "other")

    st.markdown("**📍 Geo Coordinates**")
    latitude  = st.number_input("Latitude",  value=37.77, format="%.4f")
    longitude = st.number_input("Longitude", value=-122.42, format="%.4f")

# ─── Prediction Logic ─────────────────────────────────────────────────────────
def build_feature_row():
    """Build the feature vector matching the training feature set."""
    # Engineered features
    funding_per_round = np.log1p(funding_total_usd / max(funding_rounds, 1))
    active_round_count = has_roundA + has_roundB + has_roundC + has_roundD
    has_equity = int(has_VC or has_angel)
    log_funding = np.log1p(funding_total_usd)

    # Category dummies (one-hot for top 10 cats)
    all_cats = ['software', 'web', 'mobile', 'enterprise', 'advertising',
                'gamesvideo', 'ecommerce', 'biotech', 'consulting', 'other']
    cat_features = {f'cat_{c}': int(category == c) for c in all_cats}

    row = {
        'latitude': latitude,
        'longitude': longitude,
        'age_first_funding_year': first_funding_year - founded_year,
        'age_last_funding_year': last_funding_year - founded_year,
        'age_first_milestone_year': 0.0,  # not collected in UI
        'age_last_milestone_year': 0.0,
        'relationships': relationships,
        'funding_rounds': funding_rounds,
        'funding_total_usd': log_funding,
        'milestones': milestones,
        'is_CA': is_CA, 'is_NY': is_NY, 'is_MA': is_MA,
        'is_TX': is_TX, 'is_otherstate': is_otherstate,
        'is_software': is_software, 'is_web': is_web,
        'is_mobile': is_mobile, 'is_enterprise': is_enterprise,
        'is_advertising': is_advertising, 'is_gamesvideo': is_gamesvideo,
        'is_ecommerce': is_ecommerce, 'is_biotech': is_biotech,
        'is_consulting': is_consulting, 'is_othercategory': is_othercategory,
        'has_VC': int(has_VC), 'has_angel': int(has_angel),
        'has_roundA': int(has_roundA), 'has_roundB': int(has_roundB),
        'has_roundC': int(has_roundC), 'has_roundD': int(has_roundD),
        'avg_participants': avg_participants,
        'is_top500': int(is_top500),
        'founded_year': founded_year,
        'first_funding_year': first_funding_year,
        'last_funding_year': last_funding_year,
        'funding_duration_days': funding_duration_days,
        'funding_age_days': funding_age_days,
        'funding_per_round': funding_per_round,
        'active_round_count': active_round_count,
        'has_equity': has_equity,
    }
    row.update(cat_features)
    return row


def make_prediction(row_dict, model_pkg):
    """Run prediction using the trained model."""
    feature_names = model_pkg['feature_names']
    model = model_pkg['model']

    # Build DataFrame with correct columns
    input_df = pd.DataFrame([row_dict])

    # Add missing columns with 0
    for col in feature_names:
        if col not in input_df.columns:
            input_df[col] = 0

    # Drop extra columns
    input_df = input_df[feature_names]

    pred = model.predict(input_df)[0]
    if hasattr(model, 'predict_proba'):
        proba = model.predict_proba(input_df)[0]
        confidence = proba[pred]
    else:
        confidence = None

    return int(pred), confidence


# ─── Predict Button ───────────────────────────────────────────────────────────
st.divider()
col_btn, _, _ = st.columns([1, 2, 1])
with col_btn:
    predict_clicked = st.button("🔮 Predict Startup Outcome", type="primary", use_container_width=True)

if predict_clicked:
    row = build_feature_row()

    if model_package is None:
        st.error("⚠️ Model not loaded. Please run the notebook to train and save the model first.")
    else:
        with st.spinner("Analyzing startup profile..."):
            pred, confidence = make_prediction(row, model_package)

        st.divider()
        st.subheader("📊 Prediction Result")

        res_col1, res_col2, res_col3 = st.columns([1.5, 1, 1])

        with res_col1:
            if pred == 1:
                st.markdown("""
                <div class="acquired-box">
                    <h2>✅ ACQUIRED</h2>
                    <p>This startup shows strong signals of success.<br>
                    It is predicted to be <strong>acquired</strong>.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="closed-box">
                    <h2>⚠️ CLOSED</h2>
                    <p>This startup shows risk factors.<br>
                    It is predicted to <strong>close</strong>.</p>
                </div>
                """, unsafe_allow_html=True)

        with res_col2:
            if confidence is not None:
                st.metric("Confidence Score", f"{confidence * 100:.1f}%")
            outcome_label = "Acquired" if pred == 1 else "Closed"
            st.metric("Predicted Outcome", outcome_label)

        with res_col3:
            st.metric("Funding Rounds", funding_rounds)
            st.metric("Total Funding", f"${funding_total_usd:,.0f}")

        # ─── Key Insight Explanation ───────────────────────────────────────────
        st.markdown("#### 🔍 Key Factors in This Prediction")

        insights = []

        if funding_total_usd > 5_000_000:
            insights.append("💰 **High funding** (>$5M) is a strong positive signal for acquisition.")
        elif funding_total_usd < 500_000:
            insights.append("💸 **Low total funding** (<$500K) increases closure risk.")

        if has_roundB or has_roundC or has_roundD:
            insights.append("📈 **Late-stage funding rounds** (B/C/D) significantly increase acquisition probability.")

        if has_VC:
            insights.append("🏦 **VC-backed startups** have higher survival and acquisition rates.")

        if funding_rounds >= 3:
            insights.append(f"🔄 **{funding_rounds} funding rounds** indicates sustained investor confidence.")

        if is_top500:
            insights.append("🏆 **Top 500 ranking** is a strong predictor of success.")

        if avg_participants >= 3:
            insights.append(f"🤝 **{avg_participants:.0f} avg. participants** per round shows broad investor interest.")

        if milestones >= 3:
            insights.append(f"🎯 **{milestones} milestones** achieved indicates product-market progress.")

        if is_CA or is_NY or is_MA:
            state_name = "California" if is_CA else "New York" if is_NY else "Massachusetts"
            insights.append(f"📍 **{state_name}** is a top startup hub with high acquisition rates.")

        if not insights:
            insights.append("ℹ️ Prediction is based on the combination of all entered features.")

        insight_html = "<div class='insight-box'>"
        for ins in insights:
            insight_html += f"<p>{ins}</p>"
        insight_html += "</div>"
        st.markdown(insight_html, unsafe_allow_html=True)

# ─── Demo Mode (if no model) ──────────────────────────────────────────────────
if not model_package and not predict_clicked:
    st.info(
        "📌 **Demo Mode**: No trained model found. "
        "Run `LaunchLyft_Notebook.ipynb` first to train and save `launchlyft_model.pkl`, "
        "then place it in the same folder as this app."
    )

# ─── Footer ──────────────────────────────────────────────────────────────────
st.divider()
st.markdown(
    "<div style='text-align:center;color:#999;font-size:0.85rem;'>"
    "LaunchLyft · AI Course Project · Built with Streamlit & Scikit-learn · "
    "Data: Crunchbase Startup Dataset"
    "</div>",
    unsafe_allow_html=True
)
