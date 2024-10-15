import pgzrun
import random
from pygame import Rect

class Hero:
    def __init__(self, x, y):
        self.actor = actor('hero_idle', (x, y))
        self.rect = Rect(self.actor.x, self.actor.y, self.actor.width, self.actor.height)
    
    def move(self, dx, dy):
        self.actor.x += dx
        self.actor.y += dy
        self.rect.update(self.actor.x, self.actor.y, self.actor.width, self.actor.height)

class Enemy:
    def __init__(self, x, y, patrol_area):
        self.actor = actor('enemy_idle', (x, y))
        self.rect = Rect(self.actor.x, self.actor.y, self.actor.width, self.actor.height)
        self.patrol_area = patrol_area
    
    def move(self):
        # Lógica de patrulha
        pass

teacher = 5
# Variáveis globais
WIDTH = 800
HEIGHT = 600


# Variável para controlar o estado do jogo
game_state = 'menu'  # Pode ser 'menu', 'playing', ou 'exit'

# Definindo áreas dos botões
start_button = Rect((300, 200), (200, 50))  # Botão de "Iniciar Jogo"
sound_button = Rect((300, 300), (200, 50))  # Botão de "Música On/Off"
exit_button = Rect((300, 400), (200, 50))   # Botão de "Sair"

# Controle de som
sound_on = True

# Função que desenha o menu principal
def draw_menu():
    screen.clear()
    screen.draw.text("Menu Principal", (320, 100), fontsize=50, color="white")
    
    # Desenhando os botões
    screen.draw.filled_rect(start_button, "green")
    screen.draw.text("Iniciar Jogo", (start_button.x + 30, start_button.y + 10), fontsize=40, color="white")
    
    screen.draw.filled_rect(sound_button, "blue")
    screen.draw.text("Música: " + ("Ligada" if sound_on else "Desligada"), (sound_button.x + 30, sound_button.y + 10), fontsize=40, color="white")
    
    screen.draw.filled_rect(exit_button, "red")
    screen.draw.text("Sair", (exit_button.x + 80, exit_button.y + 10), fontsize=40, color="white")

# Função para desenhar o jogo quando estiver jogando
def draw_game():
    screen.clear()
    screen.draw.text("Jogando...", (320, 240), fontsize=50, color="white")
    global game_running
    game_running = True
    music.play('bg_music')


# Função principal de desenho
def draw():
    if game_state == 'menu':
        draw_menu()
    elif game_state == 'playing':
        draw_game()

# Função para atualizar a lógica do jogo
def update():
    pass  # No menu, não precisamos de atualizações

# Função para detectar cliques do mouse
def on_mouse_down(pos):
    global game_state, sound_on

    if game_state == 'menu':
        # Verificar se o clique foi no botão de "Iniciar Jogo"
        if start_button.collidepoint(pos):
            game_state = 'playing'  # Muda o estado para "jogando"
        
        # Verificar se o clique foi no botão de "Música On/Off"
        elif sound_button.collidepoint(pos):
            sound_on = not sound_on  # Alterna entre ligar/desligar música
            if sound_on:
                music.play('bg_music')
            else:
                music.stop()
        
        # Verificar se o clique foi no botão de "Sair"
        elif exit_button.collidepoint(pos):
            game_state = 'exit'
            exit()

# Iniciar a música de fundo
music.play('bg_music')



game_running = False

hero_idle_frames = ['hero_idle_1', 'hero_idle_2', 'hero_idle_3', 'hero_idle_4']
# Sprites do herói e dos inimigos
hero = Actor("hero_idle_1", (100, 500))  # 'hero_idle' deve ser uma animação de idle
enemies = []

# Lista de frames (quadros) da animação idle


# Controle da animação
animation_frame = 0  # Quadro atual da animação
animation_speed = 0.1  # Velocidade da animação (quanto menor, mais rápida)
animation_timer = 0  # Temporizador para controlar a mudança de quadros

# Função para o movimento do herói
def update_hero():
    if keyboard.left:
        hero.x -= 5
        hero.image = 'hero_run_1'
    elif keyboard.right:
        hero.x += 5
        hero.image = 'hero_run_1'
    else:
        hero.image = 'hero_idle_1'

# Função de atualização de inimigos
def update_enemies():
    for enemy in enemies:
        enemy.move()

# Função principal de atualização do jogo
def update():
    if not game_running:
        return
    update_hero()
    update_enemies()

# Função principal de desenho do jogo
def draw():
    if not game_running:
        draw_menu()
    else:
        screen.clear()
        hero.draw()
        for enemy in enemies:
            enemy.draw()

# Função de clique do mouse no menu
def on_mouse_down(pos):
    if not game_running:
        if 350 < pos[1] < 400:  # Start Game
            start_game()
        elif 400 < pos[1] < 450:  # Toggle Sound
            toggle_sound()
        elif 450 < pos[1] < 500:  # Exit
            exit_game()

pgzrun.go()
