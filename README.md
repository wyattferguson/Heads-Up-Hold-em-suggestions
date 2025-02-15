# :tada: Rough Refactor & Suggestions

So this is just a very very rough once over refactor of what would be some good steps to take and might learn from. I tried to add useful comments explaining why things are moved around or changed. Most of the actaully poker logic I lifted out, but this is more just a rough base to look at. Hopefully it helps.

## Some key points to take away would be:

- Break up your code into useful components that try to do just one thing.
- When you find yourself using the same variables everywhere for a few functions its probably time to just make it a class.
- Use type hinting, makes it easier to dev your IDE will pick it up and helps reduce bugs.
- Try not to repeat your self, if you find you using similar blocks of code over and over, you can probably find a way to abstract that code away into a function or class to make your overall code much easier to read and maintain.
- Enums and dataclasses are super useful
- Write doc strings for your functions, makes everything easier to understand, and you will thank yourself later.
- All the files have a little example script at the bottom to show how everything works

## Things that are not included:

- Determining winning hand
- Determing the next players move logic, each player has a next_move function, which is where that would live.
- All the extras of computing ante levels, betting amounts, pot management,etc...
- Basically everything for the actually gameplay, this is all just a skeleton of how as you learn might want to rework your code.
