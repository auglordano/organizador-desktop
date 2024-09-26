import os  # Biblioteca para interagir com o sistema operacional e manipular o sistema de arquivos.
import shutil  # Biblioteca para operações de cópia e movimentação de arquivos.
from datetime import datetime  # Módulo para trabalhar com datas e horários.

# Caminho absoluto da área de trabalho do usuário.
desktopPath = os.path.join(os.path.expanduser("~"), "Desktop")
print(f"Caminho da área de trabalho: {desktopPath}")

# Mapeamento de pastas e extensões de arquivos para organizar.
folderMap = {
    'Imagens': ['.png', '.jpg', '.jpeg', '.gif'],
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.avi', '.mov'], 
    'Músicas': ['.mp3', '.wav', '.acc']
}

def createFolders():
    """
    Cria as pastas necessárias na área de trabalho para organizar os arquivos
    com base nas extensões especificadas em 'folderMap'.

    Para cada pasta (chave) no dicionário 'folderMap', é criado um diretório
    correspondente se ele ainda não existir. Isso ajuda a manter a área de
    trabalho organizada, categorizando arquivos por tipo.

    Exemplos de pastas criadas:
        'Imagens' -> para arquivos com extensão .png, .jpg, .jpeg, .gif.
        'Documentos' -> para arquivos com extensão .pdf, .docx, .txt, .xlsx.

    Retorno:
        None
    """
    for folder in folderMap:
        folderPath = os.path.join(desktopPath, folder)
        if not os.path.exists(folderPath):
            try:
                os.makedirs(folderPath)
                print(f"Pasta criada: {folderPath}")
            except Exception as e:
                print(f"Erro ao criar a pasta {folderPath}: {e}")

def moveFiles():
    """
    Move os arquivos da área de trabalho para as pastas apropriadas
    com base nas suas extensões.

    A função percorre cada arquivo presente na área de trabalho, verifica se
    a extensão corresponde a uma das categorias no dicionário 'folderMap' e,
    se corresponder, move o arquivo para a pasta associada. As operações 
    realizadas são registradas no arquivo de log.

    Retorno:
        None
    """
    for fileName in os.listdir(desktopPath):
        filePath = os.path.join(desktopPath, fileName)

        # Verifica se é um arquivo e não uma pasta.
        if os.path.isfile(filePath):
            fileExtension = os.path.splitext(fileName)[1].lower()
            print(f"Verificando arquivo: {fileName} (Extensão: {fileExtension})")

            # Percorre o folderMap para verificar em qual pasta deve mover o arquivo.
            for folder, extensions in folderMap.items():
                if fileExtension in extensions:
                    newPath = os.path.join(desktopPath, folder, fileName)
                    try:
                        shutil.move(filePath, newPath)
                        logAction(f"Movido: {fileName} para {folder}")
                        print(f"Arquivo movido: {fileName} para {folder}")
                    except Exception as e:
                        print(f"Erro ao mover o arquivo {fileName} para {newPath}: {e}")
                    break
        else:
            print(f"{fileName} não é um arquivo ou está em uso.")

def logAction(action):
    """
    Registra as ações realizadas no processo de organização em um arquivo de log.

    As informações são salvas no arquivo 'desktop_cleanup_log.txt', criado na
    área de trabalho. O log inclui a data e a hora em que a ação foi realizada,
    facilitando o acompanhamento das mudanças na organização.

    Parâmetros:
        action (str): Descrição da ação realizada (e.g., arquivo movido, pasta criada).

    Retorno:
        None
    """
    logFile = os.path.join(desktopPath, 'desktop_cleanup_log.txt')
    try:
        with open(logFile, 'a') as log:
            log.write(f"{datetime.now()}: {action}\n")
        print(f"Log registrado: {action}")
    except Exception as e:
        print(f"Erro ao escrever no log {logFile}: {e}")

def organizeDesktop():
    """
    Função principal que organiza a área de trabalho.

    - Cria as pastas necessárias com base no dicionário 'folderMap'.
    - Move os arquivos para as pastas designadas de acordo com suas extensões.
    - Registra todas as ações em um arquivo de log.

    É chamada uma única vez para executar todo o processo de organização.

    Retorno:
        None
    """
    print("Iniciando a organização da área de trabalho...")
    createFolders()
    print("Pastas criadas (se não existiam).")
    moveFiles()
    print("Arquivos movidos.")
    logAction("Área de trabalho organizada!")
    print("Organização concluída!")

# Chama a função principal para organizar a área de trabalho.
organizeDesktop()
