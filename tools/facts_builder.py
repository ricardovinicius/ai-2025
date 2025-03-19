class FactsBuilder:
    def __init__(self):
        self.facts = {}

    def add_fact(self, field: str, value: str):
        """Add a fact to the knowledge base."""
        self.facts[field] = value

    def build_from_cli(self):
        """Build facts interactively from command line."""
        while True:
            fact = input("Enter fact (field:value) or press Enter to finish: ")
            if not fact:
                break
            try:
                field, value = fact.split(":")
                self.add_fact(field.strip(), value.strip())
            except ValueError:
                print("Invalid format. Use field:value")
