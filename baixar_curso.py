from pyrogram import Client
import os
import time
import re

api_id = api_id  # Seu api_id
api_hash = "api_hash"  # Seu api_hash
canal = "link ou codigo -0000000"  # Link ou codigo do canal que você entrou

pasta_videos = "videos"
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
    mensagens_com_video = [msg for msg in app.get_chat_history(canal) if msg.video]
    total_videos = len(mensagens_com_video)
    print(f"📊 Total de vídeos encontrados: {total_videos}\n")

    # Pergunta o intervalo desejado
    inicio = int(input(f"📥 A partir de qual vídeo deseja baixar? (1 a {total_videos}): "))
    fim = int(input(f"📥 Até qual vídeo deseja baixar? ({inicio} a {total_videos}): "))

    mensagens_filtradas = mensagens_com_video[inicio-1:fim]

    for msg in mensagens_filtradas:
        def limpar_nome(texto):
            texto_limpo = re.sub(r'[\\\\/:*?"<>|]', '', texto)
            return texto_limpo.strip()[:100]

        legenda = msg.caption or f"video_{msg.id}"
        nome_arquivo = limpar_nome(legenda) + ".mp4"
        caminho_completo = os.path.join(pasta_videos, nome_arquivo)

        print(f"\n📥 Baixando {contador + inicio - 1} de {total_videos}: {nome_arquivo}")
        if not os.path.exists(caminho_completo):
            app.download_media(msg.video, file_name=caminho_completo, progress=mostrar_progresso)
            print()
            total_baixados += 1
        else:
            print(f"✅ Já existe: {nome_arquivo}")
        contador += 1

    print(f"\n🎉 Download concluído! Total de vídeos baixados: {total_baixados}")

