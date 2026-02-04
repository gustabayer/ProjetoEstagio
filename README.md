# Analisador de Currículos com IA (Gemini 2.5)
Este projeto é uma ferramenta de automação para Recrutamento e Seleção que utiliza a Inteligência Artificial do Google Gemini para ler currículos em PDF, analisar critérios técnicos e comportamentais, e atribuir uma nota de 0 a 100 baseada na senioridade da vaga.

## 🚀 Funcionalidades
- **Leitura de PDF:** Extrai texto de arquivos PDF (mesmo com layouts complexos) usando `pdfplumber`.
- **Análise por Senioridade:** Utiliza estratégias de avaliação diferentes para cada nível:
    - **Aprendiz/Estagiário:** Foco em Soft Skills e Vontade de Aprender.
    - **Júnior:** Foco em Projetos Pessoais, Portfólio e Stack Básica.
    - **Pleno:** Foco em Autonomia e Resolução de Problemas.
    - **Sênior:** Foco em Arquitetura, Liderança e Experiência.
- **Critérios Personalizados:** Pesos ajustáveis para cada ompetência.
- **Integração Google Gemini:** Usa o SDK mais recente (`google.genai`) com o modelo Gemini 2.5 Flash.,

## 🛠️ Pré-requisitos
- Python 3.10 ou superior instalado.
- Uma **API Key** do Google AI Studio (Gemini).

## 📦 Instalação
1. **Clone o projeto** (ou baixe a pasta):
```bash
git clone https://seu-repositorio.git
cd analisador-cv-ia
```

2. **Crie um ambiente virtual** (opcional, mas recomendado):
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install google-genai pdfplumber python-dotenv
```

## ⚙️ Configuração
1. Na raiz do projeto, crie um arquivo chamado `.env` (sem nome antes do ponto).
2. Adicione sua chave de API dentro dele:
```
GEMINI_API_KEY=Cole_Sua_Chave_Aqui_Sem_Aspas
```
3. Crie uma pasta chamada `Arquivos` na raiz do projeto. É aqui que você colocará os PDFs dos candidatos.

## 🖥️ Como Usar
1. Coloque o currículo em PDF na pasta `Arquivos/`.
2. Execute o sprint principal:
```bash
python main.py
```
3. O sistema listará os arquivos disponíveis. Digite o nome do arquivo desejado (ex: `candidato.pdf`).
4. Digite o nível da vaga (ex.: `Junior`, `Pleno`, `Senior`).
5. A IA fará a análise e exibirá o relatório no terminal.

**Exemplo de saída:**
```
============================================================
📄 ARQUIVO: candidato_joao.pdf
🎯 Nível Aplicado: JÚNIOR
🏆 Pontuação: 85.0 / 100
Situação: ✅ APROVADO
------------------------------------------------------------
Detalhes da Avaliação:
   • Stack Tecnologica             : 90
   • Projetos Pessoais             : 80
   • Logica Programacao            : 85
   • Ingles                        : 70
============================================================
```

## 📂 Estrutura do Projeto
```
analisador-cv-ia/
│
├── Arquivos/              # Pasta onde você coloca os PDFs
│   └── curriculo.pdf
│
├── .env                   # Arquivo de configuração (NÃO COMPARTILHAR)
├── main.py                # Arquivo principal (Executar este)
├── analisadores.py        # Lógica de pesos e níveis (Strategy Pattern)
├── gemini_client.py       # Conexão com a IA (SDK google-genai)
└── README.md              # Documentação
```

## 🧠 Como a IA Pensa (Critérios)
O sistema utiliza pesos diferentes para calcular a nota final. Você pode alterar esses pesos no arquivo `analisadores.py`.

| Nível | Critério Principal | Peso Maior | Nota de Corte |
| :--- | :--- | :--- | :--- |
| **Estagiário** | Potencial e Comportamento | Fit Cultural (40%) | 70 pontos |
| **Júnior** | Execução e Portfólio | Stack Técnica (40%) | 75 pontos |
| **Pleno** | Autonomia | Autonomia/Entrega (30%) | 80 pontos |
| **Sênior** | Estratégia | Experiência/Liderança (40%) | 85 pontos |

## ⚠️ Solução de Problemas Comuns
**Erro: "API Key não encontrada"**
- Verifique se o arquivo `.env` está criado corretamente e se o nome da variável é `GEMINI_API_KEY`.

**Erro: "PDF vazio ou ilegível"**
- O currículo provavelmente é uma imagem (escaneada) ou foi salvo em um formato que o leitor de PDF não reconhece.
- _Solução:_ Tente selecionar o texto do PDF com o mouse. Se não conseguir, a IA também não conseguirá ler. Peça ao candidato uma versão em texto/Word salvo como PDF.