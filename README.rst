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
    
now open excel or libre office calc or a program like that can open and edit .xlsx files and make one in the program directory. this file needs to be empty.
so in libre office do file>saveas>save ass xlsx microsoft office 2007-365 and save it.

Running
----------

now just run main.py by doing
.. code:: sh

    #linux/Windows/MacOs
    cd reportbot2/
    python3 main.py
    
    
