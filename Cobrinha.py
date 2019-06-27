import pygame
from random import randrange

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

def inicializacao():
    try:
        pygame.init()
        print("Modulo Pygame inicializado com sucesso") 
    except:
        print ("Falha ao inicializar o modulo")

def spawnCobra(cobraXY):
    for xy in cobraXY:
        pygame.draw.rect(fundo, verde, [xy[0], xy[1], tamanho, tamanho]) # Desenha um retangulo (a cobra) na tela

def spawnMaca(macaX, macaY):
    pygame.draw.rect(fundo, vermelho, [macaX,macaY,tamanho,tamanho]) # Desenha um retangulo (a maçã) na tela

def texto(msg, cor, tam, x, y):
    fonte = pygame.font.SysFont(None, tam)
    texto1 = fonte.render(msg, True, cor)
    fundo.blit(texto1, [x, y])

def velocidade(pontos):
    if(pontos<=10):
        relogio.tick(10.5) # fps da cobra
    elif(pontos>10 and pontos<=20):
        relogio.tick(15)
    elif(pontos>20 and pontos<=30):
        relogio.tick(20)
    elif(pontos >30 and pontos<=40):
        relogio.tick(25)
    elif(pontos>40 and pontos<=50):
        relogio.tick(30)
    elif(pontos>50 and pontos<=60):
        relogio.tick(35)
    else:
        relogio.tick(40)
    

inicializacao()



altura, largura = 480, 640
tamanho = 10




relogio = pygame.time.Clock() # Define o fps do jogo
fundo = pygame.display.set_mode((largura, altura)) # Cria uma tela com 640x480
pygame.display.set_caption("Cobrinha") # Da um nome a janela




def jogo():
    posX = randrange(0, (largura-tamanho), 10)
    posY = randrange(0, (altura-tamanho), 10)
    macaX = randrange(0, (largura-tamanho), 10)
    macaY = randrange(0, (altura-tamanho), 10)

    velocidadeX = 0
    velocidadeY = 0
    cobraXY = []
    cobraComp = 2
    pontos = 0

    sair = True
    fimDeJogo = False

    while sair:

        while fimDeJogo:
            for event in pygame.event.get(): # Pega todos os eventos que estão acontecendo
            
                if(event.type == pygame.QUIT): # Se um dos eventos for fechar ele fecha o jogo
                    sair = False
                    fimDeJogo = False
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_c):
                        posX = randrange(0, (largura-tamanho), 10)
                        posY = randrange(0, (altura-tamanho), 10)
                        macaX = randrange(0, (largura-tamanho), 10)
                        macaY = randrange(0, (altura-tamanho), 10)

                        velocidadeX = 0
                        velocidadeY = 0
                        cobraXY = []
                        cobraComp = 2
                        pontos = 0
                        
                        sair = True
                        fimDeJogo = False
                    if(event.key == pygame.K_s):
                        sair = False
                        fimDeJogo = False
                        
            fundo.fill(azul)
            texto("Fim de Jogo!", verde, 50, largura/3.3, altura/3.3)
            texto("Pontuação: "+ str(pontos), verde, 30, largura/2.7, altura/2)
            texto("Aperte c para jogar novamente ou s para sair!", verde, 20, largura/4, altura/1.5)
            pygame.display.update()

        for event in pygame.event.get(): # Pega todos os eventos que estão acontecendo
            
            if(event.type == pygame.QUIT): # Se um dos eventos for fechar ele fecha o jogo
                sair = False
                
            if(event.type == pygame.KEYDOWN): # Verifica se algum botao foi apertado
                if(event.key == pygame.K_LEFT and velocidadeX != tamanho): # Verifica se o botao pressionado foi a seta da esquerda
                    velocidadeY = 0
                    velocidadeX = -tamanho
                if(event.key == pygame.K_RIGHT and velocidadeX != -tamanho): # Verifica se o botao pressionado foi a seta da direita
                    velocidadeY = 0
                    velocidadeX = tamanho
                if(event.key == pygame.K_UP and velocidadeY != tamanho): # Verifica se o botao pressionado for a seta para cima
                    velocidadeX = 0
                    velocidadeY = -tamanho
                if(event.key == pygame.K_DOWN and velocidadeY != -tamanho): # Verifica se o botao pressionado for a seta para baixo
                    velocidadeX = 0
                    velocidadeY = tamanho

            
        if(sair):
            fundo.fill(preto) # Define uma cor de fundo para a tela
            
            if(posX == macaX and posY == macaY): # verificação se bateu na maçã, criando nova posição da maçã e aumentando tamanho da cobra 
                macaX = randrange(0, (largura-tamanho), 10) 
                macaY = randrange(0, (altura-tamanho), 10)
                cobraComp += 1
                pontos +=1


            if(posX > largura): # verifica colisao com as bordas
                fimDeJogo = True
            elif(posX < 0):
                fimDeJogo = True
            elif(posY > altura):
                fimDeJogo = True
            elif(posY < 0):
                fimDeJogo = True
                
            posX += velocidadeX
            posY += velocidadeY

            cobraInicio = [] # Nova posição da cobra
            cobraInicio.append(posX)
            cobraInicio.append(posY)
            cobraXY.append(cobraInicio) # cobra inteira 

            if(len(cobraXY) > cobraComp): # condição para a cobra não crescer infinitamente
                del cobraXY[0]
                
            if( any(bloco == cobraInicio for bloco in cobraXY[:-1]) and len(cobraXY) != 2):
                fimDeJogo = True
            
            texto("Pontuação: "+ str(pontos), branco, 20, 10, 10)
            
            spawnCobra(cobraXY)
            spawnMaca(macaX, macaY)
            
            pygame.display.update() # atualiza constantemente a janela

            velocidade(pontos)
jogo()
pygame.quit() # fecha a janela do jogo
