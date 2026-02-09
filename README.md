# Suspicious Login Detection

## Description
This project detects suspicious login attempts using Python, based on login time, location, and device type.  
It is fully self-contained and does not require any external libraries.

## How to Run
1. Open [suspicious_login_detection.py](./suspicious_login_detection.py) in Python 3.x
2. Run the script
3. Check the console output for flagged logins

##  Methodology
 Step 1: Input Parsing → Reads login data
 Step 2: Feature Extraction → Identifies unusual patterns
 Step 3: Anomaly Detection → Flags deviations
 Step 4: Output Classification → Labels Safe/Suspicious
 Step 5: Summary → Reports all flagged logins
   
## Example Output
# Suspicious_Login_Detection
Detect suspicious login attempts using Python, based on time, location, and device type
Suspicious Login Detection Output:

User 1: Normal (Login at 08:15 from India)

User 2: Suspicious (Login at 02:30 from USA)

User 3: Normal (Login at 09:00 from India)

User 4: Suspicious (Login at 23:45 from India)

User 5: Suspicious (Login at 03:15 from Russia)

Total logins: 5 | Suspicious: 3 (60.0%)

<img width="673" height="259" alt="image" src="https://github.com/user-attachments/assets/3fbeebce-8d10-48ee-b096-39bf6a30c9d0" />

