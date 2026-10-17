# templerun.py
# Simple Temple Run-like infinite runner implemented with Pygame
# Controls:
#   Left / Right arrows -> change lane
#   Up or Space -> jump
#   R -> restart after game over
#   Esc or window close -> quit

import pygame
import random
import sys

# ---- Config ----
SCREEN_W, SCREEN_H = 800, 500
FPS = 60

LANES = 3
TRACK_WIDTH = int(SCREEN_W * 0.6)
LANE_WIDTH = TRACK_WIDTH // LANES
LANE_X_START = (SCREEN_W - TRACK_WIDTH) // 2

PLAYER_W, PLAYER_H = 36, 56
PLAYER_Z_POS = 150  # reference z on screen (not used for 3D math here, only for spawn distance)
GRAVITY = 1.0
JUMP_V = -18

OBSTACLE_MIN_SIZE = 24
OBSTACLE_MAX_SIZE = 64
OBSTACLE_SPAWN_GAP = 1200  # in game distance units (we'll convert to time using speed)
COIN_SPAWN_GAP = 700

# Colors
BG_TOP = (15, 26, 43)
BG_BOTTOM = (7, 20, 39)
TRACK_COLOR = (7, 25, 52)
LANE_COLOR = (36, 49, 75)
PLAYER_COLOR = (45, 227, 182)
HEAD_COLOR = (255, 218, 186)
OBSTACLE_COLOR = (139, 62, 47)
COIN_COLOR = (255, 210, 77)
TEXT_COLOR = (230, 238, 249)

# ---- Helper ----
def lane_center_x(lane_index):
    return LANE_X_START + lane_index * LANE_WIDTH + LANE_WIDTH // 2

