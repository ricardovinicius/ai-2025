
# Aplicação de Redes Bayesianas para Diagnóstico Médico

## Introdução

Redes Bayesianas são modelos gráficos probabilísticos capazes de representar e inferir relações de dependência entre variáveis aleatórias. Em aplicações médicas, essas redes permitem realizar diagnósticos com base em sintomas observados, considerando incertezas e correlações entre sinais clínicos e doenças. Neste trabalho, apresentamos um exemplo de aplicação de Rede Bayesiana voltado ao diagnóstico de doenças respiratórias a partir de sintomas clínicos e variáveis fisiológicas.

## Fonte de Dados

A base de dados utilizada neste projeto foi obtida a partir de uma fonte pública no Kaggle, contendo registros tabulados de pacientes. A base incluía informações como:

-   **Variáveis fisiológicas**: Pressão arterial, nível de colesterol, sexo biológico, entre outros.
    
-   **Sintomas**: Febre, tosse, fadiga, dificuldade para respirar.
    
-   **Diagnóstico final**: Classificação do paciente com uma das doenças (por exemplo, _Pneumonia_, _Asma_, _Bronquite_) e uma variável de saída (classificada como _Positive_ ou  _Negative_).

A base de dados está disponível em: https://www.kaggle.com/datasets/uom190346a/disease-symptoms-and-patient-profile-dataset.

Para essa aplicação utilizamos dados apenas sobre algumas doenças específicas para fins de simplificar o exemplo. As doenças classificadas foram:
- Allergic Rhinitis
- Asthma
- Common Cold
- Influenza
- Pneumonia
    

## Modelagem da Rede Bayesiana

A modelagem da rede seguiu os seguintes princípios:

-   As variáveis fisiológicas foram tratadas como **nós independentes**.
    
-   A variável **Disease** representa o diagnóstico do paciente, e pode assumir os valores `{Pneumonia, Asthma, Common Cold, ..., Negative}`.
    
-   A variável **Disease** possui como pais as variáveis fisiológicas (e.g., _Blood_Pressure_, _Cholesterol_Level_, _Gender_).
    
-   Os **sintomas** foram modelados como **variáveis dependentes** da doença, assumindo que a manifestação dos sintomas é influenciada diretamente pelo tipo de doença do paciente.
    
-   A rede foi implementada em formato XML compatível com a ferramenta **GeNIe**.

A escolha da ferramenta GeNIE se deu pela facilidade da modelagem e utilização.
    
### Estrutura da Rede

![Topologia da Rede](https://i.imgur.com/NrYg0L2.png)
*Figura 1: Visualização da topologia da rede no GeNIe.*

![Disease TPC](https://i.imgur.com/uxm14Am.png)
*Figura 2: Tabela de Probabilidade Condicional de Disease no GeNIe.*

## Representação do Conhecimento



O conhecimento médico foi representado por meio de uma rede Bayesiana em que as **probabilidades condicionais** foram estimadas a partir da frequência dos eventos na base de dados. A ausência de casos específicos foi tratada por meio de distribuições uniformes, assumindo incerteza quando não havia evidência empírica.

Para realizar a criação da rede, criamos uma aplicação simples em **Python** que transformava os dados tabulados no formato XML compatível, fazendo os cálculos das probabilidades conforme descrito.

A representação foi salva em um arquivo `.xml` no padrão SMILE/GeNIe, e visualizada com auxílio do software **GeNIe Academic**. A rede foi construída com nós categóricos, e os estados de cada variável foram derivados diretamente dos valores presentes na base.

## Inferência e Exemplos

A ferramenta GeNIe foi utilizada para realizar inferência probabilística sobre a rede construída. A seguir, são apresentados exemplos de uso:

### Exemplo 1: Diagnóstico baseado em sintomas

Dado o cenário em que um paciente apresenta:

-   **Fever = Yes**
    
-   **Cough = Yes**
    
-   **Difficulty_Breathing = Yes**
    

Ao inserir essas evidências na rede, a probabilidade da variável **Disease** muda consideravelmente, indicando um aumento significativo da probabilidade de doenças como _Asthma_. O sistema é capaz de inferir que, com base nesses sintomas, há uma alta probabilidade de infecção respiratória.

![enter image description here](https://i.imgur.com/MBS4mTg.png)
*Figura 3: Demonstração do Exemplo 1.*


### Exemplo 2: Variação por características fisiológicas

Para um paciente do sexo masculino, com pressão arterial elevada e colesterol alto, mesmo sem sintomas relatados, a rede indica uma probabilidade ligeiramente maior das doenças em relação a _Allergic Rhinitis_. A inferência reflete padrões estatísticos extraídos da base.

![enter image description here](https://i.imgur.com/7C2qVUI.png)
*Figura 4: Demonstração do Exemplo 2.*

## Conclusão

A aplicação de redes Bayesianas em sistemas de suporte ao diagnóstico médico permite lidar com incertezas, ausência de dados e relações probabilísticas entre variáveis. A modelagem apresentada demonstra como sintomas e características clínicas podem ser combinados para estimar a probabilidade de doenças com base em uma base de dados real. A ferramenta GeNIe se mostrou adequada tanto para a construção quanto para a inferência e visualização da rede.
