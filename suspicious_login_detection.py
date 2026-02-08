# Suspicious Login Detection

login_data = [
    {"user_id": 1, "login_time": "08:15", "location": "India", "device": "Laptop"},
    {"user_id": 2, "login_time": "02:30", "location": "USA", "device": "Mobile"},
    {"user_id": 3, "login_time": "09:00", "location": "India", "device": "Mobile"},
    {"user_id": 4, "login_time": "23:45", "location": "India", "device": "Laptop"},
    {"user_id": 5, "login_time": "03:15", "location": "Russia", "device": "Desktop"},
]

def flag_login(time_str, location):
    hour = int(time_str.split(":")[0])
    if hour < 6 or hour > 22 or location not in ["India"]:
        return "Suspicious"
    return "Normal"

suspicious_count = 0
total = len(login_data)

print("Suspicious Login Detection Output:\n")
for login in login_data:
    status = flag_login(login["login_time"], login["location"])
    print(f"User {login['user_id']}: {status} (Login at {login['login_time']} from {login['location']})")
    if status == "Suspicious":
        suspicious_count += 1

print(f"\nTotal logins: {total} | Suspicious: {suspicious_count} ({(suspicious_count/total)*100:.1f}%)")
