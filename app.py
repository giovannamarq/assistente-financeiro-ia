import os
from pypdf import PdfReader
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = os.environ.get("GOOGLE_API_KEY", "COLOQUE_SUA_CHAVE_AQUI")

print("A carregar e a estruturar o extrato PDF...")
leitor_pdf = PdfReader("NU_672372683_01MAI2026_31MAI2026.pdf")

texto_completo_extrato = ""
for i, pagina in enumerate(leitor_pdf.pages):
    texto_completo_extrato += f"\n--- PÁGINA {i+1} ---\n"
    texto_completo_extrato += pagina.extract_text()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.1) 

print("\n🤖 Assistente Financeiro IA Avançado Ativo! (Digite 'sair' para encerrar)")
print("-" * 50)

while True:
    pergunta_usuario = input("\nVocê: ")
    
    if pergunta_usuario.lower() == 'sair':
        print("Atendimento encerrado. Até breve! 👋")
        break
        
    if not pergunta_usuario.strip():
        continue

    prompt = f"""
    Você é um assistente financeiro especialista em análise de extratos bancários.
    Analise o extrato fornecido abaixo para responder às perguntas com total precisão matemática.
    
    ATENÇÃO ÀS REGRAS:
    1. Faça as contas e validações passo a passo antes de dar o resultado final.
    2. Se a pergunta for sobre um dia específico, localize esse dia no extrato e verifique todas as entradas e saídas listadas abaixo dele.
    3. Responda de forma direta, clara e amigável.

    DADOS COMPLETOS DO EXTRATO:
    {texto_completo_extrato}

    Pergunta do Utilizador: {pergunta_usuario}
    Resposta Analítica:
    """

    try:
        resposta_final = llm.invoke(prompt)
        print(f"Assistente IA: {resposta_final.content}")
    except Exception as e:
        print(f"Erro ao consultar o Gemini: {e}")