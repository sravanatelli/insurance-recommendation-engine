def generate_explanations(products, profile):
    explained = []

    for product in products:
        reason = ""
        if product == "Family Health Insurance":
            reason = "You have dependents and need health coverage."
        elif product == "Term Life Insurance":
            reason = "Middle-aged individuals should secure their family’s financial future."
        elif product == "Retirement Pension Plan":
            reason = "Seniors should plan for retirement income."
        elif product == "Wealth Builder Policy":
            reason = "High income indicates suitability for long-term investment insurance."

        explained.append({"product": product, "reason": reason})

    return explained
