# 🚀 GLOBAL SOLUTION: Otimização Energética por Data Science e IoT
## Foco: Eliminação de Desperdício Residual (R$ 26.155,68/ano)

# Integrantes:

• Gabriel Drebtchinsky Q de Carvalho – RM566729
• José Ribeiro dos Santos Neto – RM567692

---

### 1. 🎯 Abordagem Estratégica: Análise de Dados

**Decisão:** Escolhemos a **Opção A: Análise de Dados** como a abordagem mais eficiente.

**Justificativa:** O maior impacto na otimização energética está em **quantificar o problema**. Ao focar na Modelagem de Dados e no *insight*, garantimos que a solução proposta (Automação/IoT) seja diretamente justificada por um cálculo financeiro sólido, priorizando o ROI do projeto.

---

### 2. 🏗️ Modelagem e Geração do Dataset

Para simular um ambiente corporativo real, criamos um *dataset* com medições **horárias** de 30 dias.

**Raciocínio da Simulação:**
* **Servidores:** Consumo base **alto e constante** (24/7).
* **Escritório Geral:** Consumo **variável** (pico durante o dia).
* **Injeção de Desperdício:** Introduzimos propositalmente um consumo residual de $\approx 1,8 \text{ kWh}/\text{h}$ no **Escritório Geral** durante a madrugada e finais de semana. Este é o nosso **problema-alvo**.

#### Estrutura do Arquivo: `consumo_energetico_simulado.csv`

| Coluna | Descrição | Importância na Análise |
| :---: | :---: | :---: |
| `DataHora` | Timestamp da medição (horária). | Chave para identificar padrões temporais (dia vs. noite). |
| `Setor` | Área de medição. | Segmentação do consumo para direcionar a solução. |
| `Consumo_kWh` | Consumo energético na hora. | **Variável principal** – o que será reduzido. |
| `Ocupacao_Pessoas` | Número de pessoas presentes (simulado). | Variável crucial para **separar uso produtivo de desperdício**. |
| `Tarifa_RS_kWh` | Custo unitário da energia (R$ 0,85). | Base para o cálculo do impacto financeiro (Custo x kWh). |

---

### 3. 🔎 Análise de Dados Completa (EDA)

O objetivo da Análise Exploratória de Dados (EDA) é transformar o consumo em um **Diagnóstico Acionável**.

#### 3.1. Visão Geral (Custo Mensal Total)
* **Consumo Total Mensal:** 12.189,45 kWh
* **Custo Total Mensal Estimado:** R$ 10.361,03

#### 3.2. Identificação do Problema: O Desperdício

Definimos um filtro rigoroso para isolar o consumo não produtivo no setor **Escritório Geral**:
* **Filtro:** `Setor == 'Escritorio_Geral'` **AND** `Ocupacao_Pessoas <= 1` **AND** `Fora de Horário Comercial`.

**Resultados da Quantificação (Custo do Desperdício):**

| Métrica | Valor | Raciocínio (Por que é importante?) |
| :---: | :---: | :---: |
| **Desperdício Isolado (kWh)** | **2.564,28 kWh/mês** | Quantifica exatamente o volume de energia perdida. |
| **Custo do Desperdício (Mensal)** | **R$ 2.179,64** | O valor exato que a empresa gasta desnecessariamente. |
| **Custo Anual Projetado** | **R$ 26.155,68** | O *target* financeiro para justificar a solução. |
| **% do Desperdício no Total** | **21,04%** | Indica que o problema é sistêmico e merece atenção imediata. |

**GRÁFICO CHAVE (Apresentado no Notebook `analise_energetica.ipynb`):**
* **Gráfico de Linha: Consumo Horário vs. Ocupação no Escritório Geral.** Este gráfico mostra claramente o **vale de consumo** no período noturno, onde o `Consumo_kWh` residual (a linha) permanece alto, enquanto a `Ocupacao_Pessoas` (a barra) cai para zero, provando o desperdício.

---

### 4. ⚙️ Solução Proposta: Otimização por IoT

A solução de **Otimização Energética** é a eliminação total do desperdício de R$ 26.155,68 anuais, utilizando tecnologia **IoT** (Automação).

#### Proposta Técnica: Sistema de Desligamento Inteligente
A solução consiste na instalação de **Relés Inteligentes (Smart Plugs)** ou **Disjuntores IoT** controlados por um *Gateway*.

* **Ação:** Criação de uma rotina de automação forçada.
    * **Dias Úteis:** Desligamento automático de todos os periféricos (monitores, iluminação secundária, carregadores) às **20:00**.
    * **Finais de Semana:** Desligamento total.
* **Benefício:** Elimina 100% da chance de erro humano (esquecimento), garantindo que o consumo caia para o mínimo aceitável quando o setor estiver vazio.

#### Análise de Retorno sobre Investimento (ROI)

| Métrica | Valor | Conclusão Financeira |
| :---: | :---: | :---: |
| **Economia Mensal Gerada** | R$ 2.179,64 | O ganho mensal é maior que o investimento total. |
| **Investimento Inicial Estimado (CAPEX)** | R$ 1.600,00 | Custo dos dispositivos IoT (Sensores, Relés, Gateway). |
| **Período de Retorno (Payback)** | **< 1 Mês (0,73 meses)** | A solução se paga em aproximadamente **22 dias**. |

---

link Vídeo: https://youtu.be/NdZ1oLZ-RF4

link Github: https://github.com/ZeNeto10/Gs_Energia.git