import pandas as pd
import json
import os

def compute_percentage_change_v1(current, previous):

    if previous == 0:
        return 0

    return ((current - previous) / previous) * 100


def flag_significant_regions_v1(changes, threshold=8):

    flagged = []

    for region, change in changes.items():

        if abs(change) > threshold:
            flagged.append(region)

    return flagged


def save_state_v1(month_summary, path):

    with open(path, "w") as f:
        json.dump(month_summary, f, indent=4)

    print(f"State saved to {path}")


def load_previous_state_v1(path):

    if not os.path.exists(path):
        return {}

    with open(path, "r") as f:
        return json.load(f)


df = pd.read_csv("region_month_sales.csv")

print("\n REGION MONTH SALES ")
print(df)

pivot = df.pivot(
    index="region",
    columns="month",
    values="total_sales"
)

print("\n SALES BY REGION AND MONTH ")
print(pivot)


april_may_changes = {}

for region in pivot.index:

    april_sales = pivot.loc[region, "2026-04"]
    may_sales = pivot.loc[region, "2026-05"]

    change = compute_percentage_change_v1(
        may_sales,
        april_sales
    )

    april_may_changes[region] = round(change, 2)


print("\n APRIL → MAY ")

for region, change in april_may_changes.items():

    print(
        f"{region}: {change}%"
    )


april_may_flags = flag_significant_regions_v1(
    april_may_changes,
    threshold=8
)

print("\nFlagged regions — April → May:")
print(april_may_flags)

may_june_changes = {}

for region in pivot.index:

    may_sales = pivot.loc[region, "2026-05"]
    june_sales = pivot.loc[region, "2026-06"]

    change = compute_percentage_change_v1(
        june_sales,
        may_sales
    )

    may_june_changes[region] = round(change, 2)


print("\n MAY → JUNE ")

for region, change in may_june_changes.items():

    print(
        f"{region}: {change}%"
    )

may_june_flags = flag_significant_regions_v1(
    may_june_changes,
    threshold=8
)

print("\nFlagged regions — May → June:")
print(may_june_flags)


april_summary = {}

for region in pivot.index:

    april_summary[region] = float(
        pivot.loc[region, "2026-04"]
    )


save_state_v1(
    april_summary,
    "state.json"
)


loaded_state = load_previous_state_v1(
    "state.json"
)

print("\n LOADED STATE")
print(loaded_state)

print("\n")
print("PART 2 METRICS ENGINE COMPLETED")
print("")

print("\nApril → May flagged:")
print(april_may_flags)

print("\nMay → June flagged:")
print(may_june_flags)