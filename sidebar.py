import streamlit as st


def render_sidebar(model_package):
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-logo">
            <div class="sidebar-logo-icon">🚀</div>
            <div>
                <div class="sidebar-logo-text">LaunchLyft</div>
                <div class="sidebar-logo-badge">AI · v2.0</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if model_package:
            model_name = model_package.get('model_name', 'ML Model')
            st.markdown(f"""
            <div class="model-status">
                <div class="model-status-dot"></div>
                <div class="model-status-label">{model_name} · Active</div>
            </div>
            """, unsafe_allow_html=True)
            metrics = model_package.get('metrics', {})
            if metrics:
                st.markdown('<div class="sidebar-section-label">Model Performance</div>', unsafe_allow_html=True)
                for k, v in metrics.items():
                    st.markdown(f"""
                    <div class="metric-chip">
                        <span class="metric-chip-label">{k}</span>
                        <span class="metric-chip-value">{v}</span>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="model-status" style="background:rgba(252,129,129,0.08);border-color:rgba(252,129,129,0.25);">
                <div class="model-status-dot" style="background:#fc8181;box-shadow:0 0 8px #fc8181;"></div>
                <div class="model-status-label" style="color:#fc8181;">Model not loaded</div>
            </div>
            """, unsafe_allow_html=True)
            st.caption("Run the training notebook to generate `launchlyft_model.pkl`")

        st.markdown('<div class="sidebar-section-label">Signal Factors</div>', unsafe_allow_html=True)
        factors = [
            "Funding Amount & Rounds", "VC / Angel Investment",
            "Funding Timeline", "Startup Category",
            "US State Location", "Milestones & Network",
        ]
        factor_html = "".join([f'<span class="factor-tag">◈ {f}</span>' for f in factors])
        st.markdown(f'<div style="line-height:2;">{factor_html}</div>', unsafe_allow_html=True)

        st.markdown('<div class="sidebar-section-label">Data Source</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size:0.78rem;color:var(--text-muted);line-height:1.6;">'
            'Trained on historical <strong style="color:var(--text-secondary)">Crunchbase</strong> '
            'startup data covering funding rounds, acquisitions, and closures.</div>',
            unsafe_allow_html=True,
        )