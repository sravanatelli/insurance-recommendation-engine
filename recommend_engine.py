def recommend_products(profile):
    recommendations = []

    if profile["has_children"]:
        recommendations.append("Family Health Insurance")

    if profile["life_stage"] == "middle_aged":
        recommendations.append("Term Life Insurance")

    if profile["life_stage"] == "senior":
        recommendations.append("Retirement Pension Plan")

    if profile["income"] > 800000:
        recommendations.append("Wealth Builder Policy")

    return recommendations
