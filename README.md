# scavenger-hunt #

This is a scavenger hunt to learn Linux commands. Our goal is to find all
the clues and learn how to use basic Linux commands in the process.

## Setup ##

If you are using a new Linux install or Live CD, you may need to install
Git first (`sudo apt-get install git` on Ubuntu). Open a terminal and type:

    git clone https://github.com/pushingice/scavenger-hunt.git
    cd scavenger-hunt

First, choose a secret number with at least 4 digits to share with your team,
or keep to yourself if you are working alone. Don't forget it! The secret
number makes your clues unique, so other teams can't look over your shoulder.
Then type:

    python generate_clues.py [secret number]

Any time we enclose something in square brackets, you need to replace it
with an actual value (called an argument). For example, to get started I
might type:

    python generate_clues.py 42

This will create a subdirectory called `clues`. Be sure to keep this file
(called the README) open in a separate viewer.

## Reference ##

If you want to learn more about Linux when you are finished, or need a reference
during the hunt, go here: http://www.tldp.org/LDP/intro-linux/html/index.html.

### Clue 1: The Hunt Begins ###

#### `man` ####

The first command we are going to learn is `man`, which is short for manual.
Typing `man [command]` will give you a help page (usually called a manpage)
for most commands.

#### `ls` ####

The next command we need to learn is `ls` (list). Type `man ls` and read the
description. Press `q` to exit. Then type `ls` and you should see something
like this:

    APPENDIX.md clues generate_clues.py LICENSE.md next_clue.py README.md

Items which are blue are directories and everything else is a file. Any time
you need to know which files and directories are available, type `ls`.

#### `cd` ####

We need a couple more tools before we can start clue hunting. To change to
another directory we use `cd` (change directory). You may notice that
`man cd` doesn't work. Sometimes there is no manpage for a command. In that
case google is your friend. Changing directories is pretty simple:

    cd clues

This puts us in the clues directory. To go up a directory, we can do this:

    cd ..

If you ever get lost, just do

    cd ~/scavenger-hunt

to return home. If you `cd` to the `clues` directory and do an `ls`, you
will notice that there are a lot of clue directories. Most of them contain
fake clues. Throughout our hunt we will be looking for real clues. Using
`cd`, navigate to `clues/12345` and type `ls`. You should see a single
file named `clue`.

#### `cat` ####

Finally we need to be able to look at our clues. First read the manpage for
`cat`, then do:

    cat clue

This should list the clue in your terminal. From now on, everything we need
will be contained in these clue files. It's a good idea to keep track of
all the clue folders (like `123456`) on a piece of paper. You can also do
things like copy all the clue files to your home folder, or cut and paste
the clue text into another file.
