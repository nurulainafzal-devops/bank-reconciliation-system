from fuzzywuzzy import fuzz

def is_match(bank_txn, internal_txn, amount_tolerance=5, date_match=True):
    
    # 1. Amount check (with tolerance)
    amount_ok = abs(bank_txn["Amount"] - internal_txn["Amount"]) <= amount_tolerance

    # 2. Description similarity
    desc_score = fuzz.ratio(
        bank_txn["Description"].lower(),
        internal_txn["Description"].lower()
    )

    desc_ok = desc_score > 70  # 70% similarity threshold

    # 3. Date check (simple match)
    date_ok = True
    if date_match:
        date_ok = bank_txn["Date"] == internal_txn["Date"]

    # FINAL DECISION
    return amount_ok and desc_ok and date_ok



def reconcile(bank_data, internal_data):

    matched = []
    unmatched = []

    for b in bank_data:
        found = False

        for i in internal_data:
            if is_match(b, i):
                matched.append((b, i))
                found = True
                break

        if not found:
            unmatched.append(b)

    return {
        "matched": matched,
        "unmatched": unmatched
    }
