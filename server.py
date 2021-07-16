from gsheet import Gspread
from flask import Flask
from data_handling import DataHandler


app = Flask(__name__)
sheet = Gspread()
data_handler = DataHandler()


@app.route('/')
def home():
    data_handler.home_data()
    return data_handler.response


@app.route('/searchmonth')
def search_month():
    data_handler.search_month()
    return data_handler.response


@app.route('/searchdate')
def search_date():
    data_handler.search_day()
    return data_handler.response


if __name__ == "__main__":
    app.run(debug=True)
