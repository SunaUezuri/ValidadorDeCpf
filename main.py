from valida_cpf import valida_cpf

cpf = input("Digite o número do CPF para validação: ")

valido = valida_cpf(cpf)

if valido:
    print("CPF válido.")
else:
    print("CPF inválido.")