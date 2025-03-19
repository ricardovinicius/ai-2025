from inference_agent.inference_rules import hypothetical_syllogism, modus_ponens, modus_tollens


class InferenceMotor:
    """
    The inference motor of the expert system.
    """

    def __init__(self, rules, facts, goal):
        self.rules = rules
        self.facts = facts
        self.goal = goal
        self.explanation = []  # Lista para armazenar os passos da explicação

    def derivate_facts(self):
        """
        Derives new facts from the knowledge base.
        :return: The updated list of facts.
        """
        new_facts = self.facts.copy()

        for rule in self.rules:
            # Aplicar silogismo hipotético
            updated_rules = hypothetical_syllogism(rule, self.rules)
            if updated_rules and updated_rules != self.rules:
                self.rules = updated_rules
                self.explanation.append(
                    f"Aplicado silogismo hipotético com a regra: {rule}")

            # Aplicar modus ponens
            if modus_ponens(rule, new_facts):
                for consequence, value in rule["consequence"].items():
                    new_facts[consequence] = value
                    self.explanation.append(
                        f"Aplicado modus ponens: {rule} -> {consequence} = {value}"
                    )

            # Aplicar modus tollens
            updated_facts = modus_tollens(rule, new_facts)
            if updated_facts != new_facts:
                self.explanation.append(
                    f"Aplicado modus tollens com a regra: {rule}")
                new_facts = updated_facts

        return new_facts

    def infer(self):
        """
        Infers the goal from the knowledge base.
        :return: The inferred goal and explanation.
        """
        self.explanation = []  # Reiniciar a explicação para uma nova inferência

        while True:
            self.explanation.append(f"Fatos atuais: {self.facts}")
            new_facts = self.derivate_facts()

            if self.goal in new_facts:
                self.explanation.append(
                    f"Objetivo '{self.goal}' alcançado com valor: {new_facts[self.goal]}")
                return new_facts

            if new_facts == self.facts:
                self.explanation.append(
                    "Nenhum novo fato pode ser derivado. Objetivo não alcançado.")
                return new_facts

            self.facts = new_facts

    def get_explanation(self):
        """
        Returns the explanation of the inference process.
        :return: List of explanation steps
        """
        return self.explanation
