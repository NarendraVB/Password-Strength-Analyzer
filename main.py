from src.analyzer import analyze_password


password = input("Enter Password: ")

report = analyze_password(password)

print(f"""Password Analysis Report:
-------------------------""")
for key, value in report["report"].items():
    if isinstance(value, bool):
        value = "✔ Yes" if value else "✘ No"
    print(f"{key.replace('_', ' ').capitalize()}: {value}")
print(f"Score: {report['score']}")
print(f"Strength: {report['strength']}")
print(f"Entropy: {report['entropy']} bits")
print(f"Entropy Rating: {report['entropy_rating']}")
print(f"Estimated Crack Time: {report['Estimated Crack Time']}")
if "suggestions" in report:
    print("Suggestions:")
    for suggestion in report["suggestions"]:
        print(f"  - {suggestion}")
