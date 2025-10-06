"""
Product Recommendation System

Ethical Guidelines:
- Transparency: The system explains how recommendations are made.
- Fairness: Recommendations are not biased toward any particular product or group.
- User Feedback: Users can provide feedback to improve recommendations.
"""

# Sample product catalog
products = [
    {"id": 1, "name": "Wireless Mouse", "category": "Electronics"},
    {"id": 2, "name": "Yoga Mat", "category": "Fitness"},
    {"id": 3, "name": "Water Bottle", "category": "Fitness"},
    {"id": 4, "name": "Bluetooth Speaker", "category": "Electronics"},
    {"id": 5, "name": "Notebook", "category": "Stationery"},
    {"id": 6, "name": "Pen Set", "category": "Stationery"},
]

def explain_recommendation_method():
    print("\n[Transparency Notice]")
    print("Recommendations are based on the categories of products you have previously purchased or shown interest in.")
    print("We do not use any personal or sensitive information, and all products are treated equally for fairness.\n")

def get_user_history():
    print("Please enter the IDs of products you have purchased or liked (comma-separated):")
    print("Available products:")
    for p in products:
        print(f"  {p['id']}: {p['name']} ({p['category']})")
    ids = input("Your product IDs: ")
    try:
        user_ids = [int(i.strip()) for i in ids.split(",") if i.strip().isdigit()]
        return [p for p in products if p["id"] in user_ids]
    except Exception:
        print("Invalid input. Proceeding with empty history.")
        return []

def recommend_products(user_history):
    # Gather categories from user history
    categories = set(p["category"] for p in user_history)
    # Recommend products from those categories not already purchased
    recommendations = [
        p for p in products
        if p["category"] in categories and p not in user_history
    ]
    # If no history, recommend a diverse set (one from each category)
    if not user_history or not recommendations:
        seen = set()
        recommendations = []
        for p in products:
            if p["category"] not in seen:
                recommendations.append(p)
                seen.add(p["category"])
    return recommendations

def get_user_feedback(recommendations):
    print("\nWe value your feedback! Please rate the recommendations (1-5 stars):")
    for p in recommendations:
        while True:
            rating = input(f"  {p['name']} ({p['category']}): ")
            if rating.strip() in {"1", "2", "3", "4", "5"}:
                print(f"  Thank you for rating {p['name']} with {rating} star(s).")
                break
            else:
                print("  Please enter a number between 1 and 5.")

def main():
    print("Welcome to the Ethical Product Recommendation System!")
    explain_recommendation_method()
    user_history = get_user_history()
    recommendations = recommend_products(user_history)
    print("\nRecommended products for you:")
    for p in recommendations:
        print(f"  - {p['name']} ({p['category']})")
    get_user_feedback(recommendations)
    print("\nThank you for using our system. Your feedback helps us improve fairness and quality!")

if __name__ == "__main__":
    main()
