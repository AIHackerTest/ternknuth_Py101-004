#!/usr/bin/env python3
import ch3_mod
from flask import Flask, render_template, request
app = Flask(__name__)
list_history_record = []

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def city_weather():
    button_value = request.form['button']
    if button_value == "帮助":
        return render_template('help.html', help_value = ch3_mod.help_message() )
    elif button_value == "历史":
        return render_template('history.html', history_value = ch3_mod.history_message(list_history_record) )
    elif button_value == "查询":
        city_name = request.form['city_name']
        result = ch3_mod.get_city_weather(city_name)
        if len(result) > 1:
            list_history_record.append(result )
        else:
            pass
        return render_template('city.html', city_value = result)

        

if __name__ == '__main__':
    app.run(debug=True)

