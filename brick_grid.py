from brick import brick_width, brick_height, Brick

margin_left = 5
margin_right = 5
margin_top = 30

class BrickGrid:
    def __init__(self):
        self.rows = 5
        self.cols = 8
        self.bricks = []
        self.colors = [
            (255, 0, 0),
            (255, 165, 0),
            (255, 255, 0),
            (0, 255, 0),
            (0, 0, 255)
        ]
        available_width = 640 - 5 - 5
        total_brick_width = self.cols * brick_width
        remaining_space = available_width - total_brick_width

        brick_spacing = remaining_space / (self.cols - 1)

        for row in range(self.rows):
            for col in range(self.cols):
                x = margin_left + col * (brick_width + brick_spacing)
                y = margin_top + row * (brick_height + 5)
                color = self.colors[row % len(self.colors)]
                self.bricks.append(Brick(color, x, y))

    def draw_grid(self, screen):
        for brick in self.bricks:
            brick.draw(screen)