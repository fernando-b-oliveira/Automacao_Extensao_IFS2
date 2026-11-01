# Web Data Bridge & Companion API
> Arquitetura modular e escalável conectando extensões web (Manifest V3) a uma API local em Python para automação e exportação de dados.

## 📌 Visão Geral
Este projeto demonstra o padrão arquitetural **Browser Extension + Local Bridge Server**:
- A extensão web interage com páginas dinâmicas, extrai dados estruturados sob demanda e os despacha via HTTP assíncrono.
- O servidor local (Flask) recebe os registros validados e gerencia a persistência contínua em planilhas (`Excel / CSV`) sem travar o navegador ou expor credenciais na nuvem.

## 🚀 Arquitetura
```
[Navegador Web / DOM] 
       │ (JSON via Fetch)
       ▼
[Local Bridge - Flask API (Porta 5000)]
       │ (Pandas / OpenPyXL)
       ▼
[Planilhas Formatadas - /exports/*.xlsx]
```

## 🛠️ Tecnologias Utilizadas
- **Backend:** Python 3.9+, Flask, Flask-CORS, Pandas, OpenPyXL.
- **Frontend / Extensão:** JavaScript ES6, Manifest V3.

## 📦 Como Executar

### 1. Iniciar o Servidor Companion
```bash
pip install flask flask-cors pandas openpyxl
python server.py
```

O servidor iniciará em `http://127.0.0.1:5000`.

### 2. Carregar a Extensão
1. Abra o Google Chrome e acesse `chrome://extensions/`.
2. Ative o **Modo do desenvolvedor** no canto superior direito.
3. Clique em **Carregar sem compactação** e selecione a pasta `extension/`.

### 3. Teste Rápido via Terminal
```bash
curl -X POST http://127.0.0.1:5000/api/v1/export \
  -H "Content-Type: application/json" \
  -d "{\"collection\":\"exemplo_teste\",\"records\":[{\"item\":\"A1\",\"status\":\"OK\"}]}"
```

## 🛡️ Segurança e Governança
- O servidor roda vinculado a `127.0.0.1` (loopback local).
- Não há armazenamento de credenciais ou dados corporativos confidenciais neste repositório.
- Licença: MIT
