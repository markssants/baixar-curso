# Telegram Video Downloader

Um script em Python para baixar **todos os vídeos** de um canal do Telegram, incluindo canais privados (usando o chat ID interno).

## ⚙️ Pré-requisitos

- Python 3.10+ instalado no sistema
- Uma conta Telegram ativa
- Uma API no [Telegram] (https://my.telegram.org/auth)
- Acesso ao canal (você precisa **entrar no canal primeiro**, mesmo que seja privado)

## 🧪 Instalação

```bash
mkdir baixar_curso
cd baixar_curso
python3 -m venv venv
source venv/bin/activate
pip install pyrogram tgcrypto
```

## 🔑 Configurar API ID e Hash

1. Vá em [https://my.telegram.org](https://my.telegram.org)
2. Faça login e crie um aplicativo
3. Pegue o `api_id` e o `api_hash`
4. Preencha essas variáveis nos scripts `descobrir_id.py` e `baixar_videos.py`

## 🔍 Como descobrir o chat ID do canal

Se o canal for **privado** ou estiver acessível via link de convite (`https://t.me/+...`), o Pyrogram **não aceita esse link direto**. Você precisa descobrir o `chat_id`.

### Faça isso **apenas uma vez**:

1. **Entre no canal** manualmente pelo Telegram
2. Rode o script:

```bash
python descobrir_id.py
```

Ele vai imprimir algo como:

```
🆔 chat_id do canal: -1001234567890
```

3. Copie esse número e substitua no script principal:

```python
canal = -1001234567890
```

## ▶️ Como executar o bot para baixar os vídeos

Depois de configurar o `chat_id`, rode:

```bash
python baixar_curso.py
```

## 📁 Estrutura esperada

```
baixar_curso/
├── baixar_curso.py
├── descobrir_id.py
├── executar.sh
└── minha_sessao.session 
└── minha_sessao.session-journal
└── README.md
├── videos/
├── venv/
```

## 🛑 Observações

- O arquivo `minha_sessao.session` será gerado após o primeiro login.
- Esse arquivo autentica você automaticamente nas execuções seguintes.
- O script **não baixa novamente vídeos já salvos**.
