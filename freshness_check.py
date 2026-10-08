import json
from datetime import date

with open("Kinyoubi_India_Campaign.json", "r") as file:
    data = json.load(file)

today = date.today()

for source in data["sources"]:
    checked_on = source.get("checked_on")

    if not checked_on:
        print("REVIEW:", source["id"], "| Missing check date")
        continue

    checked = date.fromisoformat(checked_on)
    age = (today - checked).days

    if "role" in source.get("supports", []) or "contact" in source.get("supports", []):
        limit = 30
    else:
        limit = 90

    if age > limit:
        print("REVIEW:", source["id"], "| Age:", age, "days")