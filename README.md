# Focused

The project aims to help people get more productive using a BOT that will track your progress, using pomodoro units (customizable), giving to the user hints & tips on how getting on track with their own objectives.


## TO-DO 
* [ ] To-Do (MVP)
* [ ] Reminder
* [ ] Overview
* [ ] Hints & Tips
* [ ] Pomodoro Defaults
* [ ] Pomodoro Custom 
* [ ] Dashboard - Web


## Technologies

- Python 3.7+
- Discord Py
- PostgreSQL
- Redis para cache
- Elixir/Ecto - API


## Getting Started

At this point the project still only a Discord BOT so you will need to use pip to install the required libs using the command:

```
pip install -r requirements.txt
```

### Prerequisites

Yet the project is growing, only [Discord.py](https://github.com/Rapptz/discord.py) is used


### Installing

To install a development environment at your machine, use virtualenv from python, to create a isolated env to not polute your global installation:

```
virtualenv --python=path/to_your/python_binary venv
```
do not forget before using the terminal access the source, inside the directory which has the virtual environment, activate it

```
source venv/bin/activate
```

then install

```
pip install -r requirements.txt
```

## Running the tests

The project does not have tests yet 

### coding style

We do follow PEP-8

