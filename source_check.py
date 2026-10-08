import json

with open("Kinyoubi_India_Campaign.json", "r") as file:
    data = json.load(file)

sources = {source["id"]: source for source in data["sources"]}

for lead in data["leads"]:
    for source_id in lead.get("company_source_ids", []):
        if source_id in sources:
            print(lead["id"], "→", sources[source_id]["url"])
        else:
            print("Missing source:", source_id)
print("Source check completed")