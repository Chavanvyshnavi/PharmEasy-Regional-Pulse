import json
from datetime import datetime
import uuid


ALLOWED_DECISIONS = {
    "approve",
    "edit",
    "reject"
}


def review_gate_v1(report, decision, reviewer_note=""):

    # Check whether decision is valid
    if decision not in ALLOWED_DECISIONS:
        raise ValueError(
            "Decision must be approve, edit, or reject."
        )

    run_id = str(uuid.uuid4())

    # Determine whether downstream use is allowed
    if decision == "approve":
        downstream_allowed = True

    elif decision == "edit":
        downstream_allowed = False

    else:
        downstream_allowed = False

    # Create updated report
    updated_report = report.copy()

    updated_report["decision"] = decision
    updated_report["reviewer_note"] = reviewer_note
    updated_report["downstream_use_allowed"] = downstream_allowed

    # Region for audit log
    region = updated_report.get(
        "region",
        "Guntur"
    )

    # Create audit record
    audit_record = {
        "timestamp": datetime.now().isoformat(),
        "run_id": run_id,
        "region": region,
        "decision": decision,
        "reviewer_note": reviewer_note
    }

    # Append audit record
    with open("audit_log.jsonl", "a") as f:
        f.write(
            json.dumps(audit_record) + "\n"
        )

    return updated_report

sample_report = {
    "region": "Guntur",
    "Context": "Guntur sales increased from April to May.",
    "Insight": "Sales increased by 122.19%.",
    "Implication": "The movement requires review."
}


print("\n")
print("TEST 1 — APPROVE")
print("")

approve_result = review_gate_v1(
    sample_report,
    "approve",
    "Numbers verified; approved."
)

print(approve_result)


print("\n")
print("TEST 2 — EDIT")
print("")

edit_result = review_gate_v1(
    sample_report,
    "edit",
    "Clarify the implication."
)

print(edit_result)


print("\n")
print("TEST 3 — REJECT")
print("")

reject_result = review_gate_v1(
    sample_report,
    "reject",
    "Evidence requires further review."
)

print(reject_result)


print("\n")
print("REVIEW GATE TESTING COMPLETED")
print("")