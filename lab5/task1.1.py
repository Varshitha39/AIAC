
def encrypt_email(email):
    # Simple "encryption": reverse the email and shift each character by 1
    return ''.join(chr(ord(c) + 1) for c in email[::-1])

def collect_user_data():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    encrypted_email = encrypt_email(email)
    user_data = {
        "name": name,
        "age": age,
        "email": encrypted_email
    }
    return user_data

if __name__ == "__main__":
    data = collect_user_data()
    print("Collected user data (with encrypted email):", data)
