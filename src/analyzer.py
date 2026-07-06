import math
from src.utils import format_time
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
            is_common = False

            for common in COMMON_PASSWORDS:

                if common in password.lower():
                    is_common = True
                    break


            report = {
                "length": len(password),
                "Uppercase": any(char.isupper() for char in password),
                "Lowercase": any(char.islower() for char in password),
                "Numbers": any(char.isdigit() for char in password),
                "Symbols": any(not char.isalnum() for char in password),
                "is_common_password": is_common
            }
    

            score = 0

            if report["length"] >= 12:
                score += 2

            if report["Uppercase"]:
                score += 1

            if report["Lowercase"]:
                score += 1

            if report["Numbers"]:
                score += 1

            if report["Symbols"]:
                score += 1
            if report["is_common_password"]:
                score -= 2
            score = max(0, score)

            if score <= 2:
                strength = "Weak"
            elif score <= 4:
                strength = "Medium"
            else:
                strength = "Strong"


            character_set = 0

            if report["Lowercase"]:
                character_set += 26

            if report["Uppercase"]:
                character_set += 26

            if report["Numbers"]:
                character_set += 10

            if report["Symbols"]:
                character_set += 32

            if character_set > 0:
                entropy = round(report["length"] * math.log2(character_set), 2)
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


            search_space = character_set ** report["length"] if character_set > 0 else 0

            average_guesses = search_space / 2

            guesses_per_second = 100_000_000_000  

            seconds = format_time(average_guesses / guesses_per_second if guesses_per_second else 0)


            suggestions = []
            if report["length"] < 12:
                suggestions.append("Increase password length to at least 12 characters.")

            if not report["Uppercase"]:
                suggestions.append("Add uppercase letters.")

            if not report["Lowercase"]:
                suggestions.append("Add lowercase letters.")

            if not report["Numbers"]:
                suggestions.append("Add numbers.")

            if not report["Symbols"]:
                suggestions.append("Add symbols.")

            if report["is_common_password"]:
                suggestions.append("Avoid common passwords.")


            if suggestions:
                return {"report": report, "score": score, "strength": strength, "entropy": entropy, "entropy_rating": entropy_rating,"Estimated Crack Time": seconds, "suggestions": suggestions}
            else:
                return {"report": report, "score": score, "strength": strength, "entropy": entropy, "entropy_rating": entropy_rating, "Estimated Crack Time": seconds, "suggestions": ["No suggestions. Your password meets the current policy."]}