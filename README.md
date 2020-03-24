# jump-n-run

Basic 2D platformer built with python3 and pygame.

## Getting Started

Make sure you have python and pygame installed 
(tested with `python 3.7.7` and `pygame 1.9.6`), then just run `main.py`.  

## main.py
Let's look into `main.py`:

```python
from Game import Game

g = Game()
g.load_level('./level/current.txt')
g.mainloop()
```

Pretty straightforward, huh? Create an instance of `Game`, 
load your level by specifying the path and start the mainloop.

## Level-editing
As the levels are just `.txt`-files, you can easily create your own levels.
Every char in the lvl file will be translated to one block. With the default config
you can go 15 blocks high. Level length is calculated dynamically and the camera will 
move accordingly. So the (horizontal) sky is the limit ;)

Currently there
are 4 different block types:
```text
1                 SOLID    Use it as ground, wall, or ceiling
2                 DEADLY   You know it, you love it, but if you touch it, you're dead
x                 SPAWN    The player will spawn right in this tile
Everything else   AIR      The player will just pass through these tiles
``` 

- What happens if I call `load_level` multiple times?  
--> The last call counts, so the last level will be loaded
- Can I load levels after calling mainloop?  
--> Yes and no. You can't do it in main.py after calling `g.mainloop()`, because when
the program reaches your code, the mainloop won't run anymore. But if you load it 
inside the mainloop it'll work.

## config.py
You can change basically all important game parameters in `config.py`. And who doesn't
love to play around with block-size, colors, player-controls or player-physics??