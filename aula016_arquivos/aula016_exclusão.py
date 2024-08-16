# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 15/08/2024
# Aula 014 - Arquivos

import csv
import os


os.system('cls')

arquivo = 'aula016_arquivos/arquivos_csv/gravacao/alunas.csv'
nome_para_apagar = input('Digite o nome que deseja apagar: ')

# Lendo os dados do arquivo
with open(arquivo, 'r') as arquivo_csv:
    leitura = csv.DictReader(arquivo_csv, delimiter=';')
    cadastro = list(leitura)
print(cadastro)
    
# Verificando se o nome existe e apagando o registro
apagado = False
novo_cadastro = [registro for registro in cadastro \
                if registro['nome'] != nome_para_apagar]

if len(novo_cadastro) < len(cadastro):
    apagado = True
    
# Reescrevendo o arquivo com os dados atualizados
with open(arquivo, 'w', newline='') as arquivo_csv:
    campos = ['nome', 'telefone', 'cidade']
    escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
    
    escrever.writeheader()
    escrever.writerows(novo_cadastro)
print('-' * 70)
if apagado:
    print(f'Registro com nome {nome_para_apagar} apagado com sucesso.')
else:
    print(f'Registro com nome {nome_para_apagar} não encontrado.')
print('-' * 70)