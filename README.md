# SupeRR Selector – Season 2 Dashboard

A Streamlit dashboard presenting a reproducible, rule-based analysis of batter and bowler performance in high-pressure T20 match situations.

## Files
- `app.py` — Streamlit dashboard
- `player_metrics.csv` — aggregated player metrics and rankings (no ball-by-ball rows)
- `requirements.txt` — Python dependencies
- `METHODOLOGY.md` — pressure definition, formulas, rankings and limitations

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy
Deploy this repository with Streamlit Community Cloud. Set the main file path to `app.py`.

## Important
The rankings depend on the pressure definition and scoring weights documented in `METHODOLOGY.md`. They are analytical outputs, not claims about players' mental states. The original ball-by-ball dataset is not included.
