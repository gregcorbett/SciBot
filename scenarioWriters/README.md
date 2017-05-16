# Creating a new scenario
1. Choose a scenario name. It will be referred to below as `<name>`.

2. Copy `scenarioWriters/scenarioWriterBlank.py` to `scenarioWriters/scenarioWriter<name>.py`

3. At Line 10 onward, add the following:
```
# Initialises a new scenario object and sets the scenario name.
scenario = Scenario('<name>')
```

* Decide how big you want each square to be, in terms of pixels. If you already have a `BeeBot` image (or `Obstacle` images/`Goal` images), your squares should be the same size as this. Add the following code, but replace `n` with your number.
```
# The size of an individual square.
scenario.set_board_step(n)
```

* Decide how many squares you want your map to be. If you already have a background image, this will dictate the height and width. Add the following code, but replace `x` and `y` with your width and height in terms of squares.
```
# Sets the width of the map in terms of squares.
scenario.set_logical_width(x)
# Sets the height of the map in terms of squares.
scenario.set_logical_height(y)
```

* Decide where you want your `BeeBot` to start. Add the following code, replacing `x, y` with your starting co-ordinates.
```
# Sets the bee bot starting square.
scenario.set_beebot_start_position(x, y)
```

* Set your `BeeBot` sprite, it needs to be the same size as your squares. Add the following code, but replace `<sprite>` with the file path of your image.
```
# Set the BeeBot sprite.
scenario.set_beebot_sprite('<sprite>')
```

* You will need to tell the program which way you’re `BeeBot` sprite is facing, where 'UP' is `Heading.NORTH`. Add the following code, but replace <heading> with your heading.
```
# Sets the BeeBots starting direction, where "UP" is Heading.NORTH.
# (other options are Heading.EAST, Heading.SOUTH and Heading.WEST)
scenario.set_beebot_heading(<heading>)
```

* Set the background image. Add the following code, but replace <background> with the file path of your image.
```
# Sets the image on the map.
scenario.set_background('<background>')
```

* If the image has no grid, one can be added by adding the following code and replacing `(R, G, B)` with your chosen RGB colour.
```
scenario.set_border_colour((R, G, B))
```

* Obstacles, squares to avoid, need to be defined separately. To add an `Obstacle`, add the following code, but replace `x, y` with your `Obstacle` location.
  To add an `Obstacle` with an image, replace `x, y` with your `Obstacle` location and the file path of the image e.g. `(1, 2, './img/Default/obstacle1.jpg')`
```
# This line adds an obstacle.
scenario.add_obstacle(x, y)
```

* Goals, squares to reach, need to be defined separately also. To add a `Goal`, add the following code, but replace `x, y` with your `Goal` location.
  To add a `Goal` with an image, replace `x, y` with your `Goal` location and the file path of the image e.g. `(1, 2, './img/Default/goal1.jpg')`
```
# This line adds a goal.
scenario.add_goal(x, y)
```

* You can decide whether you want your goals to be completed in the order added, or in any order. Add one of the following blocks of code.
```
# This method means the goals must be met in the order added.
scenario.set_ordered_goals(True)
```
or
```
# This method means the goals can be met in any order.
scenario.set_ordered_goals(False)
```

* You'll need to set a sprite for when your BeeBot crashes. Add the following code, but replace `path` with the file path of the image.
```
# Sets the sprite to be displayed when the robot crashes
scenario.set_beebot_fail_sprite('path')
```

4. Finally, run `python scenarioWriters/ScenarioWriter<name>.py` to generate your `.scitbot` file.