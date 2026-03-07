REQUIRED_FIELDS = [
    "sample_size",
    "study_design",
    "phase",
    "primary_endpoint",
    "efficacy_results",
    "safety_results"
]


def validate_record(record):
    """Validate that required fields exist and contain source_text."""
    if "error" in record:
        return False

    for field in REQUIRED_FIELDS:
        if field not in record:
            return False

        value = record[field]
        if value is None:
            continue

        if not isinstance(value, dict):
            return False

        if "source_text" not in value:
            return False

    return True
