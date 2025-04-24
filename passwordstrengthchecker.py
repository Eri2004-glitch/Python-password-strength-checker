import re
def check_password(password):
    score = 0
    feedback = []

#To check the length of the password.....
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short. Use at least 8 characters.")

#To check for presence of uppercase......
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

#To check for presence of lowercase......
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

#To check for presence of numbers........
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

#To check for special characters....
    if re.search(r"[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

#To check for strong length
    if len(password) >= 12:
        score += 1  # Bonus point for length

#To check for strength rating
    if score <= 2:
        strength = "Weak"
    elif 3 <= score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback


# --- Main Program ---

user_password = input("Enter a password to check: ")
strength, suggestions = check_password(user_password)

print(f"\nPassword Strength: {strength}")
if suggestions:
    print("Suggestions to improve:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
else:
    print("Great job! Your password looks strong.")
