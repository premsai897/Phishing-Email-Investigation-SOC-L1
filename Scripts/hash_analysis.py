import hashlib

file_path = "Evidence/sample.txt"

sha256 = hashlib.sha256()

with open(file_path, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
        sha256.update(chunk)

print("\n===== FILE HASH ANALYSIS =====")
print("File:", file_path)
print("SHA-256:", sha256.hexdigest())
print("Algorithm: SHA-256")
print("Status: Hash generated successfully")
print("===== ANALYSIS COMPLETED =====")
