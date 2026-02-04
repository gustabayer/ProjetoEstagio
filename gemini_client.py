from google import genai
from google.genai import types
import json
import re
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API Key não encontrada. Verifique o arquivo .env")

client = genai.Client(api_key=api_key)

def limpar_resposta_json(texto_resposta):
    padrao = r"```json\s*(.*?)\s*```"
    match = re.search(padrao, texto_resposta, re.DOTALL)
    if match:
        texto_resposta = match.group(1)
    
    texto_resposta = texto_resposta.replace("```", "").strip()
    return texto_resposta

def chamar_gemini_para_analise(texto_curriculo, criterios_pesos):
    lista_criterios = list(criterios_pesos.keys())
    
    # Prompt reforçado
    prompt = f"""
    Atue como um sistema de ATS (Applicant Tracking System).
    Analise o texto do currículo abaixo e extraia notas de 0 a 100 para os seguintes critérios:
    {lista_criterios}

    Contexto para avaliação:
    - Stack Tecnológica: Procure por linguagens e frameworks modernos citados.
    - Projetos Pessoais: Considere projetos de extensão universitária, projetos acadêmicos, TCCs, links de GitHub e projetos práticos de cursos (Udemy/Alura).
    - Experiência: Considere estágios, monitorias acadêmicas e freelances como válidos.
    
    REGRAS TÉCNICAS OBRIGATÓRIAS:
    1. Responda ESTRITAMENTE um JSON válido.
    2. NÃO use Markdown na resposta.
    3. Use aspas duplas para chaves e valores.
    4. Se o texto do currículo parecer vazio ou ilegível, retorne notas 0.

    Currículo:
    {texto_curriculo}
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.1,
                response_mime_type="application/json"
            )
        )
        
        texto_limpo = limpar_resposta_json(response.text)
        dados = json.loads(texto_limpo)
        return dados

    except Exception as e:
        print(f"⚠️ Erro na API (Novo SDK): {e}")
        return {k: 0 for k in lista_criterios}