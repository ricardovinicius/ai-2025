import sys
import json

from inference_agent.inference_motor import InferenceMotor
from tools.facts_builder import FactsBuilder

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Usage:\n"
            "  python main.py -k <knowledge_base_file> -f [facts_file] -g <goal_name>\n"
            "  python main.py --tool <tool_name> [tool_args...]"
        )
        sys.exit(1)

    if sys.argv[1] == "--tool":
        if len(sys.argv) < 3:
            print("Error: Tool name required")
            sys.exit(1)
        tool_name = sys.argv[2]
        tool_args = sys.argv[3:]

        if tool_name == "kb_builder":
            from tools.knowledge_base_builder import KnowledgeBaseBuilder
            kb_builder = KnowledgeBaseBuilder()
            kb_builder.build_from_cli()

            output_path = tool_args[0] if len(
                tool_args) > 0 else "knowledge_base.json"

            kb_builder.save_to_json(output_path)
        elif tool_name == "extract_kb_from_dt":
            from tools.extract_kb_from_dt import extract_rules

            if len(tool_args) < 1:
                print(
                    "Usage: python main.py --tool extract_kb_from_dt <input_file> <output_file>")
                sys.exit(1)

            input_file = tool_args[0]
            output_file = tool_args[1] or None

            with open(input_file, 'r') as f:
                decision_tree = json.load(f)

            knowledge_base = extract_rules(decision_tree)

            with open(output_file, 'w') as f:
                if output_file is not None:
                    f.write(json.dumps(knowledge_base,
                            indent=4, ensure_ascii=False))
                else:
                    print(json.dumps(knowledge_base, indent=4, ensure_ascii=False))
        else:
            print(f"Error: Tool '{tool_name}' not found")
            sys.exit(1)

        sys.exit(0)

    # Check for minimum required arguments
    if len(sys.argv) < 5:
        print("Missing required arguments for inference mode")
        sys.exit(1)

    # Parse command line arguments
    knowledge_base_file = None
    facts_file = None
    goal = None

    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "-k":
            knowledge_base_file = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "-f":
            facts_file = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "-g":
            goal = sys.argv[i + 1]
            i += 2
        else:
            i += 1

    if not knowledge_base_file or not goal:
        print("Missing required arguments: knowledge base file (-k) and goal (-g)")
        sys.exit(1)

    with open(knowledge_base_file, 'r') as f:
        knowledge_base = json.load(f)

    if facts_file:
        with open(facts_file, 'r') as f:
            facts = json.load(f)
    else:
        facts_builder = FactsBuilder()
        facts_builder.build_from_cli()
        facts = facts_builder.facts

    inference_motor = InferenceMotor(knowledge_base, facts, goal)
    RESULT = inference_motor.infer()

    print("\nExplanation:")

    for step in inference_motor.explanation:
        print(step)

    print("\nInference Result:")

    if goal in RESULT:
        print("Goal reached")

        print(f"{goal} = {RESULT[goal]}")
    else:
        print("Goal not reached")

    print("\nFinal Facts:")

    print(RESULT)
