### Clue 3: Humans vs. Machines ###

#### Binary vs. Text ####

There are two basic types of files: binary and text. Text can be read by both
humans and the computer, and is sometimes referred to as "human-readable". For
example, the file you are reading right now is text.

Binary is a number system that uses only 0 and 1 as digits. For example, 42 is
represented as 101010 in binary. Each digit is called a "bit". Eight bits is
called a "byte". There are 256 possible bytes (2^8). Bytes are a fundamental
unit of measurement in computing (*e.g.* file sizes are in bytes). Computers
use a shorthand for each byte called "hexadecimal" or more briefly "hex". In
hex there are sixteen digits, the usual 0-9 and also A-F. A is equal to 10,
B to 11, *etc*. Sometimes we write a `0x` in front of a hex number to indicate
we are using hex: 42 is `0x2A`.

If you ever look at a file and see a bunch of "garbage", you are probably
looking at a binary file. The content isn't intended for you: it's for the
computer. Binary files are sometimes referred to as "machine-readable".

#### `/bin` ####

One place you can always find binaries on a Linux system is in `/bin`. These
binaries are programs: if you `ls` in `/bin` you may recoginze some of them
(including `ls` itself). This is also a convenient way to get a list of
commands.

If you want to see the garbage view of a binary, you can `cat` or
`less` one of them. You can even `cat cat` or `less less`. On some Linux
systems you can see the hex itself with `hexdump`.

#### `/etc` ####

This directory is named after the latin *et cetera* but is usally pronounced
"et see". There are many text (and some binary) files here that are used to
configure the system. Humans and computers can both read these files to find
out how to configure the system.

For example, look at the `/etc/fstab` file. This describes how the filesystem
is mapped to the hard drive.

#### Find Clue 4 ####

Your hint for clue 4 is the file `/etc/hostname`. This file contains a single
word, which is the name of your computer. This name is your hint. Remember we
can find the next hint by typing

    python next_clue.py [secret number] [next clue number] [hint]
