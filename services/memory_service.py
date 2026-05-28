
import json
import os

CAMINHO = "data/historico.json"


def carregar_historico():
    if not os.path.exists(CAMINHO):
        return []

    with open(CAMINHO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_historico(dado):
    historico = carregar_historico()

    historico.append(dado)

    with open(CAMINHO, "w", encoding="utf-8") as arquivo:
        json.dump(
            historico,
            arquivo,
            ensure_ascii=False,
            indent=4
        )
