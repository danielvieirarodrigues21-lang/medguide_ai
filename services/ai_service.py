
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

SYSTEM_PROMPT = """
Você é um assistente virtual de saúde e bem-estar.

Regras:
- Explique informações de forma simples.
- Seja educativo.
- Não substitua médicos.
- Recomende procurar profissionais quando necessário.
- Seja cordial.
"""

def gerar_resposta(pergunta):
    try:
        resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": pergunta
                }
            ],
            temperature=0.7,
            max_tokens=300
        )

        return resposta.choices[0].message.content

    except Exception as erro:
        return f"Erro ao gerar resposta: {erro}"
