import re
from email import policy
from email.parser import BytesParser

file_path = "Sample-Emails/suspicious_email.eml"

with open(file_path, "rb") as f:
    msg = BytesParser(policy=policy.default).parse(f)

print("\n===== IOC ANALYSIS REPORT =====\n")

# Extract sender
print("Sender:", msg.get("From"))

# Extract Return-Path
print("Return-Path:", msg.get("Return-Path"))

# Extract subject
print("Subject:", msg.get("Subject"))

# Extract email body
body = msg.get_body(preferencelist=("plain",))

if body:
    content = body.get_content()
else:
    content = ""

# Extract URLs
urls = re.findall(r'https?://[^\s<>"]+', content)

print("\nExtracted URLs:")

for url in urls:
    print(url)

# Extract IP addresses
ips = re.findall(
    r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
    str(msg.get_all("Received", []))
)

print("\nSource IP indicators:")

for ip in ips:
    print(ip)

print("\n===== INVESTIGATION COMPLETED =====")
