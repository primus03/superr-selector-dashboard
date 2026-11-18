import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SupeRR Selector | Pressure Analytics", page_icon="🏏", layout="wide")
st.title("🏏 SupeRR Selector – Season 2")
st.caption("Pressure-performance analysis using the supplied IPL and T20I ball-by-ball data")

@st.cache_data
def load_data():
    return pd.read_csv("player_metrics.csv")

df = load_data()
bat = df[df["category"] == "Batter"].sort_values("rank")
bowl = df[df["category"] == "Bowler"].sort_values("rank")

c1, c2, c3 = st.columns(3)
c1.metric("Eligible batters", f"{len(bat):,}")
c2.metric("Eligible bowlers", f"{len(bowl):,}")
c3.metric("Competitions", "IPL + T20I")

st.info("Rankings compare each player's pressure performance with their own non-pressure baseline. See the Methodology tab for definitions and limitations.")

tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Top 10 Batters", "Top 10 Bowlers", "Methodology"])

with tab1:
    st.subheader("Top-ranked players")
    left, right = st.columns(2)
    with left:
        st.markdown("**Batters**")
        st.dataframe(bat.head(10)[["rank","player_name","rating","pressure_sr","baseline_sr","pressure_balls"]].round(2),
                     hide_index=True, use_container_width=True)
    with right:
        st.markdown("**Bowlers**")
        st.dataframe(bowl.head(10)[["rank","player_name","rating","pressure_economy","baseline_economy","pressure_balls"]].round(2),
                     hide_index=True, use_container_width=True)
    fig = px.bar(bat.head(10).sort_values("rating"), x="rating", y="player_name", orientation="h",
                 title="Top 10 batter pressure ratings", labels={"rating":"Rating","player_name":"Player"})
    st.plotly_chart(fig, use_container_width=True)
    fig2 = px.bar(bowl.head(10).sort_values("rating"), x="rating", y="player_name", orientation="h",
                  title="Top 10 bowler pressure ratings", labels={"rating":"Rating","player_name":"Player"})
    st.plotly_chart(fig2, use_container_width=True)

with tab2:
    st.subheader("Top 10 batters under pressure")
    st.dataframe(bat.head(10)[["rank","player_name","rating","pressure_runs","pressure_balls","pressure_sr",
                               "baseline_sr","pressure_avg","baseline_avg","pressure_matches"]].round(2),
                 hide_index=True, use_container_width=True)
    st.caption("Pressure strike rate = pressure runs per 100 legal balls. Baseline uses the player's non-pressure deliveries.")

with tab3:
    st.subheader("Top 10 bowlers under pressure")
    st.dataframe(bowl.head(10)[["rank","player_name","rating","pressure_runs_conceded","pressure_balls",
                                "pressure_economy","baseline_economy","pressure_wickets",
                                "pressure_wickets_per_100","pressure_matches"]].round(2),
                 hide_index=True, use_container_width=True)
    st.caption("Economy rate is runs conceded per six legal balls. Wicket-rate counts bowler-credited dismissals only.")

with tab4:
    st.subheader("How pressure is defined")
    st.markdown("""
**First innings**
- A delivery is under pressure when at least 15 overs have been completed and at least four wickets have fallen; or when the final three overs are underway.

**Second innings**
- A delivery is under pressure when the required run rate is at least 10 runs per over; or when it is at least 8 and five or fewer wickets remain.

**Player eligibility**
- At least 60 legal balls in pressure situations and 100 legal balls in non-pressure situations.

**Batting rating**
- Pressure strike-rate improvement + 0.5 × batting-average improvement.
- The result is multiplied by a reliability factor: √(pressure balls / (pressure balls + 100)).

**Bowling rating**
- Economy-rate improvement + 0.1 × improvement in bowler-credited wickets per 100 legal balls.
- The result is multiplied by the same reliability factor.

The baseline is each player's own performance in non-pressure deliveries. IPL and T20I competitions are combined.
""")
    st.warning("This is a transparent, rule-based model, not a causal measure of psychological pressure. The thresholds and weights are modelling choices. Small samples, role, batting position, opposition strength, venue, innings length and match context can affect rankings.")
    st.markdown("See `METHODOLOGY.md` in the repository for the full explanation and ranked lists.")

st.divider()
st.caption("Prepared for the SupeRR Selector Season 2 Round 1 challenge. Use the methodology report alongside the Unstop rankings.")
