# 📊 User Journey & Process Analysis Dashboard

> An interactive Streamlit dashboard for mapping user journeys, identifying friction points, and tracking KPIs across core product processes.

---

## Overview

This project analyzes complex datasets to visualize end-to-end user journeys — from awareness through retention — surfacing friction points that cause drop-off and enabling stakeholders to make data-driven optimization decisions. All KPIs are surfaced through automated, interactive dashboards built with Streamlit and Plotly.

---

## Features

- **KPI Summary Cards** — Conversion rate, average session time, drop-off rate, and processes mapped with period-over-period deltas
- **User Journey Funnel** — Five-stage funnel (Awareness → Exploration → Consideration → Conversion → Retention) with user counts and drop percentages
- **Friction Point Log** — Prioritized list of UX blockers filtered by severity: High, Medium, and Low
- **Weekly Conversion Trend** — Dual-axis line chart tracking conversion rate (%) vs. session volume (k) over up to 12 weeks
- **Before vs. After Drop-off** — Grouped bar chart measuring the impact of process optimizations by funnel stage
- **Process Optimization Timeline** — Status tracker for four project phases with visual progress indicators
- **Automated Dashboards Grid** — Overview of six live dashboards with their tech stack and refresh cadence
- **Interactive Sidebar** — Filter friction severity and adjust the week range dynamically

---

## Tech Stack

| Layer | Tool |
|---|---|
| App framework | [Streamlit](https://streamlit.io) |
| Charts | [Plotly](https://plotly.com/python/) |
| Data manipulation | [Pandas](https://pandas.pydata.org) |
| Styling | Custom CSS via `st.markdown` |
| Fonts | DM Serif Display, DM Mono, Outfit (Google Fonts) |

---

## Project Structure

```
.
├── app.py          # Main Streamlit application
├── README.md       # This file
└── requirements.txt
```

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/user-journey-analysis.git
cd user-journey-analysis
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

4. Open your browser at `http://localhost:8501`

---

## Requirements

Create a `requirements.txt` with the following:

```
streamlit>=1.32.0
plotly>=5.20.0
pandas>=2.0.0
```

---

## Dashboard Sections

### KPI Cards
Four headline metrics displayed at the top of the dashboard, each with a trend indicator showing change vs. the prior period.

| Metric | Value | Trend |
|---|---|---|
| Conversion Rate | 34.2% | ↑ 8.4% |
| Avg. Session Time | 4m 38s | ↑ 12% engagement |
| Drop-off Rate | 21.7% | ↓ 5.1% after fix |
| Processes Mapped | 14 | ↑ 100% coverage |

### Friction Points
Five identified blockers across the product funnel, each assigned a severity level and actionable description. Filterable via the sidebar.

### Automated Dashboards
Six live dashboards deployed across the analytics stack, covering real-time conversion monitoring, funnel analytics, friction heatmaps, executive KPI views, cohort retention, and SLA tracking.

| Dashboard | Cadence | Stack |
|---|---|---|
| Conversion Monitor | Real-time | SQL + Tableau |
| Funnel Analytics | Daily | Python + Looker |
| Friction Heatmap | Event-based | Mixpanel |
| KPI Executive View | Weekly | Power BI |
| Cohort Retention | Monthly | dbt + BigQuery |
| Process SLA Tracker | Hourly | Airflow |

---

## Sidebar Controls

| Control | Description |
|---|---|
| Weeks to display | Adjusts the conversion trend chart from 4 to 12 weeks |
| Friction severity | Filters the friction point log by High / Medium / Low |

---

## Customization

To swap in your own data, update the relevant lists and DataFrames directly in `app.py`:

- **Funnel data** — edit the `funnel_data` DataFrame (Stage, Users, Pct)
- **Friction points** — edit the `friction_points` list (text, severity, dot class, tag class)
- **Trend data** — edit `conv_data` and `session_data` arrays
- **Before/After chart** — edit `before` and `after` lists
- **Dashboards** — edit the `dashboards` list (name, stack)

---

## License

MIT License. See `LICENSE` for details.

---

## Author

Built as part of a data analysis portfolio project focused on user journey mapping and process optimization.
