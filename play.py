import pygame
import sys
import random

# 初始化
pygame.init()

# 游戏参数
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
FPS = 10

# 颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 初始化屏幕
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇游戏")

# 初始化时钟
clock = pygame.time.Clock()

# 初始化贪吃蛇
snake = [(100, 100), (90, 100), (80, 100)]
snake_dir = (GRID_SIZE, 0)

# 初始化食物
food = (random.randrange(1, (WIDTH//GRID_SIZE)) * GRID_SIZE,
        random.randrange(1, (HEIGHT//GRID_SIZE)) * GRID_SIZE)

# 计分板
score = 0

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 处理按键事件
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, GRID_SIZE):
        snake_dir = (0, -GRID_SIZE)
    if keys[pygame.K_DOWN] and snake_dir != (0, -GRID_SIZE):
        snake_dir = (0, GRID_SIZE)
    if keys[pygame.K_LEFT] and snake_dir != (GRID_SIZE, 0):
        snake_dir = (-GRID_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-GRID_SIZE, 0):
        snake_dir = (GRID_SIZE, 0)

    # 移动贪吃蛇
    head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, head)

    # 判断是否吃到食物
    if head == food:
        score += 1
        food = (random.randrange(1, (WIDTH//GRID_SIZE)) * GRID_SIZE,
                random.randrange(1, (HEIGHT//GRID_SIZE)) * GRID_SIZE)
    else:
        snake.pop()

    # 判断是否碰到边界或自己
    if (
        head[0] < 0 or
        head[0] >= WIDTH or
        head[1] < 0 or
        head[1] >= HEIGHT or
        head in snake[1:]
    ):
        print("Game Over! Your Score:", score)
        pygame.quit()
        sys.exit()

    # 渲染屏幕
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    # 显示得分
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    # 控制帧率
    clock.tick(FPS)

