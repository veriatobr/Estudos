'''Página inicial do Pygame 
Começo rápido 
Bem-vindo ao pygame! Depois de instalar o pygame ( ou para a maioria das pessoas), a próxima pergunta é como executar um loop de jogo. Pygame, ao contrário de algumas outras bibliotecas, oferece controle total da execução do programa. Essa liberdade significa que é fácil errar nas etapas iniciais.pip install pygamepip3 install pygame

Aqui está um bom exemplo de configuração básica (abre a janela, atualiza a tela e lida com eventos)--

# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

    Aqui está um exemplo um pouco mais detalhado, que mostra como mover algo (um círculo, neste caso) na tela -

# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

Para uma referência mais aprofundada, confira a seção Tutoriais abaixo, confira um tutorial em vídeo ( sou fã deste ) ou consulte a documentação da API por módulo.

Documentos¶
Leia-me
Informações básicas sobre o pygame: o que é, quem está envolvido e onde encontrá-lo.

Instalar
Etapas necessárias para compilar o pygame em diversas plataformas. Também ajude a encontrar e instalar binários pré-construídos para o seu sistema.

Argumentos da função do caminho do arquivo
Como o pygame lida com os caminhos do sistema de arquivos.

Logotipos de Pygame
Os logotipos do Pygame em diferentes resoluções.

Licença LGPL
Esta é a licença sob a qual o pygame é distribuído. Ele prevê que o pygame seja distribuído com software comercial e de código aberto. Geralmente, se o pygame não for alterado, ele poderá ser usado com qualquer tipo de programa.

Tutoriais¶
Introdução ao Pygame
Uma introdução aos fundamentos do pygame. Isto foi escrito para usuários de Python e apareceu no volume dois da revista Py.

Importar e inicializar
As etapas iniciais para importar e inicializar o pygame. O pacote pygame é composto por vários módulos. Alguns módulos não estão incluídos em todas as plataformas.

Como movo uma imagem?
Um tutorial básico que cobre os conceitos por trás da animação 2D por computador. Informações sobre como desenhar e limpar objetos para que pareçam animados.

Tutorial do Chimpanzé, Linha por Linha
Os exemplos do pygame incluem um programa simples com um punho interativo e um chimpanzé. Isso foi inspirado no irritante banner em flash do início dos anos 2000. Este tutorial examina cada linha de código usada no exemplo.

Introdução ao Módulo Sprite
Pygame inclui um módulo sprite de nível superior para ajudar a organizar os jogos. O módulo sprite inclui diversas classes que ajudam a gerenciar detalhes encontrados em quase todos os tipos de jogos. As classes Sprite são um pouco mais avançadas que os módulos regulares do pygame e precisam de mais compreensão para serem usadas corretamente.

Introdução ao Surfray
Pygame usou o módulo NumPy python para permitir efeitos eficientes por pixel nas imagens. Usar matrizes de superfície é um recurso avançado que permite efeitos e filtros personalizados. Isso também examina alguns dos efeitos simples do exemplo pygame, arraydemo.py.

Introdução ao módulo de câmera
O Pygame, a partir do 1.9, possui um módulo de câmera que permite capturar imagens, assistir transmissões ao vivo e fazer alguma visão computacional básica. Este tutorial cobre esses casos de uso.

Guia para iniciantes
Uma lista de treze dicas úteis para as pessoas se sentirem confortáveis ​​​​com o pygame.

Tutorial de criação de jogos
Um grande tutorial que cobre os tópicos maiores necessários para criar um jogo inteiro.

Modos de exibição
Obtendo uma superfície de exibição para a tela.

Referência 
Índice
Uma lista de todas as funções, classes e métodos do pacote pygame.

pygame.BufferProxy
Uma visualização de protocolo de matriz de pixels de superfície

pygame.Color
Representação de cores.

pygame.cursores
Carregando e compilando imagens de cursor.

pygame.display
Configure a superfície de exibição.

pygame.draw
Desenhar formas simples como linhas e elipses em superfícies.

pygame.event
Gerencie os eventos recebidos de vários dispositivos de entrada e da plataforma de janelas.

pygame.exemplos
Vários programas demonstrando o uso de módulos pygame individuais.

pygame.font
Carregando e renderizando fontes TrueType.

pygame.freetype
Módulo pygame aprimorado para carregar e renderizar fontes.

pygame.gfxdraw
Funções de desenho anti-aliasing.

pygame.image
Carregar, salvar e transferir superfícies.

pygame.joystick
Gerencie os dispositivos de joystick.

pygame.key
Gerencie o dispositivo de teclado.

pygame.locals
Constantes Pygame.

pygame.mixer
Carregar e reproduzir sons

pygame.mouse
Gerencie o dispositivo de mouse e a exibição.

pygame.mixer.music
Reproduza faixas de música em streaming.

pygame
Funções de nível superior para gerenciar pygame.

pygame.PixelArray
Manipule dados de pixel da imagem.

pygame.Rect
Recipiente flexível para um retângulo.

pygame.scrap
Acesso nativo à área de transferência.

pygame.sndarray
Manipule dados de amostra de som.

pygame.sprite
Objetos de nível superior para representar imagens do jogo.

pygame.Surface
Objetos para imagens e tela.

pygame.surfarray
Manipule dados de pixel da imagem.

pygame.testes
Teste o pygame.

pygame.time
Gerencie o tempo e a taxa de quadros.

pygame.transform
Redimensione e mova imagens.

API C do Pygame
A API C compartilhada entre os módulos de extensão do pygame.

Página de pesquisa
Pesquise documentos pygame por palavra-chave.



pygame._sdl2.controller	módulo pygame para trabalhar com controladores
pygame._sdl2.touch	módulo pygame para trabalhar com entrada por toque
pygame._sdl2.video	Módulo pygame experimental para portar novos sistemas de vídeo SDL
pygame.camera	módulo pygame para uso da câmera
pygame.cdrom	módulo pygame para controle de cdrom de áudio
pygame.cursors	módulo pygame para recursos de cursor
pygame.display	módulo pygame para controlar a janela de exibição e a tela
pygame.draw	módulo pygame para desenhar formas
pygame.event	módulo pygame para interagir com eventos e filas
pygame.examples	módulo de programas de exemplo
pygame.fastevent	Módulo pygame para interagir com eventos e filas de vários threads.
pygame.font	módulo pygame para carregar e renderizar fontes
pygame.freetype	Módulo pygame aprimorado para carregar e renderizar fontes de computador
pygame.gfxdraw	módulo pygame para desenhar formas
pygame.image	módulo pygame para carregar e salvar imagens
pygame.joystick	Módulo Pygame para interagir com joysticks, gamepads e trackballs.
pygame.key	módulo pygame para trabalhar com o teclado
pygame.locals	constantes pygame
pygame.mask	Módulo pygame para máscaras de imagem.
pygame.math	módulo pygame para classes de vetores
pygame.midi	Módulo pygame para interagir com entrada e saída midi.
pygame.mixer	módulo pygame para carregar e reproduzir sons
pygame.mixer.music	módulo pygame para controlar áudio transmitido
pygame.mouse	módulo pygame para trabalhar com o mouse
pygame.pixelcopy	módulo pygame para cópia geral de array de pixels
pygame.scrap	Módulo pygame para suporte à área de transferência.
pygame.sndarray	módulo pygame para acessar dados de amostra de som
pygame.sprite	módulo pygame com classes básicas de objetos de jogo
pygame.surfarray	Módulo pygame para acessar dados de pixels de superfície usando interfaces de array
pygame.tests	Pacote de conjunto de testes de unidade Pygame
pygame.time	módulo pygame para monitorar o tempo
pygame.transform	módulo pygame para transformar superfícies
pygame.version	pequeno módulo contendo informações de versão
pygame	o pacote pygame de nível superior
'''
