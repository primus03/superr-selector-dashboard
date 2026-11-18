# SupeRR Selector Season 2 — Methodology Report

## 1. Objective and source data
This analysis addresses the supplied Round 1 brief: identify the 10 batters and 10 bowlers whose measured performance is strongest in defined high-pressure situations compared with their own usual performance.

The analysis uses the supplied `ball_by_ball.csv`, `matches.csv` and `competitions.csv`. It includes competitions marked T20I and competitions whose names contain IPL, and uses innings 1 and 2 only. It excludes other domestic T20 competitions. The analysis covers 837 matches and 193,988 delivery records after those filters.

## 2. Pressure definition
The brief explicitly leaves the pressure definition to the analyst. This report uses transparent match-state rules applied before each delivery.

- **First innings:** pressure if at least 90 legal balls have already been bowled (15 overs) and at least four wickets have fallen; OR if at least 102 but fewer than 120 legal balls have been bowled (the final three overs).
- **Second innings:** pressure if the required run rate is at least 10 runs per over; OR if the required rate is at least 8 and five or fewer wickets remain.
- Required rate is runs still needed divided by overs remaining. The target is the first-innings total plus one, unless a positive revised target is supplied in the match record.
- The rules label the match situation, not a player's emotions. They are intentionally simple and reproducible.

For each delivery, the state is calculated immediately before that delivery. Legal balls exclude wides and no-balls (`extras_type` values `wide` and `Overstep`). The source's `extras1_runs` field is a categorical code, so it is not treated as a run count. Team totals add batter runs, one run for a wide/no-ball, and `extras_2_runs`.

## 3. Batting rating
For each batter, pressure and non-pressure deliveries are separated. Strike rate is runs per 100 legal balls. Batting average is runs divided by dismissals of that striker recorded in the data.

`Batting raw score = (pressure strike rate − baseline strike rate) + 0.5 × (pressure average − baseline average)`

A batter is eligible only with at least 60 pressure legal balls and 100 non-pressure legal balls.

## 4. Bowling rating
Bowler economy is runs charged to the bowler per six legal balls. Wides and no-balls are charged to the bowler; byes and leg-byes are not. Wicket rate is bowler-credited wickets per 100 legal balls. Bowler-credited dismissals are caught, bowled, LBW, stumped, and hit wicket; run-outs and other non-bowler dismissals are excluded.

`Bowling raw score = (baseline economy − pressure economy) + 0.1 × (pressure wickets/100 balls − baseline wickets/100 balls)`

A bowler is eligible only with at least 60 pressure legal balls and 100 non-pressure legal balls.

## 5. Reliability adjustment and ranking
For both roles, the raw score is multiplied by:

`Reliability factor = √(pressure legal balls / (pressure legal balls + 100))`

This shrinks ratings from smaller pressure samples toward zero. Eligible players are sorted by adjusted rating, highest first. There are 170 eligible batters and 204 eligible bowlers under these minimum-ball rules.

## 6. Top 10 batters
|   rank | player_name          |   rating |   pressure_balls |   pressure_sr |   baseline_sr |   pressure_avg |   baseline_avg |
|-------:|:---------------------|---------:|-----------------:|--------------:|--------------:|---------------:|---------------:|
|      1 | Dinesh Karthik       |    83.73 |              509 |        185.46 |         97.66 |          32.55 |          25    |
|      2 | Shashank Singh       |    68.57 |              345 |        185.51 |        123.26 |          53.33 |          22.08 |
|      3 | Gareth Delany        |    58.92 |              187 |        155.08 |         85.19 |          19.33 |          13.14 |
|      4 | Mahendra Singh Dhoni |    57.05 |              356 |        171.35 |         79.81 |          29.05 |          83    |
|      5 | Gulbadin Naib        |    56.72 |               63 |        161.9  |        112.95 |         102    |          17.44 |
|      6 | Fakhar Zaman         |    55.89 |              110 |        199.09 |        122.49 |          27.38 |          26.14 |
|      7 | Reeza Hendricks      |    52.18 |              304 |        175    |        130.57 |          59.11 |          27.68 |
|      8 | Saim Ayub            |    49.61 |               71 |        197.18 |        132.8  |          46.67 |          21.46 |
|      9 | Sam Billings         |    47.68 |               69 |        171.01 |        101.82 |          29.5  |          18.67 |
|     10 | Jaker Ali Anik       |    47    |              231 |        163.64 |        103.97 |          25.2  |          32    |

## 7. Top 10 bowlers
|   rank | player_name     |   rating |   pressure_balls |   pressure_economy |   baseline_economy |   pressure_wickets |   pressure_wickets_per_100 |
|-------:|:----------------|---------:|-----------------:|-------------------:|-------------------:|-------------------:|---------------------------:|
|      1 | Tabraiz Shamsi  |     2.52 |              113 |               7.86 |              10.51 |                 12 |                      10.62 |
|      2 | Sakib Hussain   |     2.42 |              148 |               8.15 |              10.91 |                 11 |                       7.43 |
|      3 | Mohammad Nawaz  |     2.3  |              232 |               5.56 |               7.59 |                 28 |                      12.07 |
|      4 | Vipraj Nigam    |     2.08 |               90 |               7.67 |              10.7  |                  4 |                       4.44 |
|      5 | Hasan Mahmud    |     2.05 |              127 |               6.33 |               8.5  |                 12 |                       9.45 |
|      6 | Lizaad Williams |     1.72 |               73 |               8.96 |              11.32 |                  6 |                       8.22 |
|      7 | Rasikh Salam    |     1.49 |              221 |               9.37 |              10.54 |                 21 |                       9.5  |
|      8 | Anshul Kamboj   |     1.49 |              137 |               9.02 |              10.34 |                 15 |                      10.95 |
|      9 | Kyle Jamieson   |     1.21 |              173 |               8.81 |              10.12 |                 12 |                       6.94 |
|     10 | Abrar Ahmed     |     1.2  |              251 |               5.9  |               7.03 |                 20 |                       7.97 |

## 8. Limitations and reliability
- The pressure thresholds and score weights are analyst-selected choices, not values prescribed by the challenge brief.
- The model compares each player with their own non-pressure baseline, but does not fully adjust for batting position, bowling phase, opposition quality, venue, pitch, match importance, or role.
- The data's dismissal and extras fields have to be interpreted consistently; the report documents the handling used here.
- A minimum-ball threshold and reliability adjustment reduce, but do not eliminate, small-sample effects.
- A positive rating means the player's measured performance improved under these defined conditions relative to their own baseline. It does not prove psychological resilience or guarantee future performance.
- Rankings should be treated as the output of this stated model, not as a universal or definitive player-quality ranking.

## 9. Reproducibility
The dashboard reads `player_metrics.csv`, which contains aggregated player-level outputs only. The original ball-by-ball source file is not included in this public-ready folder. Retain the original source data privately. The `app.py` dashboard can be run with the packages listed in `requirements.txt`.
