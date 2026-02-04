from abc import ABC, abstractmethod
from gemini_client import chamar_gemini_para_analise # Importando do outro arquivo

# --- Interface Base ---
class AnalisadorStrategy(ABC):
    @abstractmethod
    def analisar(self, texto_curriculo: str) -> dict:
        pass

# --- Módulo Aprendiz/Estagiário ---
class AnalisadorAprendizEstagiario(AnalisadorStrategy):
    def __init__(self):
        self.pesos = {
            "fit_cultural": 0.4,
            "escolaridade": 0.3,
            "vontade_aprender": 0.2,
            "conhecimento_basico": 0.1
        }
    
    def analisar(self, texto_curriculo):
        print(" -> Analisando perfil APRENDIZ/ESTAGIÁRIO via Gemini...")
        notas = chamar_gemini_para_analise(texto_curriculo, self.pesos)
        score_final = sum(notas[k] * peso for k, peso in self.pesos.items())
        return {"nivel": "Aprendiz/Estágio", "score": round(score_final, 1), "detalhes": notas, "aprovado": score_final >= 70}

# --- Módulo Júnior ---
class AnalisadorJunior(AnalisadorStrategy):
    def __init__(self):
        self.pesos = {
            "stack_tecnologica": 0.4,
            "projetos_pessoais": 0.3,
            "logica_programacao": 0.2,
            "ingles": 0.1
        }

    def analisar(self, texto_curriculo):
        print(" -> Analisando perfil JÚNIOR via Gemini...")
        notas = chamar_gemini_para_analise(texto_curriculo, self.pesos)
        score_final = sum(notas[k] * peso for k, peso in self.pesos.items())
        return {"nivel": "Júnior", "score": round(score_final, 1), "detalhes": notas, "aprovado": score_final >= 75}
    
# --- Módulo Pleno ---
class AnalisadorPleno(AnalisadorStrategy):
    def __init__(self):
        self.pesos = {
            "autonomia_entrega": 0.3,
            "dominio_stack": 0.3,
            "resolucao_bugs": 0.2,
            "boas_praticas_code": 0.2
        }

    def analisar(self, texto_curriculo):
        print(" -> Analisando perfil PLENO via Gemini...")
        notas = chamar_gemini_para_analise(texto_curriculo, self.pesos)
        
        score_final = sum(notas[k] * peso for k, peso in self.pesos.items())
        
        return {
            "nivel": "Pleno", 
            "score": round(score_final, 1), 
            "detalhes": notas, 
            "aprovado": score_final >= 80
        }

# --- Módulo Sênior ---
class AnalisadorSenior(AnalisadorStrategy):
    def __init__(self):
        self.pesos = {
            "experiencia_lideranca": 0.3,
            "arquitetura_software": 0.3,
            "resolucao_problemas_complexos": 0.2,
            "stack_avancada": 0.2
        }

    def analisar(self, texto_curriculo):
        print(" -> Analisando perfil SÊNIOR via Gemini...")
        notas = chamar_gemini_para_analise(texto_curriculo, self.pesos)
        score_final = sum(notas[k] * peso for k, peso in self.pesos.items())
        return {"nivel": "Sênior", "score": round(score_final, 1), "detalhes": notas, "aprovado": score_final >= 85}