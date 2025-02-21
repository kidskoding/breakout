from brick import brick_width, brick_height, Brick

rows = 5
cols = 8
bricks = []
colors = [
    (255, 0, 0),
    (255, 165, 0),
    (255, 255, 0),
    (0, 255, 0),
    (0, 0, 255)
]

margin_left = 5
margin_right = 5
margin_top = 30

class BrickGrid:
    def __init__(self):
        available_width = 640 - 5 - 5
        total_brick_width = cols * brick_width
        remaining_space = available_width - total_brick_width

        brick_spacing = remaining_space / (cols - 1)

        for row in range(rows):
            for col in range(cols):
                x = margin_left + col * (brick_width + brick_spacing)
                y = margin_top + row * (brick_height + 5)
                color = colors[row % len(colors)]
                bricks.append(Brick(color, x, y))

    def draw_grid(self, screen):
        for brick in bricks:
            brick.draw(screen)