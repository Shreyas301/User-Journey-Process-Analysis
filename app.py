import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="User Journey & Process Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Mono:wght@400;500&family=Outfit:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
}

.main-title {
    font-family: 'DM Serif Display', serif;
    font-size: 2.2rem;
    font-weight: 400;
    line-height: 1.2;
    margin-bottom: 0.25rem;
}

.eyebrow {
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #888780;
    margin-bottom: 0.4rem;
}

.section-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #888780;
    border-bottom: 1px solid #e0ddd6;
    padding-bottom: 0.4rem;
    margin-bottom: 1rem;
    margin-top: 1.5rem;
}

.kpi-card {
    background: #f7f6f2;
    border-radius: 8px;
    padding: 1rem 1.1rem;
    margin-bottom: 0.5rem;
}

.kpi-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #888780;
    margin-bottom: 4px;
}

.kpi-value-blue  { font-size: 1.7rem; font-weight: 500; color: #185FA5; line-height: 1; }
.kpi-value-green { font-size: 1.7rem; font-weight: 500; color: #3B6D11; line-height: 1; }
.kpi-value-amber { font-size: 1.7rem; font-weight: 500; color: #854F0B; line-height: 1; }
.kpi-value-coral { font-size: 1.7rem; font-weight: 500; color: #993C1D; line-height: 1; }

.delta-up   { font-size: 0.75rem; color: #3B6D11; margin-top: 3px; }
.delta-down { font-size: 0.75rem; color: #A32D2D; margin-top: 3px; }

.friction-item {
    display: flex;
    align-items: flex-start;
    gap: 8px;
    padding: 9px 0;
    border-bottom: 0.5px solid #e8e6e0;
    font-size: 0.8rem;
    color: #5F5E5A;
}

.dot { width: 8px; height: 8px; border-radius: 50%; margin-top: 3px; flex-shrink: 0; display: inline-block; }
.dot-high   { background: #E24B4A; }
.dot-med    { background: #EF9F27; }
.dot-low    { background: #3B6D11; }

.tag { font-size: 0.65rem; font-family: 'DM Mono', monospace; padding: 2px 7px; border-radius: 4px; margin-left: auto; white-space: nowrap; }
.tag-high   { background: #FCEBEB; color: #A32D2D; }
.tag-med    { background: #FAEEDA; color: #854F0B; }
.tag-low    { background: #EAF3DE; color: #3B6D11; }

.auto-card {
    background: white;
    border: 0.5px solid #e0ddd6;
    border-radius: 8px;
    padding: 12px 14px;
    margin-bottom: 8px;
}
.auto-name { font-size: 0.8rem; font-weight: 500; margin-bottom: 2px; }
.auto-type { font-size: 0.65rem; font-family: 'DM Mono', monospace; text-transform: uppercase; letter-spacing: 0.06em; color: #888780; }
.auto-status { display: inline-flex; align-items: center; gap: 4px; font-size: 0.65rem; margin-top: 6px; padding: 2px 7px; border-radius: 4px; background: #EAF3DE; color: #3B6D11; }

.tl-item { padding: 10px 0 10px 18px; border-left: 2px solid #e0ddd6; position: relative; margin-bottom: 2px; }
.tl-dot { width: 10px; height: 10px; border-radius: 50%; position: absolute; left: -6px; top: 14px; }
.tl-title { font-size: 0.82rem; font-weight: 500; margin-bottom: 2px; }
.tl-sub { font-size: 0.75rem; color: #5F5E5A; }

.panel {
    background: white;
    border: 0.5px solid #e0ddd6;
    border-radius: 12px;
    padding: 1.25rem;
}
</style>
""", unsafe_allow_html=True)


# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="eyebrow">Portfolio · Data Analysis</div>', unsafe_allow_html=True)
    st.markdown("## Filters")

    weeks = st.slider("Weeks to display", min_value=4, max_value=12, value=12, step=1)

    severity_filter = st.multiselect(
        "Friction severity",
        ["High", "Medium", "Low"],
        default=["High", "Medium", "Low"],
    )

    st.markdown("---")
    st.markdown('<div class="eyebrow">Quick Stats</div>', unsafe_allow_html=True)
    st.metric("Total Users", "12,400", "+8%")
    st.metric("Avg Conversion", "34.2%", "+8.4%")
    st.metric("Friction Points", "5 critical", "-2 resolved")


# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<div class="eyebrow">Portfolio · Data Analysis</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">User Journey &<br>Process Analysis</div>', unsafe_allow_html=True)
st.markdown(
    '<p style="color:#5F5E5A; font-size:0.9rem; max-width:680px; line-height:1.6; margin-bottom:1.5rem;">'
    "Analyzed complex datasets to map user journeys, identifying friction points in core processes "
    "to support optimization. Developed automated dashboards to track KPIs, enabling stakeholders "
    "to make data-driven decisions.</p>",
    unsafe_allow_html=True,
)


# ── KPI Cards ────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Key Performance Indicators</div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
kpis = [
    (c1, "Conversion Rate", "34.2%", "kpi-value-blue",  "delta-up",   "↑ 8.4% vs prior period"),
    (c2, "Avg. Session Time", "4m 38s", "kpi-value-green","delta-up",  "↑ 12% engagement"),
    (c3, "Drop-off Rate",   "21.7%", "kpi-value-amber", "delta-down", "↓ 5.1% after fix"),
    (c4, "Processes Mapped","14",    "kpi-value-coral",  "delta-up",  "↑ 100% coverage"),
]
for col, label, value, vcls, dcls, delta in kpis:
    with col:
        st.markdown(
            f'<div class="kpi-card">'
            f'<div class="kpi-label">{label}</div>'
            f'<div class="{vcls}">{value}</div>'
            f'<div class="{dcls}">{delta}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )


# ── Journey Funnel + Friction ─────────────────────────────────────────────────
st.markdown('<div class="section-label">User Journey & Friction Points</div>', unsafe_allow_html=True)

col_left, col_right = st.columns(2)

with col_left:
    funnel_data = pd.DataFrame({
        "Stage":   ["Awareness", "Exploration", "Consideration", "Conversion", "Retention"],
        "Users":   [12400, 9152, 6304, 4249, 2690],
        "Pct":     [100, 74, 51, 34, 22],
    })

    fig_funnel = go.Figure(go.Funnel(
        y=funnel_data["Stage"],
        x=funnel_data["Users"],
        textinfo="value+percent initial",
        marker=dict(color=["#B5D4F4","#85B7EB","#378ADD","#185FA5","#0C447C"]),
        connector=dict(line=dict(color="#e0ddd6", width=1)),
    ))
    fig_funnel.update_layout(
        margin=dict(l=0, r=0, t=10, b=10),
        height=300,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Outfit, sans-serif", size=12),
    )
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.82rem; font-weight:500; margin-bottom:0.75rem;">User journey stages</div>', unsafe_allow_html=True)
    st.plotly_chart(fig_funnel, use_container_width=True, config={"displayModeBar": False})
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    friction_points = [
        ("Checkout form — excessive required fields causing abandonment",       "High",   "dot-high", "tag-high"),
        ("Onboarding step 3 — unclear CTA leads to 38% drop-off",               "High",   "dot-high", "tag-high"),
        ("Mobile search results load time exceeds 3s threshold",                 "Medium", "dot-med",  "tag-med"),
        ("Account settings navigation — users struggle to find billing",         "Medium", "dot-med",  "tag-med"),
        ("Email confirmation copy — misaligned with brand voice",                "Low",    "dot-low",  "tag-low"),
    ]

    filtered = [(t, s, dc, tc) for t, s, dc, tc in friction_points if s in severity_filter]

    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.82rem; font-weight:500; margin-bottom:0.5rem;">Identified friction points</div>', unsafe_allow_html=True)
    for text, sev, dot_cls, tag_cls in filtered:
        st.markdown(
            f'<div class="friction-item">'
            f'<span class="dot {dot_cls}"></span>'
            f'<span style="flex:1">{text}</span>'
            f'<span class="tag {tag_cls}">{sev}</span>'
            f'</div>',
            unsafe_allow_html=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)


# ── Trend Chart ───────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Conversion Trend — Weekly</div>', unsafe_allow_html=True)

all_labels  = [f"W{i}" for i in range(1, 13)]
conv_data   = [24,26,25,28,27,30,29,31,33,32,34,34]
session_data= [9.2,9.8,9.4,10.1,10.5,11.2,10.8,11.6,12.0,11.8,12.2,12.4]

labels   = all_labels[:weeks]
conv     = conv_data[:weeks]
sessions = session_data[:weeks]

fig_trend = go.Figure()
fig_trend.add_trace(go.Scatter(
    x=labels, y=conv, name="Conversion %",
    line=dict(color="#185FA5", width=2.5),
    fill="tozeroy", fillcolor="rgba(24,95,165,0.08)",
    mode="lines+markers", marker=dict(size=5),
    yaxis="y1",
))
fig_trend.add_trace(go.Scatter(
    x=labels, y=sessions, name="Sessions (k)",
    line=dict(color="#639922", width=2.5),
    fill="tozeroy", fillcolor="rgba(99,153,34,0.07)",
    mode="lines+markers", marker=dict(size=5),
    yaxis="y2",
))
fig_trend.update_layout(
    height=260,
    margin=dict(l=0, r=0, t=10, b=10),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Outfit, sans-serif", size=12),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    xaxis=dict(showgrid=False, color="#888780"),
    yaxis=dict(title="Conversion %", color="#888780", gridcolor="#f0ede8", ticksuffix="%"),
    yaxis2=dict(title="Sessions (k)", overlaying="y", side="right", color="#888780", showgrid=False, ticksuffix="k"),
    hovermode="x unified",
)
st.plotly_chart(fig_trend, use_container_width=True, config={"displayModeBar": False})


# ── Timeline + Before/After ───────────────────────────────────────────────────
col_tl, col_bar = st.columns(2)

with col_tl:
    st.markdown('<div class="section-label">Process Optimization Timeline</div>', unsafe_allow_html=True)
    timeline = [
        ("Baseline journey mapping",  "Mapped 14 core workflows across 3 product areas", "#639922", "Completed"),
        ("Friction point analysis",   "Identified 5 critical, 7 medium severity blockers","#639922","Completed"),
        ("Dashboard automation",      "Live KPI tracking with stakeholder views",          "#185FA5","In progress"),
        ("Optimization iteration",    "A/B testing redesigned onboarding flow",            "#EF9F27","Upcoming"),
    ]
    tl_html = '<div style="background:white;border:0.5px solid #e0ddd6;border-radius:12px;padding:1.25rem;">'
    for title, sub, color, status in timeline:
        tl_html += (
            f'<div class="tl-item">'
            f'<div class="tl-dot" style="background:{color};"></div>'
            f'<div class="tl-title">{title}</div>'
            f'<div class="tl-sub">{sub}</div>'
            f'</div>'
        )
    tl_html += '</div>'
    st.markdown(tl_html, unsafe_allow_html=True)

with col_bar:
    st.markdown('<div class="section-label">Drop-off Before vs After</div>', unsafe_allow_html=True)
    stages  = ["Explore","Consider","Convert","Retain"]
    before  = [32, 41, 38, 44]
    after   = [18, 24, 22, 28]

    fig_cmp = go.Figure()
    fig_cmp.add_trace(go.Bar(name="Before", x=stages, y=before, marker_color="#F7C1C1", marker_line_width=0))
    fig_cmp.add_trace(go.Bar(name="After",  x=stages, y=after,  marker_color="#85B7EB", marker_line_width=0))
    fig_cmp.update_layout(
        height=230,
        barmode="group",
        margin=dict(l=0, r=0, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Outfit, sans-serif", size=12),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
        xaxis=dict(showgrid=False, color="#888780"),
        yaxis=dict(color="#888780", gridcolor="#f0ede8", ticksuffix="%"),
        bargap=0.25, bargroupgap=0.1,
    )
    st.plotly_chart(fig_cmp, use_container_width=True, config={"displayModeBar": False})


# ── Automated Dashboards ──────────────────────────────────────────────────────
st.markdown('<div class="section-label">Automated Dashboards Deployed</div>', unsafe_allow_html=True)

dashboards = [
    ("Conversion Monitor", "Real-time · SQL + Tableau"),
    ("Funnel Analytics",   "Daily · Python + Looker"),
    ("Friction Heatmap",   "Event-based · Mixpanel"),
    ("KPI Executive View", "Weekly · Power BI"),
    ("Cohort Retention",   "Monthly · dbt + BigQuery"),
    ("Process SLA Tracker","Hourly · Airflow alerts"),
]

cols = st.columns(3)
for i, (name, stack) in enumerate(dashboards):
    with cols[i % 3]:
        st.markdown(
            f'<div class="auto-card">'
            f'<div class="auto-name">{name}</div>'
            f'<div class="auto-type">{stack}</div>'
            f'<div class="auto-status">● Live</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

st.markdown("<br>", unsafe_allow_html=True)
