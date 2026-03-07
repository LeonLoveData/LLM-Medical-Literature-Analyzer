REQUIRED_FIELDS = ["sample_size","study_design","phase","primary_endpoint","efficacy_results","safety_results"]

def validate_record(r):
    if "error" in r:
        return False
    for f in REQUIRED_FIELDS:
        if f not in r:
            return False
        v = r[f]
        if v is None:
            continue
        if "source_text" not in v:
            return False
    return True
