import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="SupeRR Selector Season 2", page_icon="🏏", layout="wide")

BASE = Path(__file__).parent
BATTERS_FILE = BASE / "top_10_batters.csv"
BOWLERS_FILE = BASE / "top_10_bowlers.csv"
REPORT_FILE = BASE / "methodology_report.pdf"

st.title("SupeRR Selector Season 2")
st.subheader("Identify the Most Reliable Players Under Pressure")
st.caption("Rankings are displayed directly from the supplied reference CSV files. This dashboard does not recalculate or reorder them.")

@st.cache_data
def load_csv(path):
    return pd.read_csv(path)

if not BATTERS_FILE.exists() or not BOWLERS_FILE.exists():
    st.error("Required ranking CSV files are missing. Keep both ranking CSV files in the same repository folder as app.py.")
    st.stop()

batters = load_csv(BATTERS_FILE)
bowlers = load_csv(BOWLERS_FILE)

overview, batting, bowling, methodology = st.tabs(
    ["Overview", "Top 10 Batters", "Top 10 Bowlers", "Methodology"]
)

with overview:
    c1, c2, c3 = st.columns(3)
    c1.metric("Ranked batters", len(batters))
    c2.metric("Ranked bowlers", len(bowlers))
    c3.metric("Competition scope", "IPL + T20I")
    st.markdown("### Number 1 ranked players")
    left, right = st.columns(2)
    left.metric("Top batter", str(batters.iloc[0]["player"]))
    right.metric("Top bowler", str(bowlers.iloc[0]["player"]))
    st.info("Player names and ranking order are read directly from the supplied reference CSV files.")

with batting:
    st.markdown("### Top 10 Batters")
    st.caption("Displayed in the exact order supplied in top_10_batters.csv.")
    st.dataframe(batters, use_container_width=True, hide_index=True)
    if "score" in batters.columns:
        st.markdown("#### Batting score")
        st.bar_chart(batters.set_index("player")["score"])

with bowling:
    st.markdown("### Top 10 Bowlers")
    st.caption("Displayed in the exact order supplied in top_10_bowlers.csv.")
    st.dataframe(bowlers, use_container_width=True, hide_index=True)
    if "score" in bowlers.columns:
        st.markdown("#### Bowling score")
        st.bar_chart(bowlers.set_index("player")["score"])

with methodology:
    st.markdown("### Original methodology report")
    st.write("This is the original methodology PDF supplied for the project. The dashboard does not rewrite or reinterpret its methodology.")
    if REPORT_FILE.exists():
        with open(REPORT_FILE, "rb") as f:
            pdf_bytes = f.read()
        st.download_button(
            "Download methodology report (PDF)",
            data=pdf_bytes,
            file_name="methodology_report.pdf",
            mime="application/pdf",
        )
        st.success("The original methodology report is included.")
    else:
        st.warning("Upload methodology_report.pdf beside app.py in the GitHub repository to enable the report download.")
    st.markdown("The report covers data scope, pressure definition, scoring, rankings, limitations, and reproducibility notes.")
