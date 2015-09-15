### Clue 2: The Lay of the Land ###

#### `pwd` ####

What if we get lost and need to know where we are? Just type `pwd` (print
working directory). This should print something like this:

    /home/user/scavenger-hunt/clues/123456

We are five folders deep, in a folder named `123456`.

#### `cd` ####

Change directory is extremely useful, but it can also be confusing. We
already saw how you can move up one directory (`cd ..`) or down one directory
(`cd [dir]`). You can move up or down any number of directories in a single
command like this (won't actually work here):

    cd ../../../one/two/

You would navigate up 3 directories relative to where you are, then down
into directory one and then two. This is what's known as a relative path: it
depends on where you start where you will end up. The other way to change
directories is with absolute paths. Try this:

    cd /

Look around and see what's there. This is known as the root path. You can
explore the entire file system from here, using just `ls` and `cd`.

#### Find Clue 3 ####

To find the next clue, go to the `/usr` directory and count the number of
subdirectories. This is a hint to your next clue location. Go to the
`scavenger-hunt` directory, and type

    python next_clue.py [secret number] [next clue number] [hint]

So, if there were 5 directories, we would type

    python next_clue.py 42 3 5

since our secret number is 42, we want to find clue 3, and our hint is 5.
The location of our next clue should be printed. If you get the hint wrong,
an incorrect clue will be printed. This is an example of what is known as GIGO
(garbage-in, garbage-out). Helpful tip: you can open more than one terminal
window, or more than one tab in your current window with `CTRL-SHIFT-T`.

#### `less` ####

Less is a program that allows you to view files in a terminal. Unlike `cat`,
you can scroll through the file using up, down, page up, *etc*. After you
navigate to clue 3, do `less clue`. The name Less is a play on More, a similar
program. More is older and is so named because you could press enter to
see more text.
