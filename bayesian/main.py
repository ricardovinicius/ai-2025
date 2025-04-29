import pandas as pd
import xml.etree.ElementTree as ET
from collections import defaultdict
from itertools import product

def sanitize(name):
    return name.strip().replace(" ", "_")

def create_state_element(state_id):
    state_elem = ET.Element("state")
    state_elem.set("id", state_id)
    return state_elem

def create_cpt_node(var_id, states, parents=None, probs=None):
    node = ET.Element("cpt")
    node.set("id", var_id)
    for s in states:
        node.append(create_state_element(s))
    if parents:
        parent_elem = ET.SubElement(node, "parents")
        parent_elem.text = " ".join(parents)
    prob_elem = ET.SubElement(node, "probabilities")
    prob_elem.text = " ".join(f"{p:.3f}" for p in probs)
    return node

def calculate_probabilities(df, var, parents=[]):
    if not parents:
        # Probabilidades marginais para variáveis independentes
        counts = df[var].value_counts(normalize=True)
        # Normalização explícita
        total_count = counts.sum()
        normalized_counts = counts / total_count
        return normalized_counts.reindex(df[var].unique(), fill_value=0).tolist()

    probs = []
    parent_vals = [df[p].unique() for p in parents]
    for values in product(*parent_vals):
        condition = (df[parents[0]] == values[0])
        for i in range(1, len(parents)):
            condition &= (df[parents[i]] == values[i])
        sub_df = df[condition]
        if len(sub_df) == 0:
            # Se não houver dados para esse conjunto de valores, usamos uma distribuição uniforme
            probs.extend([1 / len(df[var].unique())] * len(df[var].unique()))
        else:
            counts = sub_df[var].value_counts(normalize=True)
            # Normalização explícita
            total_count = counts.sum()
            normalized_counts = counts / total_count
            probs.extend(normalized_counts.reindex(df[var].unique(), fill_value=0).tolist())
    return probs

def generate_network(df):
    df = df.copy()
    df.columns = [sanitize(c) for c in df.columns]
    df = df.fillna("Unknown")

    root = ET.Element("smile", {
        "version": "1.0", "id": "Network1", "numsamples": "10000",
        "discsamples": "10000"
    })
    nodes = ET.SubElement(root, "nodes")
    node_ids = []

    variables = ['Gender', 'Blood_Pressure', 'Cholesterol_Level']
    symptoms = ['Fever', 'Cough', 'Fatigue', 'Difficulty_Breathing']

    # Recriar a coluna Disease com estado Negative onde Outcome != Positive
    df['Disease'] = df.apply(
        lambda row: row['Disease'] if row['Outcome_Variable'] == 'Positive' else 'Negative',
        axis=1
    )
    df['Disease'] = df['Disease'].astype(str)

    # Criar CPTs de variáveis independentes
    for var in variables:
        states = df[var].unique().tolist()
        probs = calculate_probabilities(df, var)
        node = create_cpt_node(var, states, probs=probs)
        nodes.append(node)
        node_ids.append(var)

    # Criar único nó de Disease, dependente das variáveis clínicas
    disease_states = df['Disease'].unique().tolist()
    probs = calculate_probabilities(df, 'Disease', parents=variables)
    node = create_cpt_node('Disease', disease_states, parents=variables, probs=probs)
    nodes.append(node)
    node_ids.append('Disease')

    # Sintomas como filhos de Disease
    for symptom in symptoms:
        parents = ['Disease']
        states = df[symptom].unique().tolist()
        probs = calculate_probabilities(df, symptom, parents=parents)
        node = create_cpt_node(symptom, states, parents=parents, probs=probs)
        nodes.append(node)
        node_ids.append(symptom)

    tree = ET.ElementTree(root)
    add_visual_extensions(root, node_ids)
    ET.indent(tree, space="\t", level=0)
    tree.write("rede_bayesiana.xml", encoding="utf-8", xml_declaration=True)

def add_visual_extensions(root, node_ids):
    extensions = ET.SubElement(root, "extensions")
    genie = ET.SubElement(extensions, "genie", {
        "version": "1.0",
        "app": "GeNIe 5.0.4830.0 ACADEMIC",
        "name": "Network1"
    })

    # Definir posições iniciais
    x_start, y_start = 100, 100
    x_offset, y_offset = 150, 100

    for idx, node_id in enumerate(node_ids):
        node_elem = ET.SubElement(genie, "node", {"id": node_id})
        ET.SubElement(node_elem, "name").text = node_id.replace("_", " ")

        # Cores e fonte
        ET.SubElement(node_elem, "interior", {"color": "e5f6f7"})
        ET.SubElement(node_elem, "outline", {"color": "000080"})
        ET.SubElement(node_elem, "font", {"color": "000000", "name": "Arial", "size": "8"})

        # Posição calculada
        x1 = x_start + (idx % 5) * x_offset
        y1 = y_start + (idx // 5) * y_offset
        x2 = x1 + 100
        y2 = y1 + 60
        ET.SubElement(node_elem, "position").text = f"{x1} {y1} {x2} {y2}"

# === Uso ===
df = pd.read_csv("data.csv")  # Substitua pelo caminho do seu CSV
generate_network(df)
