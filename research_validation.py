import json

with open("Kinyoubi_India_Campaign.json", "r") as file:
    data = json.load(file)

errors = 0
warnings = 0

for lead in data["leads"]:

    if not lead.get("company"):
        print("ERROR:", lead["id"], "Missing company")
        errors += 1

    if not lead.get("website"):
        print("ERROR:", lead["id"], "Missing website")
        errors += 1

    if not lead.get("company_source_ids"):
        print("ERROR:", lead["id"], "Missing company source")
        errors += 1

    if not lead.get("scores"):
        print("ERROR:", lead["id"], "Missing scores")
        errors += 1

    if lead.get("priority_score") is None:
        print("ERROR:", lead["id"], "Missing priority score")
        errors += 1

    if not lead.get("decision_maker"):
        print("REVIEW:", lead["id"], "Missing decision maker")
        warnings += 1
print("\nLeads with missing contact information:")

for lead in data["leads"]:
    contact = lead.get("contact", {})

    if not contact.get("email") and not contact.get("route"):
        print("REVIEW:", lead["id"], "Missing contact route")
        
print("Research validation completed")
print("Errors:", errors)
print("Warnings:", warnings)

print("\n--- Leads with Missing Websites ---")
for lead in data["leads"]:
    if not lead.get("website"):
          print("REVIEW:", lead["id"], "Missing website")
    warnings += 1
