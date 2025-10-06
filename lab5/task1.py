# Simple script to collect user data

def collect_user_data():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    user_data = {
        "name": name,
        "age": age,
        "email": email
    }
    return user_data

if __name__ == "__main__":
    data = collect_user_data()
    print("Collected user data:", data)

    # --- Data Protection & Anonymization Comments ---
    # 1. To anonymize, do not store or transmit the 'name' and 'email' fields, or replace them with pseudonyms or hashes.
    # 2. Store data in encrypted form if saving to disk or database.
    # 3. Never share raw user data; remove or mask personally identifiable information (PII) before analysis or sharing.
    # 4. Use secure channels (e.g., HTTPS) if transmitting data over a network.
    # 5. Consider asking for user consent before collecting or processing personal data.
