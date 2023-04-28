import pandas as pd

def agrupa_perguntas_respostas(arquivo_csv):
    """Retorna uma lista de listas com as perguntas e suas respectivas respostas."""
    df = pd.read_csv(arquivo_csv, encoding='utf-8')
    perguntas = df['Pergunta'].tolist()
    respostas = df['Resposta'].tolist()
    perg_resp = []
    for i in range(len(perguntas)):
        perg_resp.append([perguntas[i].strip(), respostas[i].strip()])
    return perg_resp