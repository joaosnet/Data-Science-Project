# %%
import pandas as pd  # Importa a biblioteca pandas
import streamlit as st  # Importa a biblioteca streamlit
import joblib  # Importa a biblioteca joblib

# Carrega o modelo de aprendizado de máquina pré-treinado
# modelo = joblib.load('modelo.joblib')

x_numericos = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0,
               'minimum_nights': 0, 'ano': 0, 'mes': 0, 'n_amenities': 0, 'host_listings_count': 0}

x_tf = {'host_is_superhost': 0, 'instant_bookable': 0}

x_listas = {'property_type': ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House', 'Loft', 'Outros', 'Serviced apartment'],
            'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
            'cancellation_policy': ['flexible', 'moderate', 'strict', 'strict_14_with_grace_period']
            }

dicionario = {}  # Cria um dicionário vazio
for item in x_listas:  # Para cada item nas listas de x_listas
    for valor in x_listas[item]:  # Para cada valor no item atual
        dicionario[f'{item}_{valor}'] = 0  # Adiciona uma chave-valor ao dicionário

for item in x_numericos:  # Para cada item nos valores numéricos
    if item == 'latitude' or item == 'longitude':  # Se o item for latitude ou longitude
        valor = st.number_input(f'{item}', step=0.00001, value=0.0, format="%.5f")  # Lê um número de entrada do usuário
    elif item == 'extra_people':  # Se o item for extra_people
        valor = st.number_input(f'{item}', step=0.01, value=0.0)  # Lê um número de entrada do usuário
    else:
        valor = st.number_input(f'{item}', step=1, value=0)  # Lê um número de entrada do usuário
    x_numericos[item] = valor  # Atualiza o valor no dicionário x_numericos

for item in x_tf:  # Para cada item nos valores booleanos
    valor = st.selectbox(f'{item}', ('Sim', 'Não'))  # Lê uma opção de seleção do usuário
    if valor == "Sim":  # Se o valor for "Sim"
        x_tf[item] = 1  # Atualiza o valor no dicionário x_tf para 1
    else:
        x_tf[item] = 0  # Atualiza o valor no dicionário x_tf para 0

for item in x_listas:  # Para cada item nas listas de x_listas
    valor = st.selectbox(f'{item}', x_listas[item])  # Lê uma opção de seleção do usuário
    dicionario[f'{item}_{valor}'] = 1  # Atualiza o valor no dicionário dicionario para 1

botao = st.button('Prever Valor do Imóvel')  # Cria um botão com o texto 'Prever Valor do Imóvel'

# if botao:
#     dicionario.update(x_numericos)
#     dicionario.update(x_tf)
#     valores_x = pd.DataFrame(dicionario, index=[0])

#     dados = pd.read_csv('dados.csv')
#     colunas = list(dados.columns)[1:-1]

#     modelo = joblib.load('modelo.joblib')
#     preco = modelo.predict(valores_x)
#     st.write(preco[0])

if botao:  # Se o botão for pressionado
    dicionario.update(x_numericos)  # Atualiza o dicionário dicionario com os valores numéricos
    dicionario.update(x_tf)  # Atualiza o dicionário dicionario com os valores booleanos
    valores_x = pd.DataFrame(dicionario, index=[0])  # Cria um DataFrame a partir do dicionário

    dados = pd.read_csv('dados.csv')  # Lê os dados de um arquivo CSV
    colunas = list(dados.columns)[1:-1]  # Obtém as colunas do DataFrame, excluindo a primeira e a última

    valores_x = valores_x[colunas]  # Seleciona apenas as colunas presentes no DataFrame de dados

    # Carrega o modelo de aprendizado de máquina pré-treinado
    modelo = joblib.load('modelo.joblib')

    # Faz a previsão do valor da propriedade com base nos valores de entrada fornecidos pelo usuário
    try:
        valor_predito = modelo.predict(valores_x)[0]  # Faz a previsão do valor da propriedade
        st.success(f'O valor previsto da propriedade é R$ {valor_predito:.2f}')  # Exibe o valor previsto com duas casas decimais
    except Exception as e:
        st.error(f'Ocorreu um erro ao prever o valor da propriedade: {e}')  # Exibe uma mensagem de erro se ocorrer algum problema
