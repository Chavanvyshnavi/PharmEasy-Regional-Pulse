#Presentation Storyline — PharmEasy Regional Pulse

#Executive Audience — Situation–Complication–Resolution

#Situation

Guntur sales increased from ₹62,442.27 in April 2026 to ₹138,738.93 in May 2026, representing a +122.19% month-on-month increase. Sales then declined to ₹99,745.18 in June, which is 28.11% below May.

#Complication

The May increase is significant and requires investigation. The dataset shows the size and timing of the movement, but it does not establish the external business cause behind it. Therefore, the May level should not automatically be treated as a sustained baseline.

#Resolution

Review Guntur's category-level sales and distinct-order activity across April, May and June. Check whether the May increase was concentrated in a particular category or reflected more broadly across the region. Then validate the operational explanation with additional business evidence before making changes to ongoing plans.


#Regional Manager Audience — Overview–Category–Detail

#Overview

Guntur sales increased by +122.19% from April to May, rising from ₹62,442.27 to ₹138,738.93. June sales were ₹99,745.18, showing a partial pullback from the May level.

#Category

The category view shows which of the six medicine categories contributes most to sales and whether the movement is concentrated in a particular category. Across the full dataset, Medical Devices is the largest category by sales at ₹1,036,727.24.

#Detail

The supporting evidence comes from the cleaned order data and the Part 2 SQLite database. Sales, profit and distinct order counts are aggregated by region and month. The dashboard allows the regional manager to filter Guntur and inspect its April, May and June results before deciding on operational follow-up.

 Stakeholder Q&A

#Question 1 — Why should I believe this number?

 direct acknowledgement

That is a fair concern because a large month-on-month movement should be traceable to the underlying records.

#Verified vs. not verified

**Verified:** Guntur sales were ₹62,442.27 in April and ₹138,738.93 in May, producing a +122.19% increase. The dashboard calculates order counts using distinct order_id values.

**Not verified:** An independent reconciliation against an external finance or source-order system.

#What would resolve the uncertainty and by when?

Reconcile Guntur's April and May sales against the source order or finance system, including order IDs and sales amounts. This should be completed within one business day after the source extract is available.


#Question 2 — What if an alternative explanation is driving this increase?

#Direct acknowledgement

That is possible because the dataset identifies the movement but does not establish why it happened.

#Verified vs. not verified

**Verified:** Guntur sales increased 122.19% from April to May and then declined 28.11% from May to June.

**Not verified:** Whether the increase was caused by a promotion, pricing change, one-off order activity, category mix, seasonality or another external factor.

##What would resolve the uncertainty and by when?

Compare Guntur's April–June sales and order composition with promotion, pricing, inventory and operational records. This should be reviewed within one business day after the relevant records are available.


#Question 3 — What would change your recommendation?

#Direct acknowledgement

The recommendation would change if the May increase were shown to be a data-quality issue or a one-off event that should not influence ongoing operations.

#Verified vs. not verified

**Verified:** The cleaned dataset records the April-to-May increase and the May-to-June pullback.

**Not verified:** Whether the May level represents a repeatable demand pattern.

#What would resolve the uncertainty and by when?

Validate the affected orders, category mix and known commercial events, then reassess the recommendation within one business day of receiving the additional evidence.



#Question 4 — What did you not check?

#Direct acknowledgement

The current analysis does not establish the external business cause of the Guntur movement.

##Verified vs. not verified

**Verified:** Regional sales, profit, distinct order counts and category-level results are available in the cleaned dataset.

**Not verified:** External factors such as promotions, stock availability, pricing changes, customer acquisition campaigns or competitor activity.

#What would resolve the uncertainty and by when?

Add the relevant operational and commercial records and compare them with the April–June order timeline. This should be completed within one business day after those records are supplied.