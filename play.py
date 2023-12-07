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

# 初始化 Pygame GUI
pygame_gui.init()

# 设置 Pygame GUI 的字体
pygame.font.init()
font = pygame.font.Font(None, 36)

# 设置 Pygame GUI 的主题
theme = pygame_gui.themes.THEME_DARK
manager = pygame_gui.UIManager((WIDTH, HEIGHT), theme)

# 新增一个变量来标识游戏状态
game_active = True

while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ... （处理按键事件、移动贪吃蛇等，与之前的代码相同）

    # 判断是否碰到边界或自己
    if (
        head[0] < 0 or
        head[0] >= WIDTH or
        head[1] < 0 or
        head[1] >= HEIGHT or
        head in snake[1:]
    ):
        game_active = False  # 游戏结束
        score_text = font.render(f"Game Over! Your Score: {score}", True, (255, 0, 0))
        text_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

        # 添加重新开始按钮
        restart_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((WIDTH // 2 - 100, HEIGHT // 2 + 50), (200, 50)),
            text='Restart',
            manager=manager
        )

        # 添加退出按钮
        quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((WIDTH // 2 - 100, HEIGHT // 2 + 120), (200, 50)),
            text='Quit',
            manager=manager
        )

    # 渲染屏幕
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    if not game_active:
        screen.blit(score_text, text_rect)

    # 显示得分
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # 更新 Pygame GUI 管理器
    manager.update(FPS / 1000.0)

    # 渲染 Pygame GUI 管理器
    manager.draw_ui(screen)

    pygame.display.flip()

    # 控制帧率
    clock.tick(FPS)

    # 处理 Pygame GUI 事件
    gui_event = pygame.event.poll()
    if gui_event.type == pygame.USEREVENT and gui_event.user_type == pygame_gui.UI_BUTTON_PRESSED:
        if gui_event.ui_element == restart_button:
            # 重新开始游戏
            game_active = True
            snake = [(100, 100), (90, 100), (80, 100)]
            snake_dir = (GRID_SIZE, 0)
            food = (random.randrange(1, (WIDTH//GRID_SIZE)) * GRID_SIZE,
                    random.randrange(1, (HEIGHT//GRID_SIZE)) * GRID_SIZE)
            score = 0
        elif gui_event.ui_element == quit_button:
            pygame.quit()
            sys.exit()