# BombBot
pt-BR: Um bot de automação para mineração do token BCOIN dentro do jogo Bombcrypto sem precisar estar 24 horas monitorando seus heróis. Este script coloca todos os heróis que esteja com a estamina verde para trabalhar, atualiza a posição dos heróis, reconecta com o jogo e algumas outras coisas extras de forma totalmente automática.

en-US: An automation script for mining the BCOIN token within the Bombcrypto game without having to be 24 hours monitoring your heroes. This script puts all the heroes with the green stamina to work, updates the position of the heroes, reconnects with the game and some other extra things fully automatically.

# Pré Requisitos / Pre Requirements
#### pt-BR
##### Instalar o Python
Eu desenvolvi o bot na versão 3.7.0 do Python portanto recomendo utilizar essa mesma versão também por conta de compatibilidade (mas caso tenha outra versão já instalada, teste o robô e veja se está funcionando normalmente na sua versão).
Para instalar você precisa entrar no site oficial dele e baixar a versão de acordo com seu Sistema Operacional (32bits ou 64bits):<br>
Link 32bits: https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe<br>
Link 64bits: https://www.python.org/ftp/python/3.7.0/python-3.7.0-amd64.exe<br>
Execute como administrador o executável baixado e instale o Python. OBS: ao iniciar a instalação, quando aparecer a caixinha com opção "Add Python 3.7 to PATH" você precisa marcar ela!

#### en-US
##### Install Python
I developed the bot in Python version 3.7.0 so I recommend using that same version also for compatibility (but if you have another version already installed, test the robot and see if it works normally in your version).
To install you need to go to its official website and download the version according to your Operating System (32bits or 64bits):<br>
32bit link: https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe<br>
64bit link: https://www.python.org/ftp/python/3.7.0/python-3.7.0-amd64.exe<br>
Run the downloaded executable as administrator and install Python. NOTE: when starting the installation, when the box appears with the option "Add Python 3.7 to PATH" you need to check it!

# Principais Funções / Main Functions
#### pt-BR
- Colocar heróis (com estamina verde) para trabalhar;
- Atualizar a posição dos heróis para que não seja desconectado ou para desbugar heróis que saiam do mapa ou travem;
- Conectar ou reconectar automaticamente com sua Wallet. Atenção: necessário que ela esteja desbloqueada;
- Passar para o próximo mapa (função desativada enquanto não requer mais a necessidade dela pois o Bombcrypto implementou isto no game).

#### en-US
- Put heroes (with green stamina) to work;
- Update the position of heroes so that they are not disconnected or to debug heroes who leave the map or brake;
- Connect or reconnect automatically with your Wallet. Attention: it is required to be unlocked;
- Move on to the next map (function disabled while no longer requiring it because Bombcrypto implemented this in the game).

# Como Usar / How to Use
#### pt-BR
1. Vá até o link oficial do jogo https://app.bombcrypto.io/ e logue com sua MetaMask ou pelo menos desbloqueie ela e o bot já estará apto para uso. Importante: deixe essa tela maximizada enquanto rodar bot;
2. Abra a pasta do BombBot;
3. Clique direito sobre o arquivo "install" e execute como administrador (pode excluir este arquivo depois de finalizar a instalação das dependências);
4. Execute o arquivo "start" e troque para tela do seu navegador que está aberto o Bombcrypto;
5. Pronto, o bot irá começar a minerar automaticamente para você!

#### en-US
1. Go to the official game link https://app.bombcrypto.io/ and login with your MetaMask or at least unlock it and the bot will be ready to use. Important: leave this screen maximized while running bot;
2. Open the BombBot folder;
3. Right click on the "install" file and run as administrator (you can delete this file after finishing the installation of the dependencies);
4. Run the "start" file and switch to your browser screen that Bombcrypto is open;
5. Okay, the bot will automatically start mining for you!

# Como Configurar / How to Set Up
#### pt-BR
Você pode configurar o intervalo entre as interações do bot. Por exemplo: verificar a cada 1 minuto se está logado e a cada 5 minutos atualizar a posição dos heróis no mapa. Para fazer isto abra com qualquer editor de texto o arquivo "config".
#### Por padrão as configurações são:
- Enviar heróis para o trabalho a cada 10 minutos;
- Atualizar posição dos heróis a cada 5 minutos;
- Verificar se está conectado a cada 1 minuto.
##### Arquivo config.yaml
<img src="https://i.imgur.com/IfzP2fA.png">
Agora altere os números respectivos do seu interesse para o intervalo desejado em minutos.

#### en-US
You can configure the interval between bot interactions. For example: check every 1 minute if you are logged in and every 5 minutes update the position of heroes on the map. To do this open the "config" file with any text editor.
#### By default the settings are:
- Send heroes to work every 10 minutes;
- Update hero position every 5 minutes;
- Check that it is connected every 1 minute.
##### config.yaml file
<img src="https://i.imgur.com/IfzP2fA.png">
Now change the respective numbers of interest to the desired range in minutes.

# Atenção / Attention
#### pt-BR
- Não troque o nome de nenhum dos arquivos contidos na pasta do BombBot em "templates" e altere apenas as imagens se necessário;
- Deixe a janela do navegador que está rodando o Bombcrypto sempre maximizada e apenas ela aberta no seu monitor.

#### en-US
- Do not change the name of any of the files contained in the BombBot folder in "templates" and change only the images if necessary;
- Leave the browser window that is running Bombcrypto always maximized and only it open on your monitor.

# Como Resolver Problemas / How To Solve Problems
#### pt-BR
Caso o seu bot não esteja fazendo nada ou esteja deixando de fazer algumas coisas é porque provavelmente não está reconhecendo as imagens. Abra a pasta "templates" dentro da pasta do BombBot e troque as imagens que estejam lá dentro tirando PrintScreen da sua tela e recortando o respectivo ícone, texto ou botão. OBS: ao salvar, salve sempre com o mesmo nome que também estava na pasta "templates" e em formato ".png".

#### en-US
If your bot isn't doing anything or failing to do some things, it's probably not recognizing the images. Open the "templates" folder inside the BombBot folder and swap the images inside by taking PrintScreen from your screen and cropping its icon, text, or button. NOTE: When saving, always save with the same name that was also in the "templates" folder and in ".png" format.
