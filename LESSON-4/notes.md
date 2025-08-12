# 🎮 Pygame Functions Used - Birthday Greeting Card

This document explains the Pygame functions used in the script.

---

## 🖥️ Display & Initialization

### `pygame.init()`
- Initializes all imported Pygame modules.
- Must be called before using most Pygame functions.

### `pygame.display.set_mode([width, height])`
- Creates a window or screen for display.
- Returns a `Surface` object to draw on.
- Example: `pygame.display.set_mode([600, 600])`

### `pygame.display.set_caption("Title")`
- Sets the title of the Pygame window.
- Useful for naming your app or game window.

---

## 🎨 Drawing & Rendering

### `screen.fill(color)`
- Fills the screen surface with a solid color.
- Takes an RGB tuple. Example: `(255, 255, 255)` for white.

### `screen.blit(source_surface, (x, y))`
- Draws (`blits`) one image or surface onto another.
- Commonly used to place images or text onto the screen.
- Example: `screen.blit(image, (0, 0))`

### `pygame.display.update()`
- Updates the full display surface to the screen.
- Must be called after drawing/blitting to show changes.

---

## 🖼️ Images

### `pygame.image.load("path")`
- Loads an image from the specified file path.
- Returns a `Surface` object.
- Example: `pygame.image.load("background.jpg")`

### `pygame.transform.scale(surface, (width, height))`
- Scales an image to the specified size.
- Returns a new surface with the resized image.
- Example: `pygame.transform.scale(img, (600, 600))`

---

## 🅰️ Text

### `pygame.font.SysFont(name, size)`
- Loads a system font.
- Returns a `Font` object.
- Example: `pygame.font.SysFont("Arial", 36)`

### `font.render(text, antialias, color)`
- Renders text as a new Surface object.
- `antialias`: Boolean for smoothing the text.
- `color`: RGB tuple for text color.
- Example: `font.render("Happy", True, (0, 0, 0))`

---

## 🛑 Quit

### `pygame.quit()`
- Uninitializes all Pygame modules.
- Should be called when exiting the program to clean up properly.

---
