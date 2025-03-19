# README - Inference System

Este sistema realiza inferência com base em uma base de conhecimento, fatos e um objetivo fornecido, utilizando um motor de inferência. Ele também pode ser usado para construir ou extrair bases de conhecimento de outras fontes, como árvores de decisão.

## Funcionalidades

- **Modo de Inferência**: Usa uma base de conhecimento e fatos para realizar inferências até atingir um objetivo.
- **Ferramentas**: Oferece ferramentas para construir bases de conhecimento ou extrair uma base de conhecimento de uma árvore de decisão.

## Pré-requisitos

Antes de executar o script, tenha certeza de que você possui as seguintes dependências:

- Python 3.x

## Como usar

### Modo de Inferência

Para rodar a inferência com uma base de conhecimento e um objetivo, use o seguinte comando:

```bash
python main.py -k <knowledge_base_file> -f [facts_file] -g <goal_name>
```

#### Argumentos:

- `-k <knowledge_base_file>`: Caminho para o arquivo JSON da base de conhecimento.
- `-f <facts_file>` (opcional): Caminho para o arquivo JSON contendo os fatos iniciais. Se não for fornecido, o sistema pedirá para inserir os fatos através da interface de linha de comando.
- `-g <goal_name>`: Nome do objetivo a ser alcançado (deve ser uma chave presente na base de conhecimento).

#### Exemplo:

```bash
python main.py -k knowledge_base.json -f facts.json -g "GoalName"
```

Se o objetivo for alcançado, o sistema imprimirá o resultado e a explicação detalhada de como o objetivo foi atingido.

### Ferramentas

#### Construir a Base de Conhecimento

Para construir uma base de conhecimento, use a ferramenta `kb_builder`:

```bash
python main.py --tool kb_builder [output_path]
```

- `[output_path]`: Caminho para salvar a base de conhecimento gerada. Se não for fornecido, o arquivo será salvo como `knowledge_base.json`.

#### Extrair Base de Conhecimento de uma Árvore de Decisão

Se você tiver uma árvore de decisão e quiser gerar uma base de conhecimento a partir dela, use a ferramenta `extract_kb_from_dt`:

```bash
python main.py --tool extract_kb_from_dt <input_file> <output_file>
```

- `<input_file>`: Arquivo JSON contendo a árvore de decisão.
- `<output_file>`: Arquivo JSON para salvar a base de conhecimento extraída. Se não for fornecido, a base de conhecimento será impressa no console.

#### Exemplo:

```bash
python main.py --tool extract_kb_from_dt decision_tree.json knowledge_base.json
```

## Exemplo Completo

### Exemplo Gerente

Para exemplificar, considere que você possui uma base de conhecimento localizada em `examples/knowledge_base/credit_cart.json`, gerada com base nos dados do exemplo do Gerente, criada através da árvore de decisão `examples/decision_tree/dt_credit_cart.json` que foi gerada usando o algoritmo CART.

Execute o seguinte comando:

```bash
python main.py -k examples/knowledge_base/credit_cart.json -f examples/knowledge_base/facts_credit_cart.json -g "Risco"
```

#### Resultado Esperado:

O sistema analisará as regras da base de conhecimento e os fatos fornecidos. Se o objetivo for alcançado, ele imprimirá algo como:

```
Objetivo alcançado: Risco
Explicação:
1. Regra aplicada: ...
2. Novo fato derivado: ...
...
```

Caso contrário, ele indicará que o objetivo não pôde ser alcançado com os fatos e regras disponíveis.

## Explicação do Código

O sistema usa o **motor de inferência** para aplicar regras da base de conhecimento aos fatos fornecidos e gerar novos fatos até que o objetivo seja alcançado ou as regras não possam ser mais aplicadas. O processo é explicado passo a passo e a inferência é impressa no final.
