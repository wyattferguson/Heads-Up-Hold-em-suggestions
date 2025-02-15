# :tada: Rough Refactor & Suggestions

So this is just a very rough once over of what you might want to consider in a refactor of your poker app. I tried to add useful comments explaining why things are moved around or changed.

Some key points to take away would be:

- Break up your code into useful components that try to do just one thing.
- When you find yourself using the same variables everywhere for a few functions its probably time to just make it a class.
- Use type hinting, makes it easier to dev your IDE will pick it up and helps reduce bugs.
- Try not to repeat your self, if you find you using similar blocks of code over and over, you can probably find a way to abstract that code away into a function or class to make your overall code much easier to read and maintain.
- Enums and dataclasses are super useful
- Write doc strings for your functions, makes everything easier to understand, and you will thank yourself later.
