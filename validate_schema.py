import json
from jsonschema import Draft7Validator

with open("Kinyoubi_India_Campaign.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("Kinyoubi_India_Campaign_schema.json", "r", encoding="utf-8") as f:
    schema = json.load(f)

validator = Draft7Validator(schema)
errors = list(validator.iter_errors(data))

if not errors:
    print("✅ JSON is valid according to the Schema")
else:
    print(f"❌ Found {len(errors)} validation errors:")

    for error in errors[:20]:
        path = ".".join(str(x) for x in error.absolute_path)
        print(f"- Field: {path}")
        print(f"  Error: {error.message}")