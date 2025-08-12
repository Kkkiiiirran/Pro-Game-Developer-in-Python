
# Pygame Character Movement - Notes

This document summarizes key Python and Pygame concepts used in the character movement game code.

---

## 🔹 1. Imports

```python
import time
import pygame
```

- `pygame`: Used for 2D game development.
- `time`: Used for controlling the game loop delay (`sleep()` function).

---

## 🔹 2. Initialization

```python
pygame.init()
```

- Initializes all Pygame modules (required before using them).

---

## 🔹 3. Display Setup

```python
screen = pygame.display.set_mode([600, 600])
```

- Creates a window of size 600x600 pixels.

---

## 🔹 4. Loading Images

```python
player = pygame.image.load("character.png")
background = pygame.image.load("background.png")
```

- Loads images to be used for the player character and background.

---

## 🔹 5. Player Position and Controls

```python
player_x = 200
player_y = 200
keys = [False, False, False, False]
```

- `player_x` and `player_y`: Coordinates of the player on screen.
- `keys`: Tracks which arrow keys are currently pressed:
  - Index 0 → UP
  - Index 1 → DOWN
  - Index 2 → LEFT
  - Index 3 → RIGHT

---

## 🔹 6. Game Loop

```python
while running:
    # Game logic and drawing happen here
```

- The loop continues running until the user quits the game.

---

## 🔹 7. Drawing Images

```python
screen.blit(background, (0, 0))
screen.blit(player, (player_x, player_y))
pygame.display.flip()
```

- `blit()` draws images (surfaces) onto the screen.
- `flip()` updates the full screen with the new drawings.

---

## 🔹 8. Event Handling

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        exit(0)
```

- Detects and handles window close event and keyboard input events.

### 🔸 Keyboard Events

```python
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_UP:
        keys[0] = True
    # ...similar for other keys

if event.type == pygame.KEYUP:
    if event.key == pygame.K_UP:
        keys[0] = False
```

- Sets `keys` to `True` or `False` based on key presses/releases.

---

## 🔹 9. Movement Logic

```python
if keys[0] and player_y > 0:
    player_y -= 7
elif keys[1] and player_y < 536:
    player_y += 7

if keys[2] and player_x > 0:
    player_x -= 2
elif keys[3] and player_x < 536:
    player_x += 2
```

- Moves the player image based on key presses.
- Includes boundary checks to prevent moving off-screen.

---

## 🔹 10. Gravity Effect

```python
player_y += 5
```

- Adds a constant downward motion (simulating gravity).

---

## 🔹 11. Time Delay

```python
time.sleep(0.05)
```

- Slows down the game loop to make movement smoother and playable.

---

## ✅ Summary

| Concept                   | Description                                |
|---------------------------|--------------------------------------------|
| `pygame.init()`          | Initializes Pygame                         |
| `pygame.display.set_mode`| Creates game window                        |
| `pygame.image.load()`    | Loads sprites (player/background)          |
| `blit()` and `flip()`    | Draw and update screen                     |
| `pygame.event.get()`     | Handles user events (quit, keyboard)       |
| `pygame.KEYDOWN/KEYUP`   | Detects key presses/releases               |
| Movement logic           | Moves player and prevents screen overflow  |
| `time.sleep()`           | Controls game loop timing                  |
| Gravity simulation       | Adds downward pull on player               |

---

## 📌 File Paths (Important Note)

Ensure correct use of file paths. Use **double backslashes (`\\`)** or **raw strings**:

```python
player = pygame.image.load(r"Pro Game Developer in Python\LESSON-5\character.png")
```

Or use:

```python
player = pygame.image.load("Pro Game Developer in Python\\LESSON-5\\character.png")
```
