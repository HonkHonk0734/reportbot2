Reportbot2
==========

A bot that allow members to report bots in discord and saves them to a spreadsheet.


Installing
----------

**Python 3.8 or higher is required**

To install the discord library, the openpyxl library and datetime library run:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U discord.py openpyxl datetime

    # Windows
    py -3 -m pip install -U discord.py openpyxl datetime

now that we have installed the right libraries we need to install git to clone this repo:

.. code:: sh

    # Debain/Ubuntu
    sudo apt install git

    # Arch (pacman)
    pacman -S git
    
    # MacOs
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" 
    brew install git
    
    #windows
    https://git-scm.com/download/win
    
now that we have installed git we can clone the repo
    
.. code:: sh
    
    git clone https://github.com/HonkHonk0734/reportbot2.git
    
Configuring
----------
first go to Discord.com/developers and create an new application then go to it then go to bot>create bot. once you have done that
go to the folder that you created by git cloning. as you see there is an file named main.py open that with your favorite text editor.
on line 7 you wil see Token = '' between those you need to paste your discord bot token. so got to discord.com/developers go to your application and click on bot now under token you see copy and reveal click on copy and paste it between Token = '<here>'. now go to your discord server where you want the bot be and make a staff channel for reports and turn on developer mode in settings and right-click on the reports channel and copy channel id and paste it on line 61 between 
channel = client.get_channel(<here>) exaple = channel = client.get_channel(858635125184659477) and that is all. just run the bot now


Running
----------

now just run main.py by doing:

.. code:: sh

    #linux/Windows/MacOs
    cd reportbot2/
    python3 main.py
    
    
