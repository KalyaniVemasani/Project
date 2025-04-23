import requests

base_url = "http://169.254.169.254/latest/meta-data/"

fields = [
    "instance-id",
    "instance-type",
    "ami-id",
    "local-ipv4",
    "public-ipv4",
    "hostname",
    "local-hostname",
    "public-hostname",
    "security-groups",
    "mac"
]

print(" EC2 Instance Metadata:\n")

for field in fields:
    try:
        response = requests.get(base_url + field, timeout=2)
        response.raise_for_status()
        print(f"{field}: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"{field}:  Error fetching data - {e}")

