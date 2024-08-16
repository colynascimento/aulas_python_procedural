# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 15/08/2024
# Aula 014 - Arquivos

import csv
import os


os.system('cls')

arquivo = 'aula016_arquivos/arquivos_csv/gravacao/alunas.csv'
coluna_para_alteracao = input('Digite a coluna que deseja editar: ')
celula_para_alteracao = input('Digite a célula que deseja editar: ')

# Lendo os dados do arquivo
with open(arquivo, 'r') as arquivo_csv:
    leitura = csv.DictReader(arquivo_csv, delimiter=';')
    linhas = list(leitura)
    campos = ['nome', 'telefone', 'cidade']
    
    # Verifica se a coluna e a célula escolhida estão dentro do arquivo e substitui
    if coluna_para_alteracao in campos:
        for cadastro in linhas:
            print(cadastro)
            # if cadastro == celula_para_alteracao:
            #     nova_celula = input('Digite o novo conteúdo da célula: ')
                
