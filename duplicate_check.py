import json

with open("Kinyoubi_India_Campaign.json", "r") as file:
    data = json.load(file)

companies = set()

for lead in data["leads"]:
    company = lead["company"].strip().lower()

    if company in companies:
        print("Duplicate:", lead["company"])
    else:
        companies.add(company)
print("Duplicate check completed")