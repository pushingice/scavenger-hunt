### Clue 10: Pipes ###

#### Piping Information ####

Many commands will print their output. This is called "standard output" or
`stdout`. We saw earlier how you can redirect standard output to a file (`>`).
There is also standard input (`<`). For example, `cat < README.md` is the same
as `cat README.md`. But standard input and output can be chained together using
pipe (`|`). For example, you can count the number of files and folders in a
directory like this:

    ls | wc -w
    
This works by taking the output of `ls` and using it as the input to `wc`.
Another example:

    grep ^sand /usr/share/dict/words | wc -l

will print the number of words that start with "sand". The carat `^` symbol
is a regular expression that means "starts with". You can also use `$` for
"ends with".

#### Sort ####

Sometimes you need to sort data alphabetically. You'll notice that the
dictionary file is already sorted. You can create your own unsorted copy like
this:

    sort -R /usr/share/dict/words > random_words
    
Now you can `sort random_words` to get back to alphabetical order, or 
`sort -r random_words` for reverse alphabetical order. 

#### Finding Clue 11 ####

Use the command `ls -la /usr` to get a big list of files. The 5th column in 
that list is the size of the file in bytes. Find the sort command to print the
list of files with the largest file first, and then the rest indescending order.
Your hint is the options you had to use. You'll need to use double quotes for
your hint. For example, if your command was `sort -a -b -c`, your hint would
be

    python next_clue.py [secret] 11 "-a -b -c"
    


