### Clue 8: Counting Words ###

#### `wc` ####

Word count (`wc`) is a useful program. You can use it to tell how many lines,
words, and/or characters are in a file:

    wc README.md
    
This will print the number of lines, words, and characters, in that order. If
you just want one of those, you can use `-l`, `-w`, or `-c`. 

#### Finding Clue 9 ####

Check to see if you have the file `/usr/share/dict/words` installed. If not,
run this:

    sudo apt-get install ispell

Now there is a file that acts as a dictionary for spell-checking: 
`/usr/share/dict/words`. Your next clue is the number of words in the 
dictionary.
