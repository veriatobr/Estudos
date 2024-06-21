import pygame
import sys

pygame.init()

lagura_tela = 800
altura_tela = 600
tamanho_tela = (lagura_tela, altura_tela)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("jogo da verdade ou mentira!")

branco = (255, 250, 240)
preto = (0,0,0)
vermelho = (227, 38, 54)
verde = (0, 100, 0)

fonte = pygame.font.Font(None, 60)
fonte_pqn = pygame.font.Font(None, 40)
pergunta = "O lula é ladrao? sim ou não!"
resposta_certa = False

#seta_direita = pygame.image.load('dir.ico')
#seta_esquerda = pygame.image.load('esq.ico')

#seta_direita = pygame.transform.scale(seta_direita(50, 50))
#seta_esquerda = pygame.transform.scale(seta_esquerda(50, 50))
rodando = True
resposta = None

while rodando:
   for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
       rodando = False
    elif evento.type == pygame.KEYDOWN:
       if evento.key == pygame.K_RIGHT: #se for nao so lembrar de colocar no loop infinito
          resposta = False
       elif evento.key == pygame.K_LEFT:
          resposta = True
        
    tela.fill(branco)
    
    texto_renderizado = fonte.render(pergunta, True, preto)
    texto_rect = texto_renderizado.get_rect(center=(lagura_tela / 2, altura_tela / 3))
    tela.blit(texto_renderizado, texto_rect)
    #tela.blit(seta_direita, lagura_tela / 2 - 50, altura_tela / 2 - 50)
    #tela.blit(seta_esquerda, lagura_tela / 2 - 50, altura_tela / 2 - 50)
    

    if resposta is not None:
       if resposta == resposta_certa:
          resultado_texto = "Ele realmente é um ladrão!"
          cor_resultado = verde
       else:
            resultado_texto = "Tem certeza que ele não é um ladrao?"
            cor_resultado = vermelho
            resultado_renderizado = fonte_pqn.render(resultado_texto, True, cor_resultado)

       resultado_renderizado = fonte.render(resultado_texto, True, cor_resultado)
       resultado_rect = resultado_renderizado.get_rect(center=(lagura_tela /4, 4* altura_tela /6))
       tela.blit(resultado_renderizado, resultado_rect)
       

    pygame.display.flip()
pygame.quit()
sys.exit()