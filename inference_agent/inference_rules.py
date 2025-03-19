def modus_ponens(rule, facts):
    """
    Modus Ponens inference rule.
    :param rule: The rule to be applied.
    :param facts: The facts to be used.
    :return: The updated facts.
    """
    for condition, value in rule["conditions"].items():
        if condition not in facts or facts[condition] != value:
            return False

    return True


def hypothetical_syllogism(rule, rules):
    """
    Hypothetical Syllogism inference rule.
    :param rule: The rule to be applied.
    :param rules: The list of rules to be used.
    :return: The updated list of rules
    """
    for other_rule in rules:
        if other_rule["conditions"] == rule["consequence"]:
            new_rule = {
                "conditions": {
                    **rule["conditions"],
                },
                "consequence": {
                    **other_rule["consequence"],
                }
            }
            rules.append(new_rule)

            return rules


def modus_tollens(rule, facts):
    """
    Modus Tollens inference rule.
    :param rule: The rule to be applied.
    :param facts: The facts to be used.
    :return: The updated facts.
    """
    for consequence, value in rule["consequence"].items():
        if consequence in facts and facts[consequence] == "False":
            for condition in rule["conditions"]:
                if condition not in facts:
                    facts[condition] = "False"

    return facts
