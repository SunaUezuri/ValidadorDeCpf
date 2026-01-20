def valida_cpf(cpf: str) -> bool:
    """
    Valida um número de CPF.

    Parâmetros:
    cpf (str): O número do CPF a ser validado. Deve conter apenas dígitos.

    Retorna:
    bool: True se o CPF for válido, False caso contrário.
    """

    # Limpa o CPF removendo caracteres não numéricos
    cpf = limpar_cpf(cpf)

    # Verifica se todos os dígitos são iguais
    if not tem_11_digitos(cpf) or todos_digitos_iguais(cpf):
        return False

    digito1 = calcular_digito(cpf[:9], 10)
    digito2 = calcular_digito(cpf[:9] + str(digito1), 11)

    return cpf[-2:] == f"{digito1}{digito2}"

def limpar_cpf(cpf: str) -> str:
    """
    Remove caracteres não numéricos de um número de CPF.

    Parâmetros:
    cpf (str): O número do CPF a ser limpo.

    Retorna:
    str: O CPF contendo apenas dígitos.
    """
    return ''.join(filter(str.isdigit, cpf))

def tem_11_digitos(cpf: str) -> bool:
    """
    Verifica se o CPF contém exatamente 11 dígitos.

    Parâmetros:
    cpf (str): O número do CPF a ser verificado.

    Retorna:
    bool: True se o CPF tiver 11 dígitos, False caso contrário.
    """
    return len(cpf) == 11

def todos_digitos_iguais(cpf: str) -> bool:
    """
    Verifica se todos os dígitos do CPF são iguais.

    Parâmetros:
    cpf (str): O número do CPF a ser verificado.

    Retorna:
    bool: True se todos os dígitos forem iguais, False caso contrário.
    """
    return cpf == cpf[0] * len(cpf)

def calcular_digito(cpf: str, peso_inicial: int) -> int:
    """
    Calcula o dígito verificador do CPF.

    Parâmetros:
    cpf (str): O número do CPF sem os dígitos verificadores.
    peso_inicial (int): O peso inicial para o cálculo.

    Retorna:
    int: O dígito verificador calculado.
    """
    soma = sum(int(cpf[i]) * (peso_inicial - i) for i in range(len(cpf)))
    digito = (soma * 10 % 11) % 10
    return digito