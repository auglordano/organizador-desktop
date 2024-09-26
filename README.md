# Organizador de Área de Trabalho

Organização da Área de Trabalho antes do script: 

![desktopa](https://github.com/user-attachments/assets/c3f65b16-d027-4c53-b152-25a98ef6e872)

Organização da Área de Trabalho depois do script:

![desktopd](https://github.com/user-attachments/assets/870b83c6-99e6-46ac-b00c-13b7c9fc12e6)

## Sobre o Projeto

O **Organizador de Área de Trabalho** é um script Python simples e eficiente, criado para automatizar a organização dos arquivos presentes na área de trabalho. Ele categoriza os arquivos em pastas específicas com base em suas extensões, proporcionando uma área de trabalho mais limpa e ordenada.

Esse projeto foi desenvolvido com o intuito de ajudar usuários que frequentemente deixam arquivos acumularem de forma desorganizada, sendo especialmente útil para pessoas que trabalham com múltiplos tipos de documentos, imagens e vídeos. Além disso, é um ótimo exemplo de como utilizar bibliotecas padrão do Python para automação de tarefas do dia a dia.

## Por que esse projeto foi criado?

O objetivo principal deste projeto é demonstrar habilidades em Python, manipulação de arquivos e organização do sistema de arquivos. Para profissionais que lidam com ambientes de desenvolvimento e trabalham frequentemente em desktops, essa automação economiza tempo e evita distrações causadas pela desordem.

Além disso, este projeto serve como um exemplo prático para mostrar como pequenas ferramentas podem ser úteis para melhorar a produtividade no dia a dia.

## Instalação e Execução

### Pré-requisitos

Para rodar esse script em seu ambiente local, você precisará de:

- **Python 3.6+**: Verifique se o Python está instalado utilizando o comando `python --version`.
- Biblioteca `shutil` (inclusa na biblioteca padrão do Python)
- Biblioteca `os` (inclusa na biblioteca padrão do Python)
- Biblioteca `datetime` (inclusa na biblioteca padrão do Python)

### Instalação

1. Clone este repositório em sua máquina local:
   ```bash
   git clone https://github.com/seu-usuario/organizador-de-area-de-trabalho.git

2. Acesse o diretório do projeto:
   ```bash
   cd organizador-de-area-de-trabalho

3. (Opcional) Crie um ambiente virtual para gerenciar as dependências do Python:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate  # Windows

4. Execute o script diretamente no terminal:
   ```bash
   python DesktopOrganizer.py

## Funcionalidades

O script possui as seguintes funcionalidades principais:

1. **Criação Automática de Pastas:**
   - Cria pastas específicas na área de trabalho para diferentes tipos de arquivos, como:
     - **Imagens:** `.png`, `.jpg`, `.jpeg`, `.gif`
     - **Documentos:** `.pdf`, `.docx`, `.txt`, `.xlsx`
     - **Vídeos:** `.mp4`, `.avi`, `.mov`
     - **Músicas:** `.mp3`, `.wav`, `.acc`

2. **Movimentação de Arquivos:**
   - Move automaticamente os arquivos da área de trabalho para suas respectivas pastas com base nas extensões.

3. **Registro de Ações:**
   - Cria um arquivo `desktop_cleanup_log.txt` na área de trabalho para registrar todas as ações realizadas, incluindo pastas criadas, arquivos movidos e qualquer erro que tenha ocorrido.

4. **Identificação de Tipos de Arquivos:**
   - Verifica a extensão dos arquivos para decidir em qual pasta deve ser movido, ignorando pastas e arquivos do sistema.

5. **Mensagens de Status:**
   - Exibe mensagens no console durante a execução para informar o status das operações, como criação de pastas, movimentação de arquivos e registro de logs.

## Como Funciona

### Estrutura do Diretório
Após executar o script, a estrutura da sua área de trabalho será organizada da seguinte forma:

Área de Trabalho/ │ ├── Imagens/ │ ├── exemplo.png │ └── foto.jpeg │ ├── Documentos/ │ ├── relatório.pdf │ └── texto.docx │ ├── Videos/ │ └── video.mp4 │ ├── Músicas/ │ └── música.mp3 │ └── desktop_cleanup_log.txt


### Logs de Execução

O arquivo `desktop_cleanup_log.txt` será criado na sua área de trabalho e conterá informações sobre cada ação realizada, como no exemplo:

```bash
2024-09-26 14:23:01: Movido: exemplo.png para Imagens 
2024-09-26 14:23:01: Movido: relatório.pdf para Documentos
2024-09-26 14:23:02: Área de trabalho organizada!
```

## Sugestões para Melhorias Futuras

1. **Configuração Personalizada:** Permitir ao usuário configurar extensões e diretórios diretamente por um arquivo de configuração `config.json`.
2. **Suporte a Outros Idiomas:** Internacionalizar as mensagens e logs para diferentes idiomas.
3. **Interface Gráfica (GUI):** Implementar uma interface gráfica para facilitar a interação do usuário.
4. **Funcionalidade de Desfazer (Undo):** Implementar a possibilidade de desfazer a última ação de organização.

## Fale Comigo

Se você tiver alguma dúvida, sugestão ou problema relacionado a este projeto, sinta-se à vontade para entrar em contato:

- **Email:** augusto_lordano@hotmail.com
- **LinkedIn:** [augustolordano](https://www.linkedin.com/in/augustolordano/)
- **GitHub:** [auglordano](https://github.com/auglordano)

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Espero que este projeto seja útil para você! Sinta-se à vontade para fazer um fork, contribuir com melhorias e compartilhar com outras pessoas que possam se beneficiar deste organizador de área de trabalho.
