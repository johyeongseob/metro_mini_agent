def action_generator(decision):
    return {
        "recheck": "Re-run inspection due to low confidence",
        "monitor": "No immediate action required",
        "inspect": "Schedule inspection",
        "repair": "Dispatch maintenance team"
    }[decision]