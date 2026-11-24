import re

file_path = "Sample-Emails/suspicious_email.eml"

with open(file_path, "r") as f:
    content = f.read()

urls = re.findall(
    r'https?://[^\s<>"]+',
    content
)

print("\n===== PHISHING URL ANALYSIS =====")

for url in urls:
    print("Extracted URL:", url)

print("\n===== ANALYSIS COMPLETED =====")
