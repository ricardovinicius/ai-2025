import cbrkit

DATAFILE_PATH = "disease.csv"

casebase = cbrkit.loaders.file(DATAFILE_PATH)

print(casebase)

query = {
    "Fever": "Yes",
    "Cough": "Yes",
    "Fatigue": "Yes",
    "Difficulty Breathing": "Yes",
    "Age": 30,
    "Gender": "Female",
    "Blood Pressure": "Normal",
    "Cholesterol Level": "Normal"
}

sim_attr = cbrkit.sim.attribute_value(
    attributes={
        "Fever": cbrkit.sim.generic.equality(),
        "Cough": cbrkit.sim.generic.equality(),
        "Fatigue": cbrkit.sim.generic.equality(),
        "Difficulty Breathing": cbrkit.sim.generic.equality(),
        "Age": cbrkit.sim.numbers.linear(max=5),
        "Gender": cbrkit.sim.generic.equality(),
        "Blood Pressure": cbrkit.sim.generic.equality(),
        "Cholesterol Level": cbrkit.sim.generic.equality(),
    },
    aggregator=cbrkit.sim.aggregator(pooling="mean"),
)

retriever = cbrkit.retrieval.dropout(
    cbrkit.retrieval.build(sim_attr),
    limit=5
)

result = cbrkit.retrieval.apply_query(casebase, query, retriever)

print(casebase[result.ranking[0]]["Disease"])
