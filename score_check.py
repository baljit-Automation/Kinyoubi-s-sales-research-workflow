import json

with open("Kinyoubi_India_Campaign.json", "r") as file:
    data = json.load(file)

for lead in data["leads"]:
    scores = lead["scores"]
    calculated = sum(scores.values())

    if calculated != lead["priority_score"]:
        print("Score mismatch:", lead["id"])     
print("Score check completed")