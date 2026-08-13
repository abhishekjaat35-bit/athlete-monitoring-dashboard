import pandas as pd


print("=" * 80)
print("                 ATHLETE MONITORING DASHBOARD")
print("=" * 80)


# ------------------------------------------
# Load Athlete Monitoring Data
# ------------------------------------------

data = pd.read_csv("athlete_monitoring_data.csv")

data["Date"] = pd.to_datetime(data["Date"])


# ------------------------------------------
# Wellness Score
# ------------------------------------------

def calculate_wellness_score(
    sleep,
    soreness,
    fatigue,
    stress,
    mood
):
    return (
        sleep
        + (6 - soreness)
        + (6 - fatigue)
        + (6 - stress)
        + mood
    )


# ------------------------------------------
# Readiness Classification
# ------------------------------------------

def classify_readiness(score):

    if score >= 85:
        return "High"

    elif score >= 70:
        return "Moderate"

    elif score >= 55:
        return "Low"

    else:
        return "Very Low"


# ------------------------------------------
# Training Load Classification
# ------------------------------------------

def classify_training_load(load):

    if load >= 700:
        return "Very High"

    elif load >= 500:
        return "High"

    elif load >= 300:
        return "Moderate"

    else:
        return "Low"


# ------------------------------------------
# Calculate Wellness
# ------------------------------------------

data["Wellness_Score"] = data.apply(
    lambda row: calculate_wellness_score(
        row["Sleep"],
        row["Soreness"],
        row["Fatigue"],
        row["Stress"],
        row["Mood"]
    ),
    axis=1
)


# ------------------------------------------
# Wellness Percentage
# ------------------------------------------

data["Wellness_Percent"] = (
    data["Wellness_Score"] / 25
) * 100


# ------------------------------------------
# Training Load Score
# ------------------------------------------

data["Load_Score"] = (
    100 - (data["Training_Load"] / 800 * 100)
).clip(lower=0)


# ------------------------------------------
# Combined Readiness Score
# ------------------------------------------

data["Readiness_Score"] = (
    data["Wellness_Percent"] * 0.70
    + data["Load_Score"] * 0.30
)


# ------------------------------------------
# Readiness Category
# ------------------------------------------

data["Readiness_Category"] = (
    data["Readiness_Score"]
    .apply(classify_readiness)
)


# ------------------------------------------
# Training Load Category
# ------------------------------------------

data["Training_Load_Category"] = (
    data["Training_Load"]
    .apply(classify_training_load)
)


# ------------------------------------------
# Monitoring Flag
# ------------------------------------------

def create_monitoring_flag(row):

    if (
        row["Readiness_Score"] < 55
        and row["Training_Load"] >= 700
    ):
        return "High Monitoring Priority"

    elif (
        row["Readiness_Score"] < 70
        and row["Training_Load"] >= 500
    ):
        return "Monitor Closely"

    elif row["Readiness_Score"] >= 85:
        return "Good Status"

    else:
        return "Normal Monitoring"


data["Monitoring_Flag"] = data.apply(
    create_monitoring_flag,
    axis=1
)


# ------------------------------------------
# Display Combined Data
# ------------------------------------------

print("\n" + "=" * 80)
print("COMBINED ATHLETE MONITORING DATA")
print("=" * 80)

display_columns = [
    "Athlete",
    "Date",
    "Training_Load",
    "Wellness_Score",
    "Readiness_Score",
    "Readiness_Category",
    "Training_Load_Category",
    "Monitoring_Flag"
]

print(
    data[display_columns].to_string(
        index=False,
        formatters={
            "Readiness_Score": "{:.1f}%".format
        }
    )
)


# ------------------------------------------
# Athlete Summary
# ------------------------------------------

athlete_summary = (
    data.groupby("Athlete")
    .agg(
        Sessions=("Athlete", "count"),
        Average_Wellness=("Wellness_Score", "mean"),
        Average_Load=("Training_Load", "mean"),
        Total_Load=("Training_Load", "sum"),
        Average_Readiness=("Readiness_Score", "mean"),
        Minimum_Readiness=("Readiness_Score", "min")
    )
    .reset_index()
)


print("\n" + "=" * 80)
print("ATHLETE MONITORING SUMMARY")
print("=" * 80)

print(
    athlete_summary.to_string(
        index=False,
        formatters={
            "Average_Wellness": "{:.1f}".format,
            "Average_Load": "{:.1f}".format,
            "Total_Load": "{:.0f}".format,
            "Average_Readiness": "{:.1f}%".format,
            "Minimum_Readiness": "{:.1f}%".format
        }
    )
)


# ------------------------------------------
# Athlete Ranking
# ------------------------------------------

ranking = athlete_summary.sort_values(
    "Average_Readiness",
    ascending=False
)


print("\n" + "=" * 80)
print("ATHLETE READINESS RANKING")
print("=" * 80)

for position, (_, athlete) in enumerate(
    ranking.iterrows(),
    start=1
):

    print(
        f"{position}. "
        f"{athlete['Athlete']:<10} "
        f"{athlete['Average_Readiness']:.1f}%"
    )


# ------------------------------------------
# Team Monitoring Summary
# ------------------------------------------

team_readiness = data["Readiness_Score"].mean()

team_wellness = data["Wellness_Score"].mean()

team_load = data["Training_Load"].mean()

total_team_load = data["Training_Load"].sum()


print("\n" + "=" * 80)
print("TEAM MONITORING SUMMARY")
print("=" * 80)

print(
    f"Average Wellness Score : "
    f"{team_wellness:.1f}/25"
)

print(
    f"Average Training Load  : "
    f"{team_load:.1f} AU"
)

print(
    f"Total Training Load    : "
    f"{total_team_load:.0f} AU"
)

print(
    f"Average Team Readiness : "
    f"{team_readiness:.1f}%"
)


# ------------------------------------------
# Monitoring Alerts
# ------------------------------------------

alerts = data[
    data["Monitoring_Flag"].isin(
        [
            "High Monitoring Priority",
            "Monitor Closely"
        ]
    )
]


print("\n" + "=" * 80)
print("MONITORING ALERTS")
print("=" * 80)

if alerts.empty:

    print("No monitoring alerts identified.")

else:

    print(
        alerts[
            [
                "Athlete",
                "Date",
                "Training_Load",
                "Readiness_Score",
                "Monitoring_Flag"
            ]
        ].to_string(
            index=False,
            formatters={
                "Readiness_Score": "{:.1f}%".format
            }
        )
    )


# ------------------------------------------
# Lowest Readiness
# ------------------------------------------

lowest = data.loc[
    data["Readiness_Score"].idxmin()
]


print("\n" + "=" * 80)
print("LOWEST READINESS OBSERVATION")
print("=" * 80)

print(f"Athlete   : {lowest['Athlete']}")
print(f"Date      : {lowest['Date'].date()}")
print(f"Training Load : {lowest['Training_Load']} AU")
print(f"Readiness : {lowest['Readiness_Score']:.1f}%")
print(f"Status    : {lowest['Monitoring_Flag']}")


# ------------------------------------------
# Export Results
# ------------------------------------------

data.to_csv(
    "athlete_monitoring_results.csv",
    index=False
)

athlete_summary.to_csv(
    "athlete_monitoring_summary.csv",
    index=False
)


# ------------------------------------------
# Final Output
# ------------------------------------------

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)

print("Files created:")
print("1. athlete_monitoring_results.csv")
print("2. athlete_monitoring_summary.csv")

print("\n" + "=" * 80)
print("MONITOR • ANALYZE • ADAPT • PERFORM")
print("=" * 80)