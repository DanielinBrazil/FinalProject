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

# Constants for drawing border around white keys
START_X = -50

# Define the notes and their corresponding sounds
notes = [
    ('B2', 'B2.mp3'), ('C3', 'C3.mp3'), ('Db3', 'Db3.mp3'), ('D3', 'D3.mp3'), ('Eb3', 'Eb3.mp3'),
    ('E3', 'E3.mp3'), ('F3', 'F3.mp3'), ('Gb3', 'Gb3.mp3'), ('G3', 'G3.mp3'),
    ('Ab3', 'Ab3.mp3'), ('A3', 'A3.mp3'), ('Bb3', 'Bb3.mp3'), ('B3', 'B3.mp3'),
    ('C4', 'C4.mp3'), ('Db4', 'Db4.mp3'), ('D4', 'D4.mp3'), ('Eb4', 'Eb4.mp3'),
    ('E4', 'E4.mp3'), ('F4', 'F4.mp3'), ('Gb4', 'Gb4.mp3'), ('G4', 'G4.mp3'),
    ('Ab4', 'Ab4.mp3'), ('A4', 'A4.mp3')
]

class Notes(pygame.sprite.Sprite):
    def __init__(self, image, x, y, sound, is_black=False):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = sound
        self.is_black = is_black  # Flag to determine if the note is a black key

    def update(self, events, black_keys):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:  # When mouse button is released
                if self.rect.collidepoint(event.pos):  # Check if clicked inside this key's rect
                    if self.sound:  # Check if the sound is available
                        # If this is a black key, play its sound
                        if self.is_black:
                            self.sound.play()
                            return True  # Indicate that a black key was pressed
                        else:
                            # If it's a white key, only play if no black key was pressed
                            if not any(black_key.rect.collidepoint(event.pos) for black_key in black_keys):
                                self.sound.play()
        return False  # Indicate that no black key was pressed


def load_sound(file_name):
    return pygame.mixer.Sound(os.path.join("Assets", file_name))

# Load sounds and create note sprites
white_keys = []
black_keys = []
idx_white = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
idx_black = [-1,0,1,2,3,4,5,6,7,8,9,10,11,12]
n = 0
for (note_name, sound_file) in notes:
    # Create white keys
    if note_name in ["B2", "C3", "D3", "E3", "F3", "G3", "A3", "B3", "C4", "D4", "E4", "F4", "G4", "A4"]:
        white_key = pygame.Surface((WHITE_KEY_WIDTH, WHITE_KEY_HEIGHT))
        white_key.fill(WHITE)
        white_keys.append(Notes(white_key, idx_white[n] * 100 - 50, 100, load_sound(sound_file)))
        white_sound = sound_file
        n += 1

    # Create black keys for specific notes
    if note_name in ['Db3', 'Eb3', 'Gb3', 'Ab3', 'Bb3', 'Db4', 'Eb4', 'Gb4', 'Ab4', 'Bb4']:
        black_key_x = (idx_black[n] * WHITE_KEY_WIDTH) + (WHITE_KEY_WIDTH - BLACK_KEY_WIDTH) / 2
        black_key = pygame.Surface((BLACK_KEY_WIDTH, BLACK_KEY_HEIGHT))
        black_key.fill(BLACK)
        black_keys.append(Notes(black_key, black_key_x, 100, load_sound(sound_file), is_black=True))

# make white and black keys groupings.
all_keys = pygame.sprite.Group(*white_keys, *black_keys)
white_keys_draw = pygame.sprite.Group(*white_keys)
black_keys_draw = pygame.sprite.Group(*black_keys)


def draw_window():
    WIN.fill(BLUE_GREEN)  # Background color
    
    #drawing white keys
    white_keys_draw.draw(WIN)

    # Draw borders for white keys
    for idx in range(len(white_keys)):
        pygame.draw.rect(WIN, WHITE_BORDER, ( START_X + idx * WHITE_KEY_WIDTH,100, WHITE_KEY_WIDTH, WHITE_KEY_HEIGHT), 3)

    #drawing black keys.
    black_keys_draw.draw(WIN)

    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        events = pygame.event.get()  # Get all events
        for event in events:
            if event.type == pygame.QUIT:  # Exit condition
                run = False
        # Update all notes based on events
        for note in all_keys:
            note.update(events, black_keys)

        draw_window()  # Render the window

    pygame.quit()

if __name__ == "__main__":
    main()
