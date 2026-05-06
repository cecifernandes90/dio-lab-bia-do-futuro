import os
import pandas as pd
import google.generativeai as genai

# =========================
# CONFIGURAÇÃO DA API
# =========================

# Defina sua chave de API como variável de ambiente antes de rodar:
# Windows (cmd): setx GEMINI_API_KEY "SUA_CHAVE"
# Linux/Mac: export GEMINI_API_KEY="SUA_CHAVE"

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Defina a variável de ambiente GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

# =========================
# CARREGAR DADOS
# =========================

try:
    df = pd.read_csv("data/transacoes.csv")
except Exception as e:
    raise Exception(f"Erro ao carregar transacoes.csv: {e}")

# =========================
# SYSTEM PROMPT
# =========================

SYSTEM_PROMPT = """
Você é o PlannerPro, um assistente financeiro estratégico e objetivo.

Seu objetivo é ajudar o usuário a planejar financeiramente a construção de um escritório em casa, com base nas transações fornecidas.

REGRAS:
- Use apenas os dados fornecidos
- Não invente informações
- Seja direto e prático
- Se não houver dados suficientes, informe claramente
"""

# =========================
# FUNÇÃO PARA FORMATAR CONTEXTO
# =========================

def gerar_contexto(df):
    resumo = df.groupby("tipo")["valor"].sum().to_dict()
    
    total_receita = resumo.get("receita", 0)
    total_despesa = resumo.get("despesa", 0)

    return f"""
Resumo financeiro do usuário:
- Total de receitas: {total_receita}
- Total de despesas: {total_despesa}
"""

# =========================
# LOOP DE INTERAÇÃO
# =========================

def main():
    print("PlannerPro iniciado. Digite 'sair' para encerrar.\n")

    contexto = gerar_contexto(df)

    while True:
        pergunta = input("Você: ")

        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Encerrando...")
            break

        prompt = f"""
{SYSTEM_PROMPT}

{contexto}

Pergunta do usuário:
{pergunta}
"""

        try:
            resposta = model.generate_content(prompt)
            print("\nPlannerPro:", resposta.text, "\n")
        except Exception as e:
            print(f"Erro ao gerar resposta: {e}")


if __name__ == "__main__":
    main()