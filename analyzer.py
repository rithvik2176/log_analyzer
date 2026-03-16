from collections import Counter

THRESHOLD = 4

def analyze(failed_attempts):
    alerts = []
    ip_list = [attempt['ip'] for attempt in failed_attempts]
    ip_counts = Counter(ip_list)

    for ip, count in ip_counts.items():
        if count >= THRESHOLD:
            first_attempt = None
            for attempt in failed_attempts:
                if attempt['ip'] == ip:
                    first_attempt = attempt
                    break

            alerts.append({
                'ip': ip,
                'count': count,
                'location': first_attempt['location'],
                'first_seen': first_attempt['timestamp']
            })

    return alerts

if __name__ == "__main__":
    fake_attempts = [
        {'timestamp': 'Dec 10 03:12:44', 'ip': '203.0.113.42', 'location': 'Berlin, Germany'},
        {'timestamp': 'Dec 10 03:13:01', 'ip': '203.0.113.42', 'location': 'Berlin, Germany'},
        {'timestamp': 'Dec 10 03:13:20', 'ip': '203.0.113.42', 'location': 'Berlin, Germany'},
        {'timestamp': 'Dec 10 03:13:35', 'ip': '203.0.113.42', 'location': 'Berlin, Germany'},
        {'timestamp': 'Dec 10 03:14:00', 'ip': '198.51.100.7', 'location': 'Tokyo, Japan'},
    ]

    results = analyze(fake_attempts)
    for r in results:
        print(r)