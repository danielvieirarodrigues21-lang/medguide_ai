
import streamlit as st
from services.ai_service import gerar_resposta
from services.health_service import (
    calcular_imc,
    calcular_consumo_agua
)
from services.memory_service import (
    salvar_historico,
    carregar_historico
)

st.set_page_config(
    page_title="MedGuide AI",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 MedGuide AI")
st.subheader("Seu assistente virtual inteligente de saúde")

historico = carregar_historico()

menu = st.sidebar.selectbox(
    "Escolha uma funcionalidade",
    [
        "Chat IA",
        "Calcular IMC",
        "Consumo Diário de Água",
        "Histórico"
    ]
)

if menu == "Chat IA":
    pergunta = st.text_input(
        "Digite sua dúvida"
    )

    if st.button("Enviar"):
        if pergunta:
            resposta = gerar_resposta(pergunta)

            st.success(resposta)

            salvar_historico({
                "pergunta": pergunta,
                "resposta": resposta
            })

elif menu == "Calcular IMC":
    peso = st.number_input(
        "Peso (kg)",
        min_value=1.0
    )

    altura = st.number_input(
        "Altura (m)",
        min_value=0.5
    )

    if st.button("Calcular"):
        imc, classificacao = calcular_imc(
            peso,
            altura
        )

        st.info(f"IMC: {imc:.2f}")
        st.success(classificacao)

elif menu == "Consumo Diário de Água":
    peso = st.number_input(
        "Informe seu peso",
        min_value=1.0
    )

    if st.button("Calcular Consumo"):
        agua = calcular_consumo_agua(peso)

        st.success(
            f"Consumo recomendado: {agua:.1f} litros por dia"
        )

elif menu == "Histórico":
    st.write(historico)
