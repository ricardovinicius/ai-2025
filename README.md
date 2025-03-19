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

## Exemplos para Questão 5

### Exemplo Gerente

Para exemplificar, considere que você possui uma base de conhecimento localizada em `examples/knowledge_base/credit_cart.json`, gerada com base nos dados do exemplo do Gerente, criada através da árvore de decisão `examples/decision_tree/dt_credit_cart.json` que foi gerada usando o algoritmo CART.

Execute o seguinte comando:

```bash
python main.py -k examples/knowledge_base/credit_cart.json -f examples/knowledge_base/facts_credit_cart.json -g "Risco"
```

### Exemplo Médico

Considere que você possui uma base de conhecimento localizada em `examples/knowledge_base/medic_cart.json`, gerada com base nos dados gerados por uma LLM para exemplificação, criada através da árvore de decisão `examples/decision_tree/dt_medic_cart.json` que foi gerada usando o algoritmo CART.

Execute o seguinte comando:

```bash
python main.py -k examples/knowledge_base/medic_cart.json -g "Diagnóstico"

#### Resultado Esperado:

O sistema irá solicitar algumas informações do paciente:

> Enter fact (field:value) or press Enter to finish: > Gravidade:Baixa

Resfriado Comum

Objetivo alcançado: Diagnóstico
Explicação:
1. Regra aplicada: ...
2. Novo fato derivado: ...
...
```

Caso contrário, ele indicará que o objetivo não pôde ser alcançado com os fatos e regras disponíveis.

Você pode usar os seguintes valores para os fatos:

### Atributos e seus valores possíveis:

- **Idade:**

  - 22
  - 23
  - 25
  - 27
  - 28
  - 30
  - 33
  - 34
  - 35
  - 38
  - 39
  - 40
  - 42
  - 45
  - 48
  - 50
  - 55
  - 56
  - 60
  - 63
  - 70

- **Sintoma Principal:**

  - Dor de cabeça
  - Dor no peito
  - Tosse seca
  - Cansaço extremo
  - Dor nas articulações
  - Dor abdominal
  - Falta de ar
  - Tosse persistente
  - Esquecimento
  - Dor de garganta
  - Dor nas costas
  - Erupção cutânea
  - Carne no seio
  - Cefaleia
  - Febre

- **Sintoma Secundário:**

  - Febre
  - Falta de ar
  - Chiado no peito
  - Perda de peso
  - Rigidez ao acordar
  - Inchaço
  - Tontura
  - Náusea
  - Sede excessiva
  - Confusão mental
  - Dificuldades para engolir
  - Dormência nas pernas
  - Zumbido no ouvido
  - Coceira
  - Cólicas fortes
  - Cólicas intestinais
  - Carne no seio
  - Dor no corpo

- **Gravidade:**

  - Baixa
  - Moderada
  - Alta

- **Histórico de Doenças:**

  - Nenhum
  - Cardíaco
  - Neurológico
  - Artrite
  - Asma
  - Irritação intestinal
  - Alergia
  - Hérnia de disco
  - Doenças inflamatórias intestinais
  - Câncer de mama
  - Diabetes tipo 2
  - Doença de Crohn

- **Diagnóstico:**
  - Gripe
  - Infarto do miocárdio
  - Resfriado comum
  - Câncer de pulmão
  - Acidente vascular cerebral (AVC)
  - Artrite reumatoide
  - Gastroenterite viral
  - Asma controlada
  - Tuberculose
  - Enxaqueca crônica
  - Diabetes tipo 2
  - Doença de Alzheimer
  - Faringite estreptocócica
  - Hérnia de disco lombar
  - Pneumonia bacteriana
  - Vertigem posicional benigna
  - Alergia alimentar
  - Câncer de mama
  - Síndrome do intestino irritável
  - Endometriose
  - Enxaqueca com aura
  - Embolia pulmonar
  - Dengue

### Exemplo Mini Akinator

Para esse exemplo foi criado uma base de dados pequena dos personagens do jogo League of Legends.

Considere que você possui uma base de conhecimento localizada em `examples/knowledge_base/lol_cart.json`, gerada com base nos dados do League of Legends, criada através da árvore de decisão `examples/decision_tree/dt_lol_cart.json` que foi gerada usando o algoritmo CART.

Execute o seguinte comando:

```bash
python main.py -k examples/knowledge_base/lol_cart.json -g "name"

#### Resultado Esperado:

O sistema irá solicitar algumas informações do personagem:

> Enter fact (field:value) or press Enter to finish: > attack_damage:65
> armor:33

Camille

Objetivo alcançado: name
Explicação:
1. Regra aplicada: ...
2. Novo fato derivado: ...
...
```

Caso contrário, ele indicará que o objetivo não pôde ser alcançado com os fatos e regras disponíveis.

Você pode usar os seguintes valores para os fatos:

- **attack_damage:**

  - 65
  - 70
  - 50
  - 53
  - 55
  - 58
  - 60
  - 62

- **armor:**

  - 33
  - 28
  - 25
  - 19
  - 20
  - 40
  - 35

- **difficulty:**

  - 1
  - 2

- **health:**

  - 480
  - 510
  - 600
  - 530
  - 540
  - 570
  - 580
  - 550
  - 500
  - 700

- **movement_speed:**

  - 330
  - 325

- **class:**
  - Mage
  - Assassin
  - Tank

E esse são os possíveis campeões

- **Champion Names:**
  - Camille
  - Fiora
  - Draven
  - Garen
  - Darius
  - Amumu
  - Cassiopeia
  - Elise
  - Anivia
  - Fiddlesticks
  - Bard
  - Ahri
  - Brand
  - Braum
  - Aurelion Sol
  - Evelynn
  - Gragas
  - Alistar
  - Galio
  - Ekko
  - Diana
  - Blitzcrank
  - Ezreal
  - Ashe
  - Cho'Gath
  - Akali
  - Gangplank
  - Dr. Mundo
  - Caitlyn

## Explicação do Código

O sistema usa o **motor de inferência** para aplicar regras da base de conhecimento aos fatos fornecidos e gerar novos fatos até que o objetivo seja alcançado ou as regras não possam ser mais aplicadas. O processo é explicado passo a passo e a inferência é impressa no final.
