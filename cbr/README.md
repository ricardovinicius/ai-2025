# Disease Diagnosis using CBRKit

Este projeto é uma aplicação simples de **Raciocínio Baseado em Casos (CBR)** usando a biblioteca [CBRKit](https://pypi.org/project/cbrkit/) para auxiliar na previsão de doenças com base em sintomas e características do paciente.

## 🧠 Objetivo

Utilizar CBR para comparar um novo caso (paciente) com casos anteriores armazenados em um dataset (`disease.csv`) e sugerir a doença mais provável com base em similaridade.

## 📁 Estrutura do Projeto

```

.
├── disease.csv          # Base de casos (dataset de doenças)
├── main.py              # Script principal com a lógica CBR
└── README.md            # Documentação do projeto

````

## 🛠️ Requisitos

- Python 3.8+
- Bibliotecas:
  - `cbrkit`

Você pode instalar o `cbrkit` com:

```bash
pip install cbrkit
````

## 📝 Dataset (`disease.csv`)

O dataset deve conter colunas representando atributos dos pacientes e a doença associada. Exemplo de colunas esperadas:

* `Fever` (Yes/No)
* `Cough` (Yes/No)
* `Fatigue` (Yes/No)
* `Difficulty Breathing` (Yes/No)
* `Age` (int)
* `Gender` (Male/Female)
* `Blood Pressure` (High/Normal/Low)
* `Cholesterol Level` (High/Normal/Low)
* `Disease` (Diagnóstico final)

## 🚀 Como Usar

### 1. Execute o script principal:

```bash
python main.py
```

### 3. Resultado Esperado

O script irá imprimir o nome da doença mais similar ao caso de entrada definido no `query`.

## 🔍 Lógica de Similaridade

O sistema usa:

* Comparação por igualdade para atributos categóricos (como `Fever`, `Gender`, etc.).
* Similaridade linear para atributos numéricos como `Age`.
* Agregador de média para combinar os escores de similaridade.

## 📬 Exemplo de Consulta (Query)

```python
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
```

## 🧪 Resultado

O sistema retorna os 5 casos mais similares, e imprime o diagnóstico (doença) do caso mais similar encontrado.
