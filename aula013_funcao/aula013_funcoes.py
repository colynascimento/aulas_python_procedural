# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 09/07/2024
# Aula 013 - Funções

def limpa_tela():
    """Função para limpar o terminal
    """    
    import os
    
    
    os.system('cls')
    
def soma(a, b):
    """Função para somar dois números

    Args:
        a (int): valor de a
        b (int): valor de b

    Returns:
        Retorna a soma de dois números
    """    
    return a + b

def firula():
    print('-' * 70)
    
# Programa principal

# Chamando a função
limpa_tela()
firula()
resposta = soma(1, 2)
print(f'A soma de dois números é: {resposta}')
firula()
print()