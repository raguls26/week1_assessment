import csv
import json
import os
import requests 
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()
api_key = os.getenv("API_KEY")

# 1. File I/O: CSV to JSON and High Earners CSV
input_file = "data/employees.csv"
json_output = "data/employees.json"
high_earners_output = "data/high_earners.csv"

employees = []
high_earners = []

with open(input_file, mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["salary"] = float(row["salary"])
        employees.append(row)
        if row["salary"] > 50000:
            high_earners.append(row)

# Save to JSON
with open(json_output, mode="w", encoding="utf-8") as f:
    json.dump(employees, f, indent=4)

# Save High Earners to CSV
with open(high_earners_output, mode="w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=employees[0].keys())
    writer.writeheader()
    writer.writerows(high_earners)

print(f"Rows read: {len(employees)} High earners: {len(high_earners)}")

# 2. REST API Calls with Timeout and Error Handling
base_url = "https://jsonplaceholder.typicode.com"

# Fetch first 3 users
try:
    response = requests.get(f"{base_url}/users", timeout=5)
    response.raise_for_status()
    users_data = response.json()
    
    for user in users_data[:3]:
        print(f"{user['id']} {user['name']} {user['email']}")
        
    # Parse nested JSON field with .get() and save
    parsed_users = []
    for u in users_data:
        parsed_users.append({
            "id": u.get("id"),
            "name": u.get("name"),
            "city": u.get("address", {}).get("city"),
            "company": u.get("company", {}).get("name")
        })
        
    with open("data/users.json", "w", encoding="utf-8") as f:
        json.dump(parsed_users, f, indent=4)

except requests.exceptions.Timeout:
    print("Request timed out.")
except requests.exceptions.ConnectionError:
    print("Connection error occurred.")
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")

# Demonstrate handling 404
try:
    res_404 = requests.get(f"{base_url}/users/9999", timeout=5)
    if res_404.status_code == 404:
        print("/users/9999 > 404 Not found")
    else:
        res_404.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching 404 endpoint: {e}")