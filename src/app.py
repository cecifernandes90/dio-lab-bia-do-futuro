import os
import pandas as pd
import google.generativeai as genai

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Defina a variável de ambiente GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

df = pd.read_csv("../data/transacoes.csv")

SYSTEM_PROMPT = """
Você é o PlannerPro, um assistente financeiro estratégico.
Você ajuda o usuário a planejar a construção de um escritório em casa.
Use apenas dados fornecidos. Não invente informações.
"""

def gerar_contexto(df):
    resumo = df.groupby("tipo")["valor"].sum().to_dict()
    return f"Receitas: {resumo.get('receita',0)} | Despesas: {resumo.get('despesa',0)}"

contexto = gerar_contexto(df)

print("PlannerPro iniciado. Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ")

    if pergunta.lower() == "sair":
        break

    prompt = f"""
{SYSTEM_PROMPT}

Contexto:
{contexto}

Pergunta:
{pergunta}
"""

    resposta = model.generate_content(prompt)
    print("\nPlannerPro:", resposta.text, "\n")