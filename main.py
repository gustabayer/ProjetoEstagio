import os
import pdfplumber
from analisadores import AnalisadorAprendizEstagiario, AnalisadorJunior, AnalisadorPleno, AnalisadorSenior

# --- 1. Função de Leitura ---
def extrair_texto_pdf_robusto(caminho_arquivo):
    text_content = ""
    try:
        with pdfplumber.open(caminho_arquivo) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text_content += extracted + "\n"
        return text_content
    except Exception as e:
        print(f"⚠️  Erro ao ler arquivo: {e}")
        return None

# --- 2. O Sistema ---
class SistemaRecrutamentoIA:
    def __init__(self):
        self.analisadores = {
            "aprendiz": AnalisadorAprendizEstagiario(),
            "estagiario": AnalisadorAprendizEstagiario(),
            "junior": AnalisadorJunior(),
            "pleno": AnalisadorPleno(),
            "senior": AnalisadorSenior()
        }
    
    def processar(self, texto_cv, nivel_vaga):
        nivel = nivel_vaga.lower().strip()
        if nivel not in self.analisadores:
            return {"erro": f"Nível '{nivel_vaga}' inválido."}
        
        return self.analisadores[nivel].analisar(texto_cv)

# --- 3. Exibição ---
def mostrar_relatorio(nome_arquivo, resultado):
    print("\n" + "="*60)
    print(f"📄 ARQUIVO: {nome_arquivo}")
    
    if "erro" in resultado:
        print(f"❌ ERRO: {resultado['erro']}")
        return

    status_icon = "✅" if resultado['aprovado'] else "❌"
    print(f"🎯 Nível Aplicado: {resultado['nivel'].upper()}")
    print(f"🏆 Pontuação: {resultado['score']} / 100")
    print(f"Situação: {status_icon} {'APROVADO' if resultado['aprovado'] else 'REPROVADO'}")
    print("-" * 60)
    print("Detalhes da Avaliação:")
    for k, v in resultado['detalhes'].items():
        print(f"   • {k.replace('_', ' ').title().ljust(30)}: {v}")
    print("="*60)

# --- 4. Execução Principal (Escolha Manual) ---
if __name__ == "__main__":
    sistema = SistemaRecrutamentoIA()
    pasta = "Arquivos" 
    
    # Verifica pasta
    if not os.path.exists(pasta):
        print(f"❌ Erro: A pasta '{pasta}' não existe.")
        exit()

    # 1. Mostra o que tem na pasta para facilitar
    print(f"📂 Arquivos disponíveis em '{pasta}':")
    arquivos_disponiveis = [f for f in os.listdir(pasta) if f.lower().endswith('.pdf')]
    
    if not arquivos_disponiveis:
        print("❌ Nenhum PDF encontrado.")
        exit()
        
    for arq in arquivos_disponiveis:
        print(f"   📄 {arq}")
    
    print("-" * 30)

    # 2. Pede para o usuário digitar
    nome_digitado = input("Digite o nome do arquivo (ex: cv.pdf): ").strip()

    # 3. Monta o caminho
    caminho_completo = os.path.join(pasta, nome_digitado)
    
    # Se o usuário esqueceu de digitar ".pdf", a gente tenta adicionar
    if not os.path.exists(caminho_completo) and not nome_digitado.lower().endswith(".pdf"):
        caminho_completo += ".pdf"
        nome_digitado += ".pdf"

    # 4. Verifica e processa
    if os.path.exists(caminho_completo):
        texto = extrair_texto_pdf_robusto(caminho_completo)
        
        if texto and len(texto) > 50:
            nivel = input("Qual o nível da vaga? (Aprendiz/Junior/Pleno/Senior): ")
            print(f"\n🚀 Analisando {nome_digitado}...")
            
            resultado = sistema.processar(texto, nivel)
            mostrar_relatorio(nome_digitado, resultado)
        else:
            print("⚠️ Erro: PDF vazio ou ilegível.")
    else:
        print(f"❌ Erro: O arquivo '{nome_digitado}' não foi encontrado na pasta '{pasta}'.")