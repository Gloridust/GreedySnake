import pygame
import sys
import random

# 初始化
pygame.init()

# 设置屏幕大小和颜色
width, height = 700, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇游戏")
bg_color = (0, 0, 0)
snake_color = (0, 255, 0)
food_color = (255, 0, 0)
text_color = (255, 255, 255)

# 蛇的初始位置和速度
snake = [(100, 100), (90, 100), (80, 100)]
snake_speed = 10
snake_direction = 'RIGHT'

# 食物的初始位置
food = (200, 200)

# 计分板
score = 0
font = pygame.font.Font(None, 36)

# 时间控制变量
last_time = pygame.time.get_ticks()

# 定义函数：绘制蛇
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, snake_color, pygame.Rect(segment[0], segment[1], 10, 10))

# 定义函数：绘制食物
def draw_food(food):
    pygame.draw.rect(screen, food_color, pygame.Rect(food[0], food[1], 10, 10))

# 定义函数：绘制计分板
def draw_score(score):
    score_text = font.render("Score: {}".format(len(snake)), True, text_color)
    screen.blit(score_text, (width - 150, 20))

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not snake_direction == 'DOWN':
                snake_direction = 'UP'
            elif event.key == pygame.K_DOWN and not snake_direction == 'UP':
                snake_direction = 'DOWN'
            elif event.key == pygame.K_LEFT and not snake_direction == 'RIGHT':
                snake_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and not snake_direction == 'LEFT':
                snake_direction = 'RIGHT'

    # 移动蛇
    head = list(snake[0])
    if snake_direction == 'UP':
        head[1] -= 10
    elif snake_direction == 'DOWN':
        head[1] += 10
    elif snake_direction == 'LEFT':
        head[0] -= 10
    elif snake_direction == 'RIGHT':
        head[0] += 10

    snake.insert(0, tuple(head))

    # 检查是否吃到食物
    if snake[0] == food:
        food = (random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10)
    else:
        snake.pop()

    # 检查是否碰到自己
    if snake[0] in snake[1:]:
        pygame.quit()
        sys.exit()

    # 检查是否碰到边界
    if snake[0][0] < 0 or snake[0][0] >= width or snake[0][1] < 0 or snake[0][1] >= height:
        pygame.quit()
        sys.exit()

    # 控制蛇的增长
    current_time = pygame.time.get_ticks()
    if current_time - last_time > 1000:  # 每隔1秒增长一次
        last_time = current_time
        snake.append((0, 0))  # 在蛇的尾部添加一个新的段

    # 清空屏幕
    screen.fill(bg_color)

    # 绘制蛇和食物
    draw_snake(snake)
    draw_food(food)

    # 绘制计分板
    draw_score(score)

    # 刷新屏幕
    pygame.display.flip()

    # 控制游戏速度
    pygame.time.Clock().tick(snake_speed)
