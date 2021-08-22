# pygame_spinner

pygame_spinner is used to create board game-style spinners within pygame

## Installation

Clone the [github](https://github.com/tjw194/pygame_spinner) repository at https://github.com/tjw194/pygame_spinner.

```bash
pip install is not yet implemented
```

## Usage

An example implementation in a simple pygame loop is provided in main.py

```python
from spinner import Spinner, SpinnerArm

# create the spinner board object
spinner_board = Spinner(display, (400, 400), 300, 12)

# change the border colors
spinner_board.border_color = 'red'

# change the border width
spinner_board.border_width = 6

# turn off segment borders
spinner_board.borders = False

# change colors of spinner segments; default is ROYGBV if not changed
# colors will rotate through values in list to color all segments
spinner_board.color_list = ['purple4', 'yellow']

# show spinner board in pygame
spinner_board.show()


# create the spinner arm object
spinner_arm(display, (400, 400), 280)

# change color of spinner arm and center circle
spinner_arm.arm_color = 'pink'
spinner_arm.cap_color = 'orange'

# change arm width
spinner_arm.arm_width = 'gray'

# show spinner arm in pygame
spinner_arm.show()

# To animate spinning, use a pygame event to trigger a random speed
spinner_arm.speed = random.randrange(40, 75, 1)
spinner_arm.spin()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
Copyright (c) 2021 Todd Wilson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.