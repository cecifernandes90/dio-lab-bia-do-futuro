# Avaliação e Métricas

## Objetivo da Avaliação
Avaliar a qualidade do agente PlannerPro na tarefa de auxiliar o planejamento financeiro para construção de um escritório em casa, garantindo respostas corretas, consistentes e baseadas nos dados fornecidos.

---

## Métricas Utilizadas

### 1. Precisão das Respostas
**Descrição:**  
Verifica se as respostas do agente estão coerentes com os dados de transações fornecidos.

**Como medir:**
- Comparação entre valores retornados e dados reais do CSV
- Verificação manual de amostras de respostas

**Meta:**  
≥ 90% de respostas consistentes com os dados

---

### 2. Taxa de Alucinação
**Descrição:**  
Avalia se o agente inventa valores ou informações não presentes nos dados.

**Como medir:**
- Testes com perguntas fora do dataset
- Verificação de respostas sem base factual

**Meta:**  
≤ 5% de respostas com informações não suportadas

---

### 3. Coerência com o Objetivo do Agente
**Descrição:**  
Avalia se o agente mantém o foco no planejamento do escritório em casa.

**Como medir:**
- Análise qualitativa das respostas
- Verificar se o agente foge do escopo financeiro definido

**Meta:**  
≥ 95% de respostas dentro do escopo

---

### 4. Clareza da Resposta
**Descrição:**  
Avalia se as respostas são compreensíveis e úteis para o usuário final.

**Como medir:**
- Feedback qualitativo
- Simulação de uso por usuários

**Meta:**  
≥ 90% de respostas consideradas claras

---

## Tabela de Avaliação (Exemplo)

| Teste | Pergunta | Esperado | Resultado | Status |
|------|---------|----------|-----------|--------|
| 1 | Quanto posso economizar? | Valor baseado em transações | Valor calculado corretamente | ✔ |
| 2 | Quanto tempo para 3000? | Cálculo baseado em saldo | Solicita dados adicionais | ✔ |
| 3 | Onde gasto mais? | Categorias reais do CSV | Identifica corretamente | ✔ |
| 4 | Investir em ações? | Recusa ou redireciona | Mantém escopo | ✔ |

---

## Conclusão

O agente PlannerPro demonstra boa precisão e forte controle de escopo, evitando alucinações e mantendo foco no objetivo principal: planejamento financeiro para construção de um escritório em casa.