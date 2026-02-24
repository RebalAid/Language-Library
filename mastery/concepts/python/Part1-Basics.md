# Basics to python!
## Before we start...
1. Install python version 3 or later, I'd recommend you download the latest version. (Note: If you use Linux, this isn't necessary as it is installed by default)
2. Use an IDE, code or text editor, just as long as it supports code functionality. I recommend Zed, VSCodium, Vim, Neovim, Nano, or Gnu Emacs, or pick any IDE you want, idc.
3. Create your own file, the python's official file extension is .py

## Lets start programming!
If you are in an IDE or whatever, follow this guide along.
```
print("Hello World!")
```

## Lets explain.
To know what we wrote, we gotta know what it means.
`print()` is a function, it is designed for a very particuler task, that is printing or "outputing" anything we want.
`("Hello World!")` this is an arguement, we want the `print()` function to output something so that we can see what it says.

## What is this?
### Explaining functions
A function is a piece of re-usable code that is or can be designed to perform a task. To know whenever it is a function or not, the end of it should have the parathenses "()" which is an execution trigger, but can also be anything, will be discussing about this in later guides.
Simply put, a function is a way of saying "We call this guy to do something for us, and we want him to perform a task for us"

`print()` is a function designed to print outputs, or more simply: A guy we call over to perform a task, to give out a speech for the audience, as we give him a script to say what we want.

You might be curious as to how functions are made, or how to make one in the first place:
```
def main():
  get_input = input("Please pick a number")
  return get_input

main()
```

This is what making a function looks like, we will get into that just a bit in later guides.

### Difference between arguement and paramater?
An arguement are actual values you pass into the function when calling it. Simply put:
You pass a script to a guy to give out a speech, that guy is actually a public speaker.

Or how about this: When you walk up to a vending machine, you insert a querter, that querter is an argument you passed into an function (vending machine)

An paramators however, are placeholders or variables when you build a function, inside the parathenses () we use:
```
def main(name):
    name = print(f"What up, {name}")
    return name
    
main("Bob")
```

We made a paramator to include a placeholder or a variable named... name, of course! And we called main() and used an argument to include a value named "Bob"
The output printed "What up, Bob" as the passing argument we made.

Think of this way: The engineers designed and made the vending machine to make it accept a quarter `def main(name)`, and when you walk up to the vending machine to insert a querter `main("Bob")` you choose to get an item from the vending machine (Hence why it printed Bobs name).

# Finally, an ending!
Well, you wrote your first python script! Or shall as everyone say, a python program. Next we will be talking about variables and related, data types. I know, it sounds daunting at first, but you will get used to it.

## A homework I got for you (a great repitative lesson).
Start by making your own print statements, try to do this repeatly, try different variations like your name, your favoriate food, your everything, just anything in particular.

### Fun fact!
Did you know that when you use double qoutation marks and enclose it with your own text `"Hello World!"`? In programming, its called a String! A String is a data type that only requires you to use double qoutation marks and enclose it with your own text, that enclosed text could be anything and everything. Happy hacking!