# ---- Game classes ----
class Player:
    def __init__(self):
        self.lane = 1  # start middle
        self.x = lane_center_x(self.lane)
        self.y = 0  # vertical offset above ground; 0 = on ground
        self.vy = 0
        self.on_ground = True
        self.width = PLAYER_W
        self.height = PLAYER_H

    def update(self):
        # smooth x towards lane center
        target_x = lane_center_x(self.lane)
        self.x += (target_x - self.x) * 0.25

        if not self.on_ground:
            self.vy += GRAVITY
            self.y += self.vy
            if self.y >= 0:
                self.y = 0
                self.vy = 0
                self.on_ground = True

    def jump(self):
        if self.on_ground:
            self.vy = JUMP_V
            self.on_ground = False

    def rect(self, track_y):
        # return screen rect for collision/drawing
        px = int(self.x - self.width // 2)
        py = int(track_y - 10 - self.height - self.y)
        return pygame.Rect(px, py, self.width, self.height)

class Obstacle:
    def __init__(self, lane, size, dist):
        self.lane = lane
        self.size = size
        self.dist = dist  # distance from player on spawn (z)
        # as it moves, dist decreases

    def update(self, speed):
        self.dist -= speed

    def screen_pos(self, track_y):
        # convert dist to a simple perspective - closer = lower on screen
        # clamp perspective factor
        depth = max(0.2, 1.0 - (self.dist / 1200.0))
        sx = lane_center_x(self.lane)
        # y becomes nearer to the track with depth
        sy = track_y - 10 - depth * 60 + (self.size * depth * 0.2)
        w = int(self.size * depth)
        h = int(self.size * depth)
        return (int(sx - w // 2), int(sy - h), w, h)

    def collides_with_player(self, player, track_y):
        # simple check: if lane equal and dist near, compare rects
        if self.lane != player.lane:
            return False
        if abs(self.dist - PLAYER_Z_POS) > 60:
            return False
        ox, oy, ow, oh = self.screen_pos(track_y)
        obst_rect = pygame.Rect(ox, oy, ow, oh)
        return obst_rect.colliderect(player.rect(track_y))

class Coin:
    def __init__(self, lane, dist):
        self.lane = lane
        self.dist = dist

    def update(self, speed):
        self.dist -= speed

    def screen_pos(self, track_y):
        depth = max(0.2, 1.0 - (self.dist / 1200.0))
        sx = lane_center_x(self.lane)
        sy = track_y - 30 - depth * 60
        r = int(10 * depth)
        return (int(sx), int(sy), r)

    def collides_with_player(self, player, track_y):
        if self.lane != player.lane:
            return False
        if abs(self.dist - PLAYER_Z_POS) > 50:
            return False
        cx, cy, r = self.screen_pos(track_y)
        pr = player.rect(track_y)
        # circle-rect simple check
        closest_x = max(pr.left, min(cx, pr.right))
        closest_y = max(pr.top, min(cy, pr.bottom))
        dx = cx - closest_x
        dy = cy - closest_y
        return dx * dx + dy * dy <= r * r

# ---- Main game ----
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Temple Run - Pygame Mini")
    clock = pygame.time.Clock()
    font_big = pygame.font.SysFont(None, 48)
    font_small = pygame.font.SysFont(None, 24)

    def reset_state():
        return {
            "player": Player(),
            "speed": 6.0,
            "distance": 0.0,   # cumulative scroll distance
            "obstacles": [],
            "coins": [],
            "spawn_acc": 0.0,
            "coin_acc": 0.0,
            "score": 0,
            "game_over": False
        }

    state = reset_state()

    track_y = int(SCREEN_H * 0.6)

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0  # seconds
        # we'll use dt to keep frame independent behavior but make spawn based on speed/distance
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if state["game_over"]:
                    if event.key == pygame.K_r:
                        state = reset_state()
                else:
                    if event.key == pygame.K_LEFT:
                        state["player"].lane = max(0, state["player"].lane - 1)
                    elif event.key == pygame.K_RIGHT:
                        state["player"].lane = min(LANES - 1, state["player"].lane + 1)
                    elif event.key in (pygame.K_UP, pygame.K_SPACE):
                        state["player"].jump()

        # if game over, skip updating objects except for input
        if not state["game_over"]:
            # update "scroll" distance and difficulty
            speed = state["speed"]
            state["distance"] += speed
            # gradually increase speed with distance
            if int(state["distance"]) % 1000 < speed:
                state["speed"] += 0.12

            # spawn obstacles based on distance accumulator
            state["spawn_acc"] += speed
            if state["spawn_acc"] > 160:
                # spawn one obstacle
                lane = random.randrange(LANES)
                size = random.randint(OBSTACLE_MIN_SIZE, OBSTACLE_MAX_SIZE)
                dist = SCREEN_W + random.randint(100, 400)
                state["obstacles"].append(Obstacle(lane, size, dist))
                state["spawn_acc"] = 0

            # spawn coins
            state["coin_acc"] += speed
            if state["coin_acc"] > 90:
                lane = random.randrange(LANES)
                dist = SCREEN_W + random.randint(120, 420)
                state["coins"].append(Coin(lane, dist))
                state["coin_acc"] = 0

            # update obstacles/coins
            for o in state["obstacles"]:
                o.update(state["speed"])
            for c in state["coins"]:
                c.update(state["speed"])

            # remove passed objects (dist < -200)
            state["obstacles"] = [o for o in state["obstacles"] if o.dist > -200]
            state["coins"] = [c for c in state["coins"] if c.dist > -200]

            # update player physics
            state["player"].update()

            # collisions
            for o in state["obstacles"]:
                if o.collides_with_player(state["player"], track_y):
                    # if obstacle small and player jumped high enough allow pass
                    # keep simple: any hit = game over
                    state["game_over"] = True
                    break

            # coins
            new_coins = []
            for c in state["coins"]:
                if c.collides_with_player(state["player"], track_y):
                    state["score"] += 10
                else:
                    new_coins.append(c)
            state["coins"] = new_coins

        # ---- Drawing ----
        # gradient background
        grd = pygame.Surface((SCREEN_W, SCREEN_H))
        for y in range(SCREEN_H):
            t = y / (SCREEN_H - 1)
            r = int(BG_TOP[0] * (1 - t) + BG_BOTTOM[0] * t)
            g = int(BG_TOP[1] * (1 - t) + BG_BOTTOM[1] * t)
            b = int(BG_TOP[2] * (1 - t) + BG_BOTTOM[2] * t)
            pygame.draw.line(grd, (r, g, b), (0, y), (SCREEN_W, y))
        screen.blit(grd, (0, 0))

        # track
        pygame.draw.rect(screen, TRACK_COLOR, (0, track_y - 40, SCREEN_W, 120))
        # lanes
        for i in range(LANES):
            x = LANE_X_START + i * LANE_WIDTH
            pygame.draw.rect(screen, LANE_COLOR, (x, track_y - 40, LANE_WIDTH - 8, 120))

        # perspective markers
        for i in range(40):
            z = i * 60 + (int(state["distance"]) % 60)
            scale = max(0.02, 1 - (z / 1200.0))
            line_w = int(4 * scale)
            center = SCREEN_W // 2
            alpha = int(15 * scale)
            marker = pygame.Surface((line_w, 6), pygame.SRCALPHA)
            marker.fill((255, 255, 255, alpha))
            screen.blit(marker, (center - line_w // 2, track_y - 8 + i * 18))

        # draw obstacles
        for o in state["obstacles"]:
            ox, oy, ow, oh = o.screen_pos(track_y)
            pygame.draw.rect(screen, OBSTACLE_COLOR, (ox, oy, ow, oh))
            # shadow
            pygame.draw.rect(screen, (0, 0, 0, 120), (ox, track_y + 20, ow, 6))

        # draw coins
        for c in state["coins"]:
            cx, cy, r = c.screen_pos(track_y)
            pygame.draw.circle(screen, COIN_COLOR, (cx, cy), max(1, r))

        # draw player
        pr = state["player"].rect(track_y)
        pygame.draw.rect(screen, PLAYER_COLOR, pr)
        # head
        head_center = (pr.centerx, pr.top - 12)
        pygame.draw.circle(screen, HEAD_COLOR, head_center, 14)

        # HUD
        score_surf = font_small.render(f"Score: {state['score']}", True, TEXT_COLOR)
        screen.blit(score_surf, (20, 20))

        hint_surf = font_small.render("← → lane   ↑ / Space jump   R restart", True, TEXT_COLOR)
        screen.blit(hint_surf, (SCREEN_W // 2 - hint_surf.get_width() // 2, 20))

        if state["game_over"]:
            overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            screen.blit(overlay, (0, 0))
            go_surf = font_big.render("Game Over", True, (255, 255, 255))
            sub_surf = font_small.render("Press R to restart", True, (240, 240, 240))
            screen.blit(go_surf, (SCREEN_W // 2 - go_surf.get_width() // 2, SCREEN_H // 2 - 40))
            screen.blit(sub_surf, (SCREEN_W // 2 - sub_surf.get_width() // 2, SCREEN_H // 2 + 10))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
