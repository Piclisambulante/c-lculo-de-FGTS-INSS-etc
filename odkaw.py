import os

def calcular_salario():
    os.system ("cls")
    print("Calculadora de Salário - Detalhamento Passo a Passo\n")
    # Entrada de dados
    salario_bruto = float(input("Digite o salário bruto (ex: 7324.65): ").replace(",", "."))
    periculosidade = input("Informe o percentual de periculosidade (ex: 30 ou deixe vazio): ").strip()
    fgts_percentual = 8  # Percentual fixo de FGTS
    inss_percentual = 14  # Percentual máximo do INSS (ajuste conforme necessário)
    irrf_faixa = [
        (4664.68, 27.5, 869.36),  # Base maior
        (3751.06, 22.5, 636.13),
        (2826.66, 15, 354.80),
        (2112.01, 7.5, 158.40),
        (0, 0, 0)
    ]

    print("\n--- Passo a Passo do Cálculo ---")

    # Cálculo de periculosidade
    if periculosidade:
        periculosidade = float(periculosidade.replace("%", ""))
        valor_periculosidade = salario_bruto * (periculosidade / 100)
        print(f"Periculosidade: {salario_bruto} * ({periculosidade}% / 100) = {valor_periculosidade:.2f}")
        salario_bruto += valor_periculosidade
        print(f"Novo Salário Bruto: Salário Base + Periculosidade = {salario_bruto:.2f}")
    else:
        valor_periculosidade = 0

    # Cálculo do FGTS
    fgts = salario_bruto * (fgts_percentual / 100)
    print(f"FGTS: {salario_bruto:.2f} * ({fgts_percentual}% / 100) = {fgts:.2f}")

    # Cálculo do INSS
    inss = salario_bruto * (inss_percentual / 100)
    print(f"INSS: {salario_bruto:.2f} * ({inss_percentual}% / 100) = {inss:.2f}")

    # Cálculo do IRRF
    base_calculo_irrf = salario_bruto - inss
    print(f"Base de Cálculo IRRF: Salário Bruto - INSS = {salario_bruto:.2f} - {inss:.2f} = {base_calculo_irrf:.2f}")
    irrf = 0
    for faixa in irrf_faixa:
        if base_calculo_irrf > faixa[0]:
            irrf = (base_calculo_irrf * (faixa[1] / 100)) - faixa[2]
            print(f"IRRF: ({base_calculo_irrf:.2f} * {faixa[1]}%) - {faixa[2]} = {irrf:.2f}")
            break
    if irrf == 0:
        print("IRRF: Isento, base de cálculo abaixo da faixa mínima.")

    # Cálculo do salário líquido
    salario_liquido = salario_bruto - inss - irrf - fgts
    print(f"Salário Líquido: Salário Bruto - INSS - IRRF - FGTS = {salario_bruto:.2f} - {inss:.2f} - {irrf:.2f} - {fgts:.2f} = {salario_liquido:.2f}")

    # Exibição do resumo final
    print("\n--- Resumo Final ---")
    print(f"Salário Bruto Final: R$ {salario_bruto:,.2f}")
    print(f"Periculosidade Adicional: R$ {valor_periculosidade:,.2f}")
    print(f"FGTS: R$ {fgts:,.2f}")
    print(f"INSS: R$ {inss:,.2f}")
    print(f"IRRF: R$ {irrf:,.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:,.2f}")

# Chama a função
calcular_salario()
