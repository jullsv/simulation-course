import pygame
import numpy as np
import random
from enum import IntEnum

class CellState(IntEnum):
    EMPTY = 0
    TREE = 1
    BURNING = 2

pygame.init()

CELL_SIZE = 8
GRID_WIDTH = 80
GRID_HEIGHT = 80
WIDTH = GRID_WIDTH * CELL_SIZE
GRID_AREA_HEIGHT = GRID_HEIGHT * CELL_SIZE
CONTROL_PANEL_HEIGHT = 200
HEIGHT = GRID_AREA_HEIGHT + CONTROL_PANEL_HEIGHT
FPS = 60 
COLORS = {
    CellState.EMPTY: (240, 230, 140),
    CellState.TREE: (34, 139, 34),
    CellState.BURNING: (255, 69, 0),
    'TEXT': (0, 0, 0),
    'BACKGROUND': (255, 255, 255),
    'PANEL_BACKGROUND': (220, 220, 220),
    'PANEL_BORDER': (100, 100, 100)
}

class ForestFireSimulation:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Моделирование лесных пожаров")
        self.clock = pygame.time.Clock()
        
        self.last_update_time = pygame.time.get_ticks()
        self.update_delay = 500 
        
        self.p = 0.01
        self.f = 0.001
        
        self.wind_direction = (0, 0)
        self.wind_speed = 0
        self.humidity = 0.3
        self.slope = 0
        
        self.grid = np.random.choice(
            [CellState.TREE, CellState.EMPTY], 
            size=(GRID_HEIGHT, GRID_WIDTH), 
            p=[0.7, 0.3]
        )
        
        self.running = True
        self.paused = False
        
        self.font_small = pygame.font.Font(None, 18)
        self.font_medium = pygame.font.Font(None, 22)
        self.font_bold = pygame.font.Font(None, 24)
        
        self.setup_initial_fire()
    
    def setup_initial_fire(self):
        center_x, center_y = GRID_WIDTH // 4, GRID_HEIGHT // 2
        for i in range(-3, 4):
            for j in range(-3, 4):
                if 0 <= center_y + j < GRID_HEIGHT and 0 <= center_x + i < GRID_WIDTH:
                    if random.random() < 0.5:
                        self.grid[center_y + j, center_x + i] = CellState.BURNING
    
    def get_neighbors(self, x, y):
        neighbors = []
        directions = [
            (-1, -1), (0, -1), (1, -1),
            (-1,  0),          (1,  0),
            (-1,  1), (0,  1), (1,  1)
            ]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT:
                neighbors.append((nx, ny, dx, dy))
        return neighbors
    
    def calculate_spread_probability(self, dx, dy):
        base_prob = 0.4 
        if self.wind_speed > 0:
            wind_factor = (dx * self.wind_direction[0] + dy * self.wind_direction[1])
            base_prob *= (1 + 0.4 * self.wind_speed * wind_factor)
        base_prob *= (1 - self.humidity * 0.7)
        if dy < 0: base_prob *= (1 + self.slope * 0.5)
        else: base_prob *= (1 - self.slope * 0.3)
        return max(0.0, min(1.0, base_prob))
    
    def update(self):
        new_grid = self.grid.copy()
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                state = self.grid[y, x]
                if state == CellState.BURNING:
                    new_grid[y, x] = CellState.EMPTY
                elif state == CellState.TREE:
                    neighbors = self.get_neighbors(x, y)
                    for nx, ny, dx, dy in neighbors:
                        if self.grid[ny, nx] == CellState.BURNING:
                            if random.random() < self.calculate_spread_probability(dx, dy):
                                new_grid[y, x] = CellState.BURNING
                                break
                    else:
                        if random.random() < self.f: new_grid[y, x] = CellState.BURNING
                elif state == CellState.EMPTY:
                    if random.random() < self.p: new_grid[y, x] = CellState.TREE
        self.grid = new_grid

    def draw(self):
        self.screen.fill(COLORS['BACKGROUND'])
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                pygame.draw.rect(self.screen, COLORS[self.grid[y, x]], 
                                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        self.draw_control_panel()

    def draw_control_panel(self):
        panel_rect = pygame.Rect(0, GRID_AREA_HEIGHT, WIDTH, CONTROL_PANEL_HEIGHT)
        pygame.draw.rect(self.screen, COLORS['PANEL_BACKGROUND'], panel_rect)
        pygame.draw.line(self.screen, COLORS['PANEL_BORDER'], (0, GRID_AREA_HEIGHT), (WIDTH, GRID_AREA_HEIGHT), 2)
        
        stats_y = GRID_AREA_HEIGHT + 10
        stats = [
            f"Деревьев: {np.sum(self.grid == CellState.TREE)}",
            f"Горит: {np.sum(self.grid == CellState.BURNING)}",
            f"Обновление: {self.update_delay}мс",
            f"",
            f"Ветер: {self.get_wind_arrow()} (ск.: {self.wind_speed:.1f})",
            f"Влажность: {self.humidity:.2f}",
            f"Уклон: {self.slope:.2f}"
        ]
        for i, stat in enumerate(stats):
            txt = self.font_medium.render(stat, True, COLORS['TEXT'])
            self.screen.blit(txt, (10, stats_y + i * 22))

        controls_start_x = 320
        
        title_wind = self.font_bold.render("ВЕТЕР / УКЛОН", True, (0, 100, 0))
        self.screen.blit(title_wind, (controls_start_x, stats_y))
        
        wind_instr = [
            "Стрелки - напр. ветра",
            f"1/2 - скор. ветра",
            f"9/0 - наклон холма",
        ]
        for i, line in enumerate(wind_instr):
            txt = self.font_small.render(line, True, COLORS['TEXT'])
            self.screen.blit(txt, (controls_start_x, stats_y + 25 + i * 18))

        col2_x = controls_start_x + 180
        title_sys = self.font_bold.render("СИСТЕМА", True, (0, 100, 0))
        self.screen.blit(title_sys, (col2_x, stats_y))
        
        sys_instr = [
            "3/4 - влажность",
            "SPACE - пауза",
            "R - сброс",
            "ESC - выход"
        ]
        for i, line in enumerate(sys_instr):
            txt = self.font_small.render(line, True, COLORS['TEXT'])
            self.screen.blit(txt, (col2_x, stats_y + 25 + i * 18))

    def get_wind_arrow(self):
        arrows = {(0, -1): "верх", (0, 1): "низ", (-1, 0): "лево", (1, 0): "право"}
        return arrows.get(self.wind_direction, "·")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: self.running = False
                elif event.key == pygame.K_SPACE: self.paused = not self.paused
                elif event.key == pygame.K_r: self.__init__()
                elif event.key == pygame.K_UP: self.wind_direction = (0, -1)
                elif event.key == pygame.K_DOWN: self.wind_direction = (0, 1)
                elif event.key == pygame.K_LEFT: self.wind_direction = (-1, 0)
                elif event.key == pygame.K_RIGHT: self.wind_direction = (1, 0)
                elif event.key == pygame.K_1: self.wind_speed = max(0, self.wind_speed - 0.1)
                elif event.key == pygame.K_2: self.wind_speed = min(3, self.wind_speed + 0.1)
                elif event.key == pygame.K_3: self.humidity = max(0, self.humidity - 0.05)
                elif event.key == pygame.K_4: self.humidity = min(1, self.humidity + 0.05)
                elif event.key == pygame.K_9: self.slope = max(-1, self.slope - 0.1)
                elif event.key == pygame.K_0: self.slope = min(1, self.slope + 0.1)

    def run(self):
        while self.running:
            self.handle_events()
            curr = pygame.time.get_ticks()
            if not self.paused and curr - self.last_update_time > self.update_delay:
                self.update()
                self.last_update_time = curr
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()

if __name__ == "__main__":
    ForestFireSimulation().run()