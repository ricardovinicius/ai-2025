import sys
import json


def extract_rules(tree, consequence_key, path=None, rules=None):
    """
    Recursively traverses the tree and extracts rules for a knowledge base.

    :param tree: The decision tree represented as a nested dictionary.
    :param path: The path of conditions traversed up to the current node.
    :param rules: The list where extracted rules will be stored.
    :return: A list of extracted rules.
    """
    if path is None:
        path = {}
    if rules is None:
        rules = []

    if isinstance(tree, dict):  # If it's a dictionary, continue traversing
        for key, value in tree.items():
            if isinstance(value, dict):  # Intermediate node
                for subkey, subvalue in value.items():
                    new_path = path.copy()
                    new_path[key] = subkey
                    extract_rules(
                        subvalue, consequence_key=consequence_key, path=new_path, rules=rules)
            else:  # Leaf node -> Store the rule
                rule = {
                    "conditions": path.copy(),
                    "consequence": value
                }
                rules.append(rule)
    else:  # If a direct value is found (avoids errors)
        rule = {
            "conditions": path.copy(),
            "consequence": {
                consequence_key: tree
            }
        }
        rules.append(rule)

    return rules


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_rules_from_dt.py -i <input_file> -o <output_file>")
        sys.exit(1)

    input_file = sys.argv[2]
    output_file = sys.argv[4] if len(sys.argv) > 4 else None

    with open(input_file, 'r') as f:
        decision_tree = json.load(f)

    knowledge_base = extract_rules(decision_tree, consequence_key="Risco")

    if output_file:
        with open(output_file, 'w') as f:
            f.write(json.dumps(knowledge_base, indent=4, ensure_ascii=False))
    else:
        print(json.dumps(knowledge_base, indent=4, ensure_ascii=False))
