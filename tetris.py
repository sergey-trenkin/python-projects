import pygame
import random

pygame.font.init()
pygame.mixer.init()

# Pygame standart
window = pygame.display.set_mode((650, 850))
back = (255, 255, 255) 
window.fill(back) 
clock = pygame.time.Clock() 
game = True
font1 = pygame.font.SysFont('zapfino', 70) 
font2 = pygame.font.SysFont('Savoye LET', 40) 
FPS = 60
# End Pygame standart

class back_rect():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (215, 215, 215)
        self.rect = pygame.Rect(self.x + 1, self.y + 1, 33, 33)
        self.end_rect = pygame.Rect(self.x, self.y, 35, 35)
    def draw(self):
        pygame.draw.rect(window, (194, 194, 194), self.end_rect)
        pygame.draw.rect(window, self.color, self.rect)

class block():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(self.x + 1, self.y + 1, 33, 33)
        self.end_rect = pygame.Rect(self.x, self.y, 35, 35)
    def move_down(self):
        global list_falling_block, list_stay_block, end, figure_, game, fi, last, list_last_block, fi_1, fi_2, list_replacement_block, replacement, y_figure, touch
        for i in range(len(list_falling_block)):
            if list_falling_block[i].end_rect.bottom == 800 or list_falling_block[i].end_rect.bottom > 100 and list_stay_block[(list_falling_block[i].rect.top - 100) // 35 + 1][(list_falling_block[i].end_rect.left - 150) // 35] != 0:
                end = True
                for i in list_falling_block:
                    if i.end_rect.top == 100:
                        game = False
                        break
                if not(game):
                    break
                for i in list_falling_block:
                    list_stay_block[(i.end_rect.top - 100) // 35][(i.end_rect.left - 150) // 35] = i

                touch = True
                break
        else:
            for i in list_falling_block:
                i.y += 35
                i.end_rect.move_ip(0, 35)
                i.rect.move_ip(0, 35)
            y_figure += 35
    def down_block(self):
        global list_down_block, list_falling_block
        self.down = True
        list_down_block.clear()
        for i in list_falling_block:
            list_down_block.append(block(i.end_rect.left, i.end_rect.top, (160, 160, 160)))
        while self.down:
            for i in range(len(list_down_block)):
                if list_down_block[i].end_rect.bottom == 800 or list_down_block[i].end_rect.bottom > 100 and list_stay_block[(list_down_block[i].rect.top - 100) // 35 + 1][(list_down_block[i].end_rect.left - 150) // 35] != 0:
                    self.down = False
                    break
            else:
                for n in list_down_block:
                    n.rect.move_ip(0, 35)
                    n.end_rect.move_ip(0, 35)
    def move_right(self):
        self.x += 35
        self.end_rect.move_ip(35, 0)
        self.rect.move_ip(35, 0)
    def move_left(self):
        self.x -= 35
        self.end_rect.move_ip(-35, 0)
        self.rect.move_ip(-35, 0)
    def check_right(self):
        global list_falling_block, list_stay_block, move, x_figure
        for i in range(len(list_falling_block)):
            if list_falling_block[i].end_rect.right == 500 or list_falling_block[i].end_rect.bottom > 100 and list_stay_block[(list_falling_block[i].end_rect.top - 100) // 35][(list_falling_block[i].end_rect.left - 150) // 35 + 1] != 0:
                move = False
                break
        else:
            move = True
            x_figure += 35
    def check_left(self):
        global list_falling_block, list_stay_block, move, x_figure
        for i in range(len(list_falling_block)):
            if list_falling_block[i].end_rect.left == 150 or list_falling_block[i].end_rect.bottom > 100 and list_stay_block[(list_falling_block[i].end_rect.top - 100) // 35][(list_falling_block[i].end_rect.left - 150)// 35 - 1] != 0:
                move = False
                break
        else:
            move = True
            x_figure -= 35
    def draw(self):
        pygame.draw.rect(window, (0, 0, 0), self.end_rect)
        pygame.draw.rect(window, self.color, self.rect)

class figure():
    def __init__(self, size, binar, color):
        global list_falling_block, x_figure, y_figure, turn_, list_down_block
        turn_ = 1
        self.size = size
        self.binar = binar
        self.color = color
        self.x = 290
        self.y = 100
        x_figure = self.x
        y_figure = self.y
        self.block_number = 0
        for i in range(len(self.binar)):
            if self.binar[int(i)] == 1:
                list_falling_block.append(block(self.x, self.y, self.color))
                list_down_block.append(block(self.x, self.y, (160, 160, 160)))
            if (i + 1) % self.size[0] == 0:
                self.x = 290
                self.y += 35
            else:
                self.x += 35
            self.block_number += 1

class last_figure():
    def __init__(self, size, binar, color):
        global list_last_block
        self.size = size
        self.binar = binar
        self.color = color
        self.x = 520
        self.y = 200 
        for i in range(len(self.binar)):
            if self.binar[int(i)] == 1:
                list_last_block.append(block(self.x, self.y, self.color))
            if (i + 1) % self.size[0] == 0:
                self.x = 520
                self.y += 35
            else:
                self.x += 35
        list_down_block[0].down_block()

class replecement_figure():
    def __init__(self, size, binar, color):
        global list_replacement_block
        self.binar = binar
        self.color = color
        self.x = 20
        self.y = 200 
        for i in range(len(self.binar)):
            if self.binar[int(i)] == 1:
                list_replacement_block.append(block(self.x, self.y, self.color))
            self.size = size
            if (i + 1) % self.size[0] == 0:
                self.x = 20
                self.y += 35
            else:
                self.x += 35

def turn():
    global turn_figures, turn_, x_figure, y_figure, fi, list_falling_block, list_down_block
    size = turn_figures[fi][0]
    turn_pos = turn_figures[fi][turn_].copy()
    x_block = 0
    y_block = 0
    zero = 0
    for i in range(size[0] * size[1]):
        if turn_pos[i] == 1:
            if x_figure + x_block < 150 or x_figure + x_block + 35 > 500 or list_falling_block[i - zero].end_rect.bottom < 100 or list_stay_block[(y_figure + y_block - 100) // 35][(x_figure + x_block - 150) // 35] != 0:
                break
        else:
            zero += 1
        if (i + 1) % size[0] == 0:
            x_block = 0
            y_block += 35
        else:
            x_block += 35
    else:
        for n in range(len(list_falling_block)):
            block_index = turn_pos.index(1)
            turn_pos.pop(block_index)
            list_down_block[n].rect.move_ip(x_figure + ((block_index + n) % size[0]) * 35 - list_falling_block[n].rect.left + 1, y_figure + ((block_index + n) // size[0]) * 35 - list_falling_block[n].rect.top + 1)
            list_down_block[n].end_rect.move_ip(x_figure + ((block_index + n) % size[0]) * 35 - list_falling_block[n].end_rect.left, y_figure + ((block_index + n) // size[0]) * 35 - list_falling_block[n].end_rect.top)
            list_falling_block[n].rect.move_ip(x_figure + ((block_index + n) % size[0]) * 35 - list_falling_block[n].rect.left + 1, y_figure + ((block_index + n) // size[0]) * 35 - list_falling_block[n].rect.top + 1)
            list_falling_block[n].end_rect.move_ip(x_figure + ((block_index + n) % size[0]) * 35 - list_falling_block[n].end_rect.left, y_figure + ((block_index + n) // size[0]) * 35 - list_falling_block[n].end_rect.top)
            if (n + 1) % size[0] == 0:
                x_block = 0
                y_block += 35
            else:
                x_block += 35
        turn_ = 1 + turn_ % 4
        list_down_block[0].down_block()

def draw_all():
    global text_next, text_null_lines, text_replacement, text_time
    window.fill(back)
    for i in list_back:
        for n in i:
            n.draw()    
    for i in range(20):
        for n in range(10):
            if list_stay_block[i][n] != 0:
                list_stay_block[i][n].draw()
    for i in list_down_block:
        i.draw()
    for i in list_falling_block:
        i.draw()
    for i in list_last_block:
        i.draw()
    for i in list_replacement_block:
        i.draw()
    text_null_lines = font1.render(str(lines), True, list_figures[fi * 3 + 2])
    text_next = font2.render('След.', True, list_figures[fi * 3 + 2])
    text_replacement = font2.render('Замена (alt)', True, list_figures[fi * 3 + 2])
    text_time = font2.render(str('Время: ' + str((pygame.time.get_ticks() - delay) // 3600000) + ':' + str((pygame.time.get_ticks() - delay) % 3600000 // 60000) + ':' + str((pygame.time.get_ticks() - delay) % 60000 // 1000) + '.' + str((pygame.time.get_ticks() - delay) % 1000 // 10)), True, list_figures[fi * 3 + 2])
    window.blit(text_null_lines, (225, -50))
    window.blit(text_next, (520, 150))
    window.blit(text_replacement, (5, 150))
    window.blit(text_time, (30, 30))
    pygame.display.update()

turn_ = 2
coefficient = 1
touch = False
end = False
delay = 0
list_figures = [[2, 2], [1, 1, 1, 1], (240, 239, 56), [3, 3], [0, 1, 0, 0, 1, 0, 1, 1, 0], (0, 0, 235), [4, 4], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0], (136, 240, 240), [3, 3], [0, 1, 0, 1, 1, 1, 0, 0, 0], (136, 0, 236), [3, 3], [0, 1, 0, 0, 1, 0, 0, 1, 1], (220, 158, 35), [3, 3], [0, 0, 0, 1, 1, 0, 0, 1, 1], (206, 0, 6), [3, 3], [0, 0, 0, 0, 1, 1, 1, 1, 0], (135, 240, 56)]
turn_figures = [[[2, 2], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], 
                [[3, 3], [0, 1, 0, 0, 1, 0, 1, 1, 0], [1, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 1, 1, 0, 0, 1]],
                [[4, 4], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]],
                [[3, 3], [0, 1, 0, 1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 1, 0], [0, 0, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 1, 0, 0, 1, 0]],
                [[3, 3], [0, 1, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 0], [0, 0, 1, 1, 1, 1, 0, 0, 0]],
                [[3, 3], [0, 0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 1, 0, 1, 0, 0], [1, 1, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 1, 1, 0, 1, 0]],
                [[3, 3], [0, 0, 0, 0, 1, 1, 1, 1, 0], [1, 0, 0, 1, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1]]]
list_stay_block = []
list_back = []
list_down_block = []
x_figure = 0
y_figure = 0
for i in range(20):
    list_back.append([])
    for n in range(10):
        list_back[i].append(back_rect(150 + n * 35, 100 + i * 35))
for i in range(20):
    list_stay_block.append([])
    for n in range(10):
        list_stay_block[i].append(0)
list_falling_block = []
list_last_block = []
list_replacement_block = []
fi = random.randint(0, 6)
figure_ = figure(list_figures[fi * 3], list_figures[fi * 3 + 1], list_figures[fi * 3 + 2])
fi_1 = random.randint(0, 6)
last = last_figure(list_figures[fi_1 * 3], list_figures[fi_1 * 3  + 1], list_figures[fi_1 * 3 + 2])
fi_2 = random.randint(0, 6)
if fi_2 == fi:
    fi_2 = (fi_2 + 1) % 7
replacement = replecement_figure(list_figures[fi_2 * 3], list_figures[fi_2 * 3  + 1], list_figures[fi_2 * 3 + 2])
move = True
lines = 0
text_time = font2.render(str('Время: ' + str((pygame.time.get_ticks() - delay) // 3600000) + ':' + str((pygame.time.get_ticks() - delay) % 3600000 // 60000) + ':' + str((pygame.time.get_ticks() - delay) % 60000 // 1000) + '.' + str((pygame.time.get_ticks() - delay) % 1000 // 10)), True, list_figures[fi * 3 + 2])
text_null_lines = font1.render(str(lines), True, list_figures[fi * 3 + 2])
text_next = font2.render('След.', True, list_figures[fi * 3 + 2])
text_replacement = font2.render('Замена (alt)', True, list_figures[fi * 3 + 2])

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                game = False
            if e.key == pygame.K_RALT or e.key == pygame.K_LALT:
                if len(list_replacement_block) > 0:
                    list_replacement_block.clear()
                    list_falling_block.clear()
                    list_down_block.clear()
                    figure_ = figure(replacement.size, replacement.binar, replacement.color)
                    fi = fi_2
                    replacement = ''
                    list_down_block[0].down_block()
            if e.key == pygame.K_RIGHT:
                list_falling_block[0].check_right()
                if move:
                    for i in range(len(list_falling_block)):
                        list_falling_block[i].move_right()
                    for i in list_down_block:
                        i.move_right()
                    list_down_block[0].down_block()
            if e.key == pygame.K_LEFT:
                list_falling_block[0].check_left()
                if move:
                    for i in range(len(list_falling_block)):
                        list_falling_block[i].move_left()
                    for i in list_down_block:
                        i.move_left()
                    list_down_block[0].down_block()
            if e.key == pygame.K_DOWN:
                list_falling_block[0].move_down()
            if e.key == pygame.K_UP:
                coefficient *= -1
            if e.key == pygame.K_SPACE:
                while not(touch):
                    list_falling_block[0].move_down()
                    draw_all()
                    pygame.time.delay(25)
            if e.key == pygame.K_p or e.key == pygame.K_g:
                pause = True
                start_pause = pygame.time.get_ticks()
                while pause:
                    for c in pygame.event.get():
                        if c.type == pygame.QUIT:
                            pause = False
                            game = False
                            break
                        if c.type == pygame.KEYDOWN:
                            if c.key == pygame.K_ESCAPE:
                                pause = False
                                game = False
                                break
                            if e.key == pygame.K_p or e.key == pygame.K_g:
                                pause = False
                                break
                delay += pygame.time.get_ticks() - start_pause
        if e.type == pygame.MOUSEBUTTONDOWN:
            turn()
    if pygame.time.get_ticks() % 500 < 20:
        list_falling_block[0].move_down()
        pygame.time.delay(20)
    block_in_line = 0
    last_lines = lines
    list_null_lines = []
    for i in list_stay_block:
        for n in i:
            if n != 0:
                block_in_line += 1
        if block_in_line == 10:
            ind = list_stay_block.index(i)
            list_null_lines.append(ind)
            lines += 1
        block_in_line = 0
    if last_lines != lines:
        if lines - last_lines == 2:
            lines += 1
        elif lines - last_lines == 3:
            lines += 4
        elif lines - last_lines == 4:
            lines += 11
        draw_all()
        start = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start < 1000:
            if (pygame.time.get_ticks() - start) % 120 < 20:
                if list_stay_block[list_null_lines[0]][0].color != (215, 215, 215):
                    for i in list_null_lines:
                        for n in list_stay_block[i]:
                            n.old_color = n.color
                            n.color = (215, 215, 215)
                else:
                    for i in list_null_lines:
                        for n in list_stay_block[i]:
                            n.color = n.old_color
                pygame.time.delay(20)
            draw_all()
        for i in range(len(list_null_lines)):
            list_stay_block.pop(list_null_lines[i])
            for b in range(len(list_stay_block)):
                if b < list_null_lines[i]:
                    for v in list_stay_block[b]:
                        if v != 0:
                            v.y += 35
                            v.end_rect.move_ip(0, 35)
                            v.rect.move_ip(0, 35)
            list_stay_block.insert(0, [])
            for m in range(10):
                list_stay_block[0].append(0)
            for n in list_null_lines:
                n -= 1
    if touch:
        list_null_lines.clear()
        last_lines = lines
        list_falling_block.clear()
        list_down_block.clear()
        figure_ = figure(last.size, last.binar, last.color)
        list_last_block.clear()
        fi = fi_1
        fi_1 = random.randint(0, 6)
        last = last_figure(list_figures[fi_1 * 3], list_figures[fi_1 * 3  + 1], list_figures[fi_1 * 3 + 2])
        list_replacement_block.clear()
        fi_2 = random.randint(0, 6)
        if fi_2 == fi:
            fi_2 = (fi_2 + 1) % 7
        replacement = replecement_figure(list_figures[fi_2 * 3], list_figures[fi_2 * 3  + 1], list_figures[fi_2 * 3 + 2])
        list_down_block[0].down_block()
        touch = False
    draw_all()
    clock.tick(FPS)
