from inference_agent.inference_rules import hypothetical_syllogism, modus_ponens, modus_tollens


class InferenceMotor:
    """
    The inference motor of the expert system.
    """

    def __init__(self, rules, facts, goal):
        self.rules = rules
        self.facts = facts
        self.goal = goal

    def derivate_facts(self):
        """
        Derives new facts from the knowledge base.
        :param rules: The list of rules.
        :param facts: The list of facts.
        :return: The updated list of facts.
        """
        new_facts = self.facts.copy()

        for rule in self.rules:
            self.rules = hypothetical_syllogism(rule, self.rules) or self.rules

            if modus_ponens(rule, new_facts):
                for consequence, value in rule["consequence"].items():
                    new_facts[consequence] = value

            new_facts = modus_tollens(rule, new_facts)

        return new_facts

    def infer(self):
        """
        Infers the goal from the knowledge base.
        :param rules: The list of rules.
        :param facts: The list of facts.
        :param goal: The goal to be inferred.
        :return: The inferred goal.
        """
        while True:
            new_facts = self.derivate_facts()

            if self.goal in new_facts:
                return new_facts

            if new_facts == self.facts:
                return new_facts

            self.facts = new_facts
