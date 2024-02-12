# COMP0034 Coursework 1 2023/24
COMP0034 Coursework 1 starter repository

## Link to Repository
https://github.com/ucl-comp0035/comp0034-cw1i-MakoaJerboa

## Usage
### Create Virtual Enviroment
In the terminal, type "py -m venv .venv" for Windows or "python3 -m venv .venv" for Unix/macOS (without the quotes)

### Activate Virtual Environment
If your IDE does not prompt you to activate the virtual environment, type ".\env\Scripts\activate" into the terminal for Windows or "source env/bin/activate" for Unix/macOS (without the quotes). Then close the terminal and open a new one, the virtual environment should now be active.

### Installing Requirements
In the terminal type "pip install -r requirements.txt"

### Run
The code can be run from the terminal by typing "flask --app coursework1 run --debug" without quotes.

### Function
Upon loading the webpage, you'll be on the landing page, from here you can click the links to view data on 2011 or 2021. You can also view data about a specific area by navigating to /yr2011/area name or /yr2021/area name . For example, to view data on Brent in the year 2011, you would navigate to /yr2011/Brent . For areas with spaces in their name also function the same way.