# Web Data Bridge & Companion API
> Arquitetura modular e escalável conectando extensões web (Manifest V3) a uma API local em Python para automação e exportação de dados.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-REST%20API-lightgrey.svg)
![Extension](https://img.shields.io/badge/Chrome-Manifest%20V3-blue.svg)

---

### ⏱️ Impacto de Negócio & Horas Economizadas (Pé no chão)
- **Fluxo Web-to-Desktop sem Atrito:** Elimina o ciclo manual de *"exportar CSV do navegador -> abrir pasta Downloads -> abrir Excel -> copiar e colar dados -> formatar"*.
- **Economia Operacional Real:** Economia estimada de **~30 a 45 minutos diários** em tarefas repetitivas de extração administrativa.
- **Escalabilidade:** Permite que qualquer página web envie dados estruturados diretamente para relatórios locais em 1 clique.

---

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

### 2. Carregar a Extensão
1. Abra o Google Chrome e acesse `chrome://extensions/`.
2. Ative o **Modo do desenvolvedor**.
3. Clique em **Carregar sem compactação** e selecione a pasta `extension/`.
