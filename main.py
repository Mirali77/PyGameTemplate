from init import *


# Цикл игры
running = True
while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)

    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()
    screen.fill(BLACK)

    # Визуализация (сборка)
    pygame.display.flip()

pygame.quit()
