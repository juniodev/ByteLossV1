## Configurando um ambiente virtual usando conda

1. Instale o conda seguindo as instruções do site oficial: https://docs.conda.io/en/latest/miniconda.html

2. Abra um terminal ou prompt de comando e execute o seguinte comando para criar um ambiente virtual:

   conda create --name my_env python=3.7.16

   Este comando criará um ambiente virtual chamado `my_env` com o Python 3.7.16 instalado.

3. Ative o ambiente virtual usando o seguinte comando:

   conda activate my_env

   Isso irá ativar o ambiente virtual, permitindo que você instale as bibliotecas necessárias para o chatbot.

4. Verifique se a versão correta do Python está instalada no ambiente virtual executando o seguinte comando:

   python --version

   Certifique-se de que a versão exibida seja `Python 3.7.16` ou superior.

5. Para desativar o ambiente virtual, use o comando:

   conda deactivate

   Isso retornará o terminal ao ambiente padrão.

## Configurando o token do bot do Telegram

1. Abra o arquivo `main.py` em um editor de texto.

2. Procure a linha que contém o token do bot do Telegram:

   chatbot = telebot.TeleBot('YOUR_TELEGRAM_API_TOKEN')

   Substitua `YOUR_TELEGRAM_API_TOKEN` pelo token do seu bot do Telegram. Se você ainda não criou um bot do Telegram, siga as instruções aqui: https://core.telegram.org/bots#3-how-do-i-create-a-bot

3. Salve o arquivo `main.py` após fazer as alterações.

## Executando o chatbot

1. No terminal, certifique-se de que o ambiente virtual `my_env` está ativado.

2. Navegue até o diretório onde o arquivo `main.py` está localizado.

3. Execute o seguinte comando para iniciar o chatbot:

   python main.py

   Isso iniciará o chatbot e você poderá interagir com ele por meio do Telegram.

Para mais informações sobre como usar a biblioteca ChatterBot, consulte a documentação oficial: https://chatterbot.readthedocs.io/en/stable/
