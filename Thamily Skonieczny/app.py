from oopenpyxl import load_workbook
from docx import Document

# 1. Carrega o arquivo Excel
caminho_excel = "fornecedores.xlsx" # Certifique-se de que o caminho está correto
workbook = load_workbook(caminho_excel)
sheet = workbook.active

# 2. Lê o contrato base (agora diretamento no Word)
for row in sheet.iter_rows(min_row=2, values_only=True): # Ignora o cabeçalho (linha 1)
    nome_empresa, endereco, cidade, estado, cep, telefone, email, setor = row

    # 3. Cria um novo documento Word para cada fornecedor
    doc = Document()

    # 4. Adiciona o texto do contrato com os dados substituidos 
    contrato = """
    Este contrato de prestação de serviços é feito entre {nome_empresa}, com endereço em {endereco}, {cidade}, {estado}, CEP {cep}, doravante dormindo FORNECEDOR, e a empresa CONTRATANTE.

    Pelo presente instrumento particular, as partes têm, entre si, justo e acordado o seguinte:

    1. OBJETO DO CONTRATO
    O FORNECEDOR compromete-se a fornecer à CONTRATANTE os serviços/material de {setor}, respeitando os padrões de qualidade e os prazos estipulados.

    2. PRAZO
    Este contrato tem prazo de vigência de 12 (doze) meses, indicando-se na data de sua assinatura.

    3. VALOR E FORMA DE PAGAMENTO
    O valor será acordado conforme demanda. Pagamentos mensais mediante nota fiscal.

    4. CONFIDENCIALMENTE
    Todas as informações trocadas serão tratadas como confidenciais.

    FORNECEDOR: {nome, empresa}
    E-mail: {email}

    CONTRATANTE: [NOME CONTRATANTE]
    E-mail: [E-MAIL CONTRATANTE]

    {cidade}, [DATA]
    """

    doc.add_paragraph(contrato)

    # 5. Salva o contrato em Word
    nome_arquivo = f"Contrato_{nome_empresa.replace('', '_')}.docx"
    doc.save(nome_arquivo)
    print(f"Contrato gerado: {nome_arquivo}")

print("Proceso concluído! Todos os contratos foram criados.")
