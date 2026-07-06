import math
def analyze_password(password):
            
            COMMON_PASSWORDS = [
            "password",
            "password123",
            "admin",
            "welcome",
            "qwerty",
            "letmein",
            "123456",
            "abc123",
            ]
            password_lower = password.lower()

            is_common = password_lower in COMMON_PASSWORDS


            report = {
                "length": len(password),
                "has_uppercase": any(char.isupper() for char in password),
                "has_lowercase": any(char.islower() for char in password),
                "has_numbers": any(char.isdigit() for char in password),
                "has_symbols": any(not char.isalnum() for char in password),
                "is_common_password": is_common
            }
    

            score = 0

            if report["length"] >= 12:
                score += 2

            if report["has_uppercase"]:
                score += 1

            if report["has_lowercase"]:
                score += 1

            if report["has_numbers"]:
                score += 1

            if report["has_symbols"]:
                score += 1
            if report["is_common_password"]:
                score -= 2
            score = max(0, score)


            character_set = 0

            if report["has_lowercase"]:
                character_set += 26

            if report["has_uppercase"]:
                character_set += 26

            if report["has_numbers"]:
                character_set += 10

            if report["has_symbols"]:
                character_set += 32

            if character_set > 0:
                entropy = report["length"] * math.log2(character_set)
            else:
                entropy = 0
            if entropy < 40:
                entropy_rating = "Very Weak"
            elif entropy < 60:
                entropy_rating = "Weak"
            elif entropy < 80:
                entropy_rating = "Good"
            else:
                entropy_rating = "Excellent"

            if score <= 2:
                strength = "Weak"
            elif score <= 4:
                strength = "Medium"
            else:
                strength = "Strong"


            
            return {"report": report,"score": score, "strength": strength, "entropy": entropy, "entropy_rating": entropy_rating}
