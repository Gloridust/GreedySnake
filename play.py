import pygame
import sys
import random

# 游戏参数
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
FPS = 10

# 颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def main():
    pygame.init()

    # 初始化屏幕
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("贪吃蛇游戏")

    # 初始化时钟
    clock = pygame.time.Clock()

    while True:
        run_game(screen, clock)

def run_game(screen, clock):
    # 初始化贪吃蛇
    snake = [(100, 100), (90, 100), (80, 100)]
    snake_dir = (GRID_SIZE, 0)

    # 初始化食物
    food = generate_food()

    # 计分板
    score = 0

    # 游戏进行标志
    game_over_flag = False

    while not game_over_flag:
        snake_dir, game_over_flag = handle_events(snake_dir, game_over_flag)

        # 如果游戏结束，等待按键
        if game_over_flag:
            render_game_over(screen, score)
            wait_for_key()
            return  # 重新开始游戏

        # 移动贪吃蛇
        head = move_snake(snake, snake_dir)

        # 判断是否吃到食物
        if head == food:
            score += 1
            food = generate_food()
        else:
            snake.pop()

        # 判断是否碰到边界或自己
        if is_collision(head, snake):
            game_over_flag = True

        # 渲染屏幕
        render_screen(screen, snake, food, score)

        # 控制帧率
        clock.tick(FPS)

def handle_events(snake_dir, game_over_flag):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, GRID_SIZE):
        return (0, -GRID_SIZE), game_over_flag
    elif keys[pygame.K_DOWN] and snake_dir != (0, -GRID_SIZE):
        return (0, GRID_SIZE), game_over_flag
    elif keys[pygame.K_LEFT] and snake_dir != (GRID_SIZE, 0):
        return (-GRID_SIZE, 0), game_over_flag
    elif keys[pygame.K_RIGHT] and snake_dir != (-GRID_SIZE, 0):
        return (GRID_SIZE, 0), game_over_flag
    elif keys[pygame.K_SPACE] and game_over_flag:
        return (GRID_SIZE, 0), False  # 重新开始游戏
    else:
        return snake_dir, game_over_flag

def move_snake(snake, snake_dir):
    head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, head)
    return head

def generate_food():
    return (random.randrange(1, (WIDTH // GRID_SIZE)) * GRID_SIZE,
            random.randrange(1, (HEIGHT // GRID_SIZE)) * GRID_SIZE)

def is_collision(head, snake):
    return (
        head[0] < 0 or
        head[0] >= WIDTH or
        head[1] < 0 or
        head[1] >= HEIGHT or
        head in snake[1:]
    )

def render_screen(screen, snake, food, score):
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

def render_game_over(screen, score):
    screen.fill(WHITE)

    font = pygame.font.Font(None, 72)
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))

    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + 50))

    pygame.display.flip()

def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

        pygame.time.delay(50)  # 添加延迟以减轻 CPU 负载

    pygame.event.clear()  # 清除事件队列，防止按键被重复处理


if __name__ == "__main__":
    main()
