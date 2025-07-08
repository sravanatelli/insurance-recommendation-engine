from src.profiling import get_customer_profile
from src.recommend_engine import recommend_products
from src.explain import generate_explanations

if __name__ == "__main__":
    customer = {
        "age": 32,
        "marital_status": "married",
        "children": 2,
        "employment": "salaried",
        "income": 900000,
        "health_condition": "average"
    }

    profile = get_customer_profile(customer)
    recommendations = recommend_products(profile)
    explained = generate_explanations(recommendations, profile)

    for rec in explained:
        print(f"{rec['product']} → {rec['reason']}")
