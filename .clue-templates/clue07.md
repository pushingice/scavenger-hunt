### Clue 7: Make Me a Sandwhich ###

https://xkcd.com/149/

#### `sudo` ####

Linux has the concept of a `root` user, which is similar to the administrator
user on Windows. This user is sometimes called the super user. If you want to
do something as the super user, but stay logged in as yourself, there is a 
command for that: `sudo`. It stands for "super-user do".

#### Installing Software ####

Sometimes you need a new program. To install software on some versions of Linux
(Ubuntu and Debian), you use the command `apt-get`. On other versions (Fedora,
CentOS) you use the command `yum`. Let's install a text editing program
called `vim`.

    apt-get install vim
    
You should get an error message asking if you are root. This means you don't
have the ability to install software. Instead, try

    sudo apt-get install vim
    
Now we have the ability to edit files. Try

    vim README.md
    
from the `scavenger-hunt` directory. Some of the commands for `vim` are a little
strange. For now, just type `:q!` to quit.


#### Finding Clue 8 ####

The hint is the name of the first folder listed in `/sys/kernel/debug`.

#### Help. I can't sudo ####

Depending on the system you are using, you may not have permission to use `sudo`.
In this case you can use the hint `denied`.

