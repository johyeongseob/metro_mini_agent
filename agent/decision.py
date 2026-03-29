def decision_engine(defect):
    severity = defect["severity"]
    confidence = defect["confidence"]

    if confidence < 0.5:
        return "recheck"

    if severity < 0.3:
        return "monitor"
    elif severity < 0.7:
        return "inspect"
    else:
        return "repair"


def compute_risk(defect):
    return round(defect["severity"] * defect["confidence"], 3)