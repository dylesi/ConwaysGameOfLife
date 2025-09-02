import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# Store rects in a list
rects = [
    pygame.Rect(50, 50, 100, 100),
    pygame.Rect(200, 100, 150, 80),
    pygame.Rect(100, 250, 120, 120)
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check collision on mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos  # mouse position (x, y)

            for i, rect in enumerate(rects):
                if rect.collidepoint(pos):
                    print(f"Clicked inside rect {i}: {rect}")

    # Draw
    screen.fill((30, 30, 30))
    for rect in rects:
        pygame.draw.rect(screen, (200, 50, 50), rect, border_radius=8)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()