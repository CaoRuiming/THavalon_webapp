# THavalon Web App

THavalon is Brown University Tech House's custom rules for The Resistance: Avalon. The original repo can be found [here](https://github.com/aquadrizzt/THavalon). This project is meant to convert the game to a web application, allowing players to make games and view their information online. 

## Technology Used
* Backend
  * Python 2.7.13
  * [django](https://www.djangoproject.com/)
* Frontend
  * HTML/CSS
  * JavaScript
  * [django templating language](https://docs.djangoproject.com/en/1.11/topics/templates/)
* Database
  * MySQL

## TODO List
* Set up full stack communication
  * Create Server
    * Ensure can load basic webpage

* Set up database
  * Need to be able to store the following:
    * Role Info
      * Name
      * Flavor text
      * What is seen (i.e., knows all evil, knows lover exactly, etc.)
      * Abilities
    * Abilities
      * Name 
      * Description
      * Ex: Reversal. Store in separate table since multiple roles can may be able to have same ability
    * Games
      * Game id
      * Status (in lobby, active, ended)
      * Lobby name
      * Lobby password (optional)
      * For each player
        * Player name
        * Player password
        * Role Text (what user would have seen in text file in original version)
        * If created game (for starting game and removing players from lobby)
      * Start time
      * End time
      * Other info tbd (such as mission results, would need to be manually entered at game end)
    
* Create home page
  * Ability to start new lobbies
  * Ability to view active games and open lobbies
    * Should be able to search/filter by game name
    * Should be able to filter by status (show in lobby only or active games only)
    * Should show start time and number of players
  * Ability to join open lobby
  
* Create lobby
  * From home page, ability to create new lobby
  * Lobby must have name and optional password

* Join lobby
  * From lobby browser on phone, ability to join a lobby
  * If new player, must enter:
    * username (must not be used)
    * password (if we do that option)
    * confirm password (if we do that option)
  * If returning player
    * username (must exist in game)
    * password
  
* In lobby
  * Ability to view lobby name
  * Ability to view other players
  * Before starting game
    * If game creator
      * Ability to remove players
      * Ability to start game (should this be open to everyone?)
  * Once game started
    * Ability to end game and optionally enter game data (should this be game creator only?)

## Dev Environment
An overview of what I did to set up my dev environment. I am using Bash for Windows 10, it should be similar for Mac and Linux. If using Windows, I would strongly recommend installing [bash for windows 10](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide).

1. Install python2.7
  * [Mac](https://www.python.org/downloads/release/python-2713/)
  * [Linux/Bash for Windows](https://tecadmin.net/install-python-2-7-on-ubuntu-and-linuxmint/)
2. [Optional] Set up virtual environment
  * Recommended for running django, so can install project specific packages
  * [Django virtualenv instructions](https://docs.djangoproject.com/en/1.11/intro/contributing/#getting-a-copy-of-django-s-development-version) (Scroll down a bit)
  * Mac/Linux: `python2.7 -m venv ~/.virtualenvs/djangodev`
  * Bash for Windows: `pip install virtualenv` then `virtualenv -p python2.7 ~/.virtualenvs/djangodev`
  * To run the virtual environment, run `source ~/.virtualenvs/djangodev/bin/activate`
3. Install django
  * In the virtual environment, `pip install Django`
  * Bash for Windows: You may need to manually install pip in the virtual environment first. To do so, download get-pip.py from [here](https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py) and run `python /path/to/get-pip.py`
  * To confirm django is installed, run `python -m django --version`. If the version is printed (currently 1.11.2), the install is complete
4. Install MySQL
  * Mac: ???
  * Bash for Windows: 
    * `sudo apt-get install mysql-client mysql-server-core-5.5 mysql-server libmysqlclient-dev`
    * `pip install mysqlclient` (see below for instructions if errors occur, may need sudo)
    * `sudo service mysql start`
  * All: 
    * `mysql -u root -p` then password you created when installing mysql
    * So we all have the same user, run `GRANT ALL PRIVILEGES ON *.* TO 'colgrevance'@'localhost' IDENTIFIED BY 'thavalon';` in the SQL terminal. This will create the user colgrevance with password thavalon for everyone. This is a huge security risk normally, but we need a user for the settings file, and it's easier to upload a settings file than ignore it. 
    * `exit` to quit mysql
    * `mysql -u colgrevance -p` then thavalon for password
    * `CREATE TABLE thavalon CHARACTER SET utf8;` then `USE thavalon;` to make the database
    * `exit` to quit mysql
  * If errors occur when trying to install mysqlclient (NOTE: These may not fix anything, are left over from using python 3.6. Downgrade to python 2.7 fixed mysql, unsure if these do anything with 2.7):
    * Check out [this link](https://askubuntu.com/questions/428198/getting-installing-gcc-g-4-9-on-ubuntu). It has some instructions on upgrading to gcc 4.9 so django will be able to install mysqlclient. You will also need to run the following:
      * `cd /usr/bin`, `sudo rm x86_64-linux-gnu-gcc`, `sudo ln -s gcc-4.9 x86_64-linux-gnu-gcc`
    * 
    * Try `sudo apt-get install python-dev python3-dev`
    * If above don't work, also try `sudo apt-get install libxml2-dev libxslt1-dev libpq-dev `
    * Ok so I'm still getting an error, am probably going to try downgrading to python2.7 and starting from scratch at some point in the next few days

