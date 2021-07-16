from data_structure import DataStruct
from gsheet import Gspread
import datetime as dt
from flask import request, render_template


class DataHandler:
    def __init__(self):
        self.data_base = []
        self.data_set = []
        self.sheet = Gspread()
        self.main_data = self.sheet.main_data
        self.response = None

    def structure_data(self):
        self.response = None
        self.data_base = []
        self.sheet.sort_alpha()
        self.sheet.get_records()
        for data in self.main_data:
            date = data['Date']
            month = data['Month']
            name = data['WebinarName']
            reg = data['Region']
            room = data['Room']
            start_time = data['StartTime']
            end_time = data['EndTime']
            year = dt.datetime.strptime(date, "%d/%m/%Y").strftime('%Y')
            data_obj = DataStruct(date, month, name, reg, room, start_time,
                                  end_time, year)
            self.data_base.append(data_obj)

    def home_data(self):
        self.response = render_template(
            "index.html",
        )

    def search_month(self):
        self.structure_data()
        self.response = None
        self.data_set = []
        for data in self.data_base:
            if data.month == str(request.args.get('months')):
                item = {
                    "date": data.date,
                    "month": data.month,
                    "name": data.name,
                    "reg": data.reg,
                    "room": data.room,
                    "start_time": data.start_time,
                    "end_time": data.end_time,
                    "year": data.year
                }
                self.data_set.append(item)
        if not self.data_set:
            self.response = render_template(
                "no_results.html",
                input="month"
            )
        else:
            self.response = render_template(
                "search.html",
                data_set=self.data_set,
                inp="Month",
                year=self.data_set[0]["year"]
            )

    def search_day(self):
        self.structure_data()
        self.response = None
        self.data_set = []
        for data in self.data_base:
            try:
                if data.date == dt.datetime. \
                        fromisoformat(str(request.args.get('date_check'))) \
                        .strftime('%d/%m/%Y'):
                    item = {
                        "date": data.date,
                        "month": data.month,
                        "name": data.name,
                        "reg": data.reg,
                        "room": data.room,
                        "start_time": data.start_time,
                        "end_time": data.end_time
                    }
                    self.data_set.append(item)
            except ValueError:
                self.response = render_template(
                    "error.html"
                )
        if len(self.data_set) == 0:
            self.response = render_template(
                "no_results.html",
                input="date"
            )
        else:
            self.response = render_template(
                "search.html",
                data_set=self.data_set,
                inp="Date",
            )
