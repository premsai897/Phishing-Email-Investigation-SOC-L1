from email import policy
from email.parser import BytesParser

file_path = "Sample-Emails/suspicious_email.eml"

with open(file_path, "rb") as f:
    msg = BytesParser(policy=policy.default).parse(f)

headers = [
    "From",
    "To",
    "Subject",
    "Date",
    "Message-ID",
    "Return-Path",
    "Received",
    "Authentication-Results"
]

print("\n===== PHISHING EMAIL HEADER ANALYSIS =====\n")

for header in headers:
    values = msg.get_all(header, [])

    for value in values:
        print(f"{header}: {value}")

print("\n===== ANALYSIS COMPLETED =====")
