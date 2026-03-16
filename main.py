# main.py
from parser import parse_log
from analyzer import analyze
from reporter import print_report
from llm_response import find_patterns



def main():
    # Step 1 — parse the log file
    failed_attempts = parse_log("/var/log/auth.log")

    # Step 2 — analyze the results
    alerts = analyze(failed_attempts)

    # Step 3 — print the report
    print_report(alerts)

    #step4
    print(find_patterns(alerts))

if __name__ == "__main__":
    main()