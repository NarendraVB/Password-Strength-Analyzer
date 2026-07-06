from src.analyzer import analyze_password


password = input("Enter Password: ")

report = analyze_password(password)

print(report)