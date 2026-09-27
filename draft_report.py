import pandas as pd

def draft_report_v1(flagged_regions, metrics):

    report = {}

    for region in flagged_regions:

        april_sales = metrics[region]["april_sales"]
        may_sales = metrics[region]["may_sales"]
        june_sales = metrics[region]["june_sales"]

        april_may_change = metrics[region]["april_may_change"]
        may_june_change = metrics[region]["may_june_change"]

        context = (
            f"{region} recorded sales of ₹{april_sales:,.2f} "
            f"in April 2026 and ₹{may_sales:,.2f} "
            f"in May 2026."
        )

        insight = (
            f"Sales changed by {april_may_change:.2f}% "
            f"from April to May. "
            f"From May to June, sales changed by "
            f"{may_june_change:.2f}%."
        )

        implication = (
            f"The {region} movement should be reviewed using "
            f"the monthly sales trend before deciding on any "
            f"operational action."
        )

        report[region] = {
            "Context": context,
            "Insight": insight,
            "Implication": implication
        }

    return report


df = pd.read_csv("region_month_sales.csv")


# Convert data into region × month format
pivot = df.pivot(
    index="region",
    columns="month",
    values="total_sales"
)


metrics = {}

for region in pivot.index:

    april_sales = pivot.loc[region, "2026-04"]
    may_sales = pivot.loc[region, "2026-05"]
    june_sales = pivot.loc[region, "2026-06"]

    april_may_change = (
        (may_sales - april_sales) / april_sales
    ) * 100

    may_june_change = (
        (june_sales - may_sales) / may_sales
    ) * 100

    metrics[region] = {
        "april_sales": april_sales,
        "may_sales": may_sales,
        "june_sales": june_sales,
        "april_may_change": april_may_change,
        "may_june_change": may_june_change
    }

april_may_flags = [
    "Bengaluru",
    "Guntur",
    "Hyderabad",
    "Karimnagar",
    "Tirupati",
    "Visakhapatnam",
    "Warangal"
]

may_june_flags = [
    "Guntur",
    "Hyderabad",
    "Karimnagar",
    "Tirupati",
    "Vijayawada",
    "Visakhapatnam",
    "Warangal"
]

flagged_regions = sorted(
    set(april_may_flags + may_june_flags)
)



report = draft_report_v1(
    flagged_regions,
    metrics
)


print("\n")
print("PART 3.1 — CII REPORT")
print("")

for region, block in report.items():

    print(f"\n### {region}")

    print("Context:")
    print(block["Context"])

    print("\nInsight:")
    print(block["Insight"])

    print("\nImplication:")
    print(block["Implication"])

print("\n")
print("CII REPORT COMPLETED")
print("")