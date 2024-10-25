import os
import pygame

pygame.init()
pygame.mixer.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE_GREEN = (71, 88, 199)
WHITE_BORDER = (200, 200, 200)  # Border color

# Window dimensions
WIDTH, HEIGHT = 1300, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Piano")

# Frames per second
FPS = 60

# Constants for key dimensions
WHITE_KEY_WIDTH = 100
WHITE_KEY_HEIGHT = 300
BLACK_KEY_WIDTH = 60
BLACK_KEY_HEIGHT = 180

# Define the notes and their corresponding sounds
notes = [
    ('C3', 'C3.mp3'), ('Db3', 'Db3.mp3'), ('D3', 'D3.mp3'), ('Eb3', 'Eb3.mp3'),
    ('E3', 'E3.mp3'), ('F3', 'F3.mp3'), ('Gb3', 'Gb3.mp3'), ('G3', 'G3.mp3'),
    ('Ab3', 'Ab3.mp3'), ('A3', 'A3.mp3'), ('Bb3', 'Bb3.mp3'), ('B3', 'B3.mp3'),
    ('C4', 'C4.mp3')
]


class Notes(pygame.sprite.Sprite):
    def __init__(self, image, x, y, sound):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = sound

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.sound.play()


def load_sound(file_name):
    return pygame.mixer.Sound(os.path.join("Assets", file_name))


# Load sounds and create note sprites
white_keys = []
black_keys = []

for idx, (note_name, sound_file) in enumerate(notes):
    # Create white keys
    white_key = pygame.Surface((WHITE_KEY_WIDTH, WHITE_KEY_HEIGHT))
    white_key.fill(WHITE)
    white_keys.append(Notes(white_key, idx * WHITE_KEY_WIDTH, 100, load_sound(sound_file)))

    # Create black keys for specific notes
    if note_name in ['Db3', 'Eb3', 'Gb3', 'Ab3', 'Bb3']:
        black_key = pygame.Surface((BLACK_KEY_WIDTH, BLACK_KEY_HEIGHT))
        black_key.fill(BLACK)
        black_keys.append(
            Notes(black_key, (idx + 0.5) * WHITE_KEY_WIDTH - BLACK_KEY_WIDTH / 2, 100, load_sound(sound_file)))

# Combine all notes into a single sprite group
all_keys = pygame.sprite.Group(*white_keys, *black_keys)


def draw_window():
    WIN.fill(BLUE_GREEN)  # Background color

    # Draw all keys
    all_keys.draw(WIN)

    # Draw borders for white keys
    for idx in range(len(white_keys)):
        pygame.draw.rect(WIN, WHITE_BORDER, (idx * WHITE_KEY_WIDTH, 100, WHITE_KEY_WIDTH, WHITE_KEY_HEIGHT), 3)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        events = pygame.event.get()  # Get events inside the main loop
        for event in events:
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    sounda = pygame.mixer.Sound(os.path.join("Assets", "C3.mp3"))
                    sounda.play()
                if event.key == pygame.K_d:
                    sounda = pygame.mixer.Sound(os.path.join("Assets", "D3.mp3"))
                    sounda.play()
                if event.key == pygame.K_e:
                    sounda = pygame.mixer.Sound(os.path.join("Assets", "E3.mp3"))
                    sounda.play()
                if event.key == pygame.K_f:
                    sounda = pygame.mixer.Sound(os.path.join("Assets", "F3.mp3"))
                    sounda.play()
                if event.key == pygame.K_g:
                    sounda = pygame.mixer.Sound(os.path.join("Assets", "G3.mp3"))
                    sounda.play()
                if event.key == pygame.K_a:
                    sounda = pygame.mixer.Sound(os.path.join("Assets", "A3.mp3"))
                    sounda.play()
                if event.key == pygame.K_b:
                    sounda = pygame.mixer.Sound(os.path.join("Assets", "B3.mp3"))
                    sounda.play()

        all_keys.update(events)
        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
