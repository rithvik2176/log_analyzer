A Python tool that analyzes SSH auth logs to detect brute force attacks, 
geolocate attackers, and use AI to identify coordinated attack patterns.
Built as a cybersecurity learning project.

## Requirements
- Python 3.x
- requests
- groq
- python-dotenv

## Sample Output
========================================
       SSH LOG ANALYSIS REPORT
========================================

🚨 ALERTS — Brute Force Detected
----------------------------------------
[!] IP Address  : 203.0.113.42
    Location    : Berlin, Germany
    Attempts    : 4
    First Seen  : Dec 10 03:12:44
----------------------------------------

🤖 AI Pattern Analysis:
Two IPs from Germany attacked within 30 seconds suggesting 
a coordinated automated attack...



