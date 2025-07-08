def get_customer_profile(data):
    profile = {}
    age = data.get("age", 0)

    if age < 30:
        profile["life_stage"] = "young_adult"
    elif age < 50:
        profile["life_stage"] = "middle_aged"
    else:
        profile["life_stage"] = "senior"

    profile["risk"] = "high" if data.get("health_condition") == "poor" else "moderate"
    profile["has_children"] = data.get("children", 0) > 0
    profile["income"] = data.get("income", 0)
    profile["employment"] = data.get("employment", "unknown")

    return profile
