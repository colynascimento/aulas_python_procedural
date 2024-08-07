# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 06/08/2024
# Aula 014 - Funções: Trabalhando com Módulos


def dividir(a, b):
    """Método para dividir 2 números

    Args:
        a (any): Dividendo
        b (any): Divisor

    Returns:
        str: Mensagem de erro ou 'Ok!' se a divisão for bem sucedida
        any: Quociente ou None em caso de erro
    """    
    if b == 0:
        return None, 'Erro de divisão'
    else:
        divisao = a / b
        return divisao, 'Ok!'