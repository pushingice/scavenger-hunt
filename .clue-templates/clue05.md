### Clue 5: Is There an Echo in Here? ###

#### `echo` ####

Sometimes we want the computer to repeat back the results of some command. Try

    echo hello
    
The most basic thing `echo` will do is repeat back whatever you type. 

#### Redirect ####
You can use this to create a small file, or start a new file:

    echo My bologna has a first name > oscar.txt
    
If you look in oscar.txt you will see exactly what you typed. The `>` symbol
used here is called a redirect. It redirects whatever would normally be printed
to the screen to a file. You can try it with other commands:

    ls > my_directory.txt
    
You can also use `echo` to display what are called environment variables

    echo $PATH
    echo $HOME

The `HOME` variable should make sense at this point. 

#### Find Clue 6 ####

The `PATH` variable tells the computer where programs are. Each path that could 
contain a program is placed between colons. Your hint for the next clue is the 
first path listed in your `PATH`.
