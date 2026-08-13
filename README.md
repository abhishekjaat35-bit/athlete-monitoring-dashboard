# Athlete Monitoring Dashboard

A Python sports-performance analytics project that integrates athlete wellness and training-load data to produce an educational athlete monitoring report.

## Objective

The system combines:

- Sleep
- Soreness
- Fatigue
- Stress
- Mood
- Training load

to calculate:

- Wellness score
- Wellness percentage
- Training-load score
- Readiness score
- Readiness category
- Training-load category
- Monitoring flags
- Athlete ranking
- Team monitoring statistics

---

## Data Flow

```text
Athlete Data
      ↓
CSV
      ↓
Pandas
      ↓
Wellness Calculation
      ↓
Training Load Analysis
      ↓
Readiness Calculation
      ↓
Monitoring Classification
      ↓
Athlete Ranking
      ↓
Performance Report
      ↓
CSV Export
```

---

## Wellness Score

Sleep and mood are treated as positive indicators.

Soreness, fatigue and stress are treated as inverse indicators.

```text
Wellness Score =
Sleep
+ (6 - Soreness)
+ (6 - Fatigue)
+ (6 - Stress)
+ Mood
```

Maximum score:

```text
25
```

---

## Readiness Score

The educational model combines wellness and training-load components.

### Wellness component

```text
Wellness % =
Wellness Score / 25 × 100
```

### Training-load component

An 800 AU reference point is used:

```text
Load Score =
100 - (Training Load / 800 × 100)
```

The score is constrained to a minimum of zero.

### Combined score

```text
Readiness =
(Wellness % × 0.70)
+
(Load Score × 0.30)
```

The model therefore gives:

```text
70% → Wellness
30% → Training-load component
```

---

## Readiness Categories

| Score | Category |
|---:|---|
| ≥ 85% | High |
| 70–84.9% | Moderate |
| 55–69.9% | Low |
| < 55% | Very Low |

---

## Training Load Categories

| Training Load | Category |
|---:|---|
| ≥ 700 AU | Very High |
| 500–699 AU | High |
| 300–499 AU | Moderate |
| < 300 AU | Low |

---

## Monitoring Rules

The program identifies potential monitoring priorities.

### High Monitoring Priority

```text
Readiness < 55%
AND
Training Load ≥ 700 AU
```

### Monitor Closely

```text
Readiness < 70%
AND
Training Load ≥ 500 AU
```

### Good Status

```text
Readiness ≥ 85%
```

Other observations are classified as:

```text
Normal Monitoring
```

---

## Dataset

The project contains 20 synthetic athlete-monitoring observations across four athletes.

### Variables

| Variable | Description |
|---|---|
| Athlete | Athlete identifier |
| Date | Monitoring date |
| Sleep | 1–5 rating |
| Soreness | 1–5 rating |
| Fatigue | 1–5 rating |
| Stress | 1–5 rating |
| Mood | 1–5 rating |
| Training_Load | Training load in arbitrary units |

---

## Technologies

- Python
- Pandas
- CSV
- Functions
- Lambda functions
- DataFrames
- GroupBy
- Aggregation
- Sorting
- Conditional logic
- Feature engineering
- Data export

---

## Installation

Install Pandas:

```bash
pip install pandas
```

---

## Run

Place the Python file and CSV file in the same directory.

Run:

```bash
python athlete_monitoring_dashboard.py
```

---

## Output

The program generates:

```text
athlete_monitoring_results.csv
athlete_monitoring_summary.csv
```

The results contain calculated monitoring variables that can be used for further analysis or visualization.

---

## Example Results

Using the included synthetic dataset:

```text
Average Wellness Score : 21.3/25
Average Training Load  : 497.5 AU
Total Training Load    : 9950 AU
Average Team Readiness : 71.0%
```

The athlete ranking is:

```text
1. Vikram
2. Rahul
3. Priya
4. Arjun
```

The lowest-readiness observation is:

```text
Athlete: Arjun
Training Load: 800 AU
Readiness: 39.2%
Status: High Monitoring Priority
```

---

## Sports Performance Application

This type of system can serve as a foundation for athlete-monitoring workflows involving:

- Strength and conditioning
- Athlete wellness
- Training-load monitoring
- Recovery monitoring
- Performance analytics
- Training-session planning
- High-performance databases
- Athlete dashboards

---

## Scientific Limitations

This project is an educational programming model.

The readiness score is **not a validated measure** of:

- Injury risk
- Fatigue
- Recovery
- Overtraining
- Physiological readiness
- Training tolerance

The 70/30 weighting and 800 AU reference point are assumptions created for this portfolio project.

Real athlete-monitoring systems should use validated measures, individual baselines, longitudinal analysis, appropriate statistical methods and professional interpretation.

A single readiness score should never be used as the sole basis for making athlete-management decisions.

---

## Future Development

Potential improvements include:

- [ ] Add rolling training-load averages
- [ ] Add acute/chronic workload metrics
- [ ] Add heart-rate data
- [ ] Add HRV
- [ ] Add GPS distance
- [ ] Add high-speed running
- [ ] Add accelerations and decelerations
- [ ] Add jump testing
- [ ] Add strength testing
- [ ] Add sleep duration
- [ ] Add athlete-specific baselines
- [ ] Add longitudinal trends
- [ ] Add Matplotlib visualizations
- [ ] Build an interactive dashboard
- [ ] Add automated reports
- [ ] Add machine-learning models

---

## Skills Demonstrated

```text
Python
   ↓
CSV
   ↓
Pandas
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Sports Science Calculations
   ↓
Athlete Monitoring
   ↓
Classification
   ↓
Ranking
   ↓
Data Export
```

---

## Author

**Abhishek Tomar**

Strength & Conditioning | Sports Performance | Sports Analytics | Python

---

## License

MIT License