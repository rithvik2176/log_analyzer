import re
import requests

LOG_PATH = "/var/log/auth.log"


def get_location(ip):
    
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data["status"] == "success":
            return f"{data['city']}, {data['country']}"
        else:
            return "private/Local network"

    except requests.exceptions.RequestException:
        return "Location unavailable."

    pass


def parse_log(filepath):
    failed_attempts = []
    pattern = r'(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}).*Failed password.*from (\d+\.\d+\.\d+\.\d+)'
    with open(filepath, 'r') as f:
        for line in f:
            match = re.search(pattern,line)
            if match:
                timestamp = match.group(1)
                ip = match.group(2)
                location = get_location(ip)
                failed_attempts.append({
                    'timestamp': timestamp,
                    'ip':ip,
                    'location': location
                })



    return failed_attempts
if __name__ == "__main__":
    results = parse_log("fakelog.txt")
    for r in results:
        print(r)   