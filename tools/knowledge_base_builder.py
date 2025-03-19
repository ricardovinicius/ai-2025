import json

class KnowledgeBaseBuilder:
    def __init__(self):
        self.knowledge_base = []

    def add_rule(self, conditions: dict, consequence: dict):
        """Add a rule to the knowledge base."""
        self.knowledge_base.append({
            "conditions": conditions,
            "consequence": consequence
        })

    def build_from_cli(self):
        """Build knowledge base interactively from command line."""
        while True:
            print("\nAdding new rule:")
            conditions = {}
            while True:
                condition = input("Enter condition (field:value) or press Enter to finish conditions: ")
                if not condition:
                    break
                try:
                    field, value = condition.split(":")
                    conditions[field.strip()] = value.strip()
                except ValueError:
                    print("Invalid format. Use field:value")
                    continue

            if not conditions:
                print("No more rules to add. Knowledge base complete.")
                break

            consequence = {}
            while True:
                cons = input("Enter consequence (field:value): ")
                try:
                    field, value = cons.split(":")
                    consequence[field.strip()] = value.strip()
                    break
                except ValueError:
                    print("Invalid format. Use field:value")
                    continue

            self.add_rule(conditions, consequence)

    def save_to_json(self, filename: str):
        """Save knowledge base to JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.knowledge_base, f, indent=4)