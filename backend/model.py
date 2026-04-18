def predict_risk(age, hr, ox):
    if hr > 120 or ox < 90:
        return "HIGH"
    elif hr > 100:
        return "MEDIUM"
    else:
        return "LOW"