from pyrogram import Client
import os
import time
import re

api_id = api_id
api_hash = "api_hash"
canal = "link ou codigo -0000000"

pasta_videos = "nomecurso"
os.makedirs(pasta_videos, exist_ok=True)

# Função de progresso
def mostrar_progresso(current, total):
    porcentagem = (current / total) * 100
    atual_mb = current / 1024 / 1024
    total_mb = total / 1024 / 1024
    print(f"\r🔄 Progresso: {atual_mb:.2f} MB de {total_mb:.2f} MB ({porcentagem:.2f}%)", end='')

app = Client("minha_sessao", api_id=api_id, api_hash=api_hash)

with app:
    offset_id = 0
    total_baixados = 0
    contador = 1

    print("🔎 Contando vídeos...")
    total_videos = sum(1 for msg in app.get_chat_history(canal) if msg.video)
    print(f"📊 Total de vídeos encontrados: {total_videos}\n")

    while True:
        mensagens = app.get_chat_history(canal, offset_id=offset_id, limit=100)
        if not mensagens:
            break

        for msg in mensagens:
            offset_id = msg.id

            if msg.video:
                def limpar_nome(texto):
                    # Remove caracteres proibidos para nome de arquivo
                    texto_limpo = re.sub(r'[\\\\/:*?"<>|]', '', texto)
                    return texto_limpo.strip()[:100]  # Limita a 100 caracteres

                # Usa a legenda como nome, se houver — senão usa um nome padrão
                legenda = msg.caption or f"video_{msg.id}"
                nome_arquivo = limpar_nome(legenda) + ".mp4"
                caminho_completo = os.path.join(pasta_videos, nome_arquivo)

                if not os.path.exists(caminho_completo):
                    print(f"\n📥 Baixando {contador} de {total_videos}: {nome_arquivo}")
                    app.download_media(msg.video, file_name=caminho_completo, progress=mostrar_progresso)
                    print()  # quebra de linha após progresso
                    total_baixados += 1
                else:
                    print(f"✅ Já existe: {nome_arquivo}")

                contador += 1

    print(f"\n🎉 Download concluído! Total de vídeos baixados: {total_baixados}")
