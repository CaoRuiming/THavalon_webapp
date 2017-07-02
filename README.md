# THavalon Web App

THavalon is Brown University Tech House's custom rules for The Resistance: Avalon. The original repo can be found [here](https://github.com/aquadrizzt/THavalon). This project is meant to convert the game to a web application, allowing players to make games and view their information online. 

## Technology Used
* Backend
  * Python 3.6
  * Most likely [django](https://www.djangoproject.com/)
* Frontend
  * If using django, then [django templating language](https://docs.djangoproject.com/en/1.11/topics/templates/)
* Database
  * Probably mongoDB

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
      * Start time
      * End time
      * Other info tbd (such as mission results, would need to be manually entered at game end)
    
* Create home page
  * Ability to start new lobbies
  * Ability to view active games and open lobbies
  * Ability to join open lobby
  
* Create lobby

* Join lobby

* Start game from lobby

## Dev Environment
An overview of what I did to set up my dev environment. I am using Bash for Windows 10, it should be similar for Mac and Linux. If using Windows, I would strongly recommend installing [bash for windows 10](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide).

1. Install python3.6
  * [Mac](https://www.python.org/downloads/release/python-361/)
  * [Linux/Bash for Windows](https://askubuntu.com/questions/865554/how-do-i-install-python-3-6-using-apt-get)
2. [Optional] Set up virtual environment
  * Recommended for running django, so can install project specific packages
  * [Django virtualenv instructions](https://docs.djangoproject.com/en/1.11/intro/contributing/#getting-a-copy-of-django-s-development-version) (Scroll down a bit)
  * Mac/Linux: `python3.6 -m venv ~/.virtualenvs/djangodev`
  * Bash for Windows: `pip3 install virtualenv` then `virtualenv -p python3.6 ~/.virtualenvs/djangodev`
  * To run the virtual environment, run `source ~/.virtualenvs/djangodev/bin/activate`
3. Install django
  * In the virtual environment, `pip3 install Django`
  * Bash for Windows: You may need to manually install pip in the virtual environment first. To do so, download get-pip.py from [here](https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py) and run `python3.6 /path/to/get-pip.py`
  * To confirm django is installed, run `python -m django --version`. If the version is printed (currently 1.11.2), the install is complete
4. Install mongoDB
  * Coming soon
