# reporter.py

def print_report(alerts):

    print("=" * 40)
    print("       SSH LOG ANALYSIS REPORT")
    print("=" * 40)

    if len(alerts) == 0:
        print("No suspicious activity detected.")
        return

    print("\n ALERTS — Brute Force Detected")
    print("-" * 40)

    for alert in alerts:
        print(f"[!] IP Address  : {alert['ip']}")
        print(f"    Location    : {alert['location']}")
        print(f"    Attempts    : {alert['count']}")
        print(f"    First Seen  : {alert['first_seen']}")
        print("-" * 40)

    print(f"\nTotal alerts: {len(alerts)}")


if __name__ == "__main__":
    fake_alerts = [
        {'ip': '203.0.113.42', 'count': 4, 'location': 'Berlin, Germany', 'first_seen': 'Dec 10 03:12:44'}
    ]
    print_report(fake_alerts)