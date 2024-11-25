from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
import calendar
from dateutil.relativedelta import relativedelta
import os

app = Flask(__name__)

def get_month_letter(month_num, position):
    months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE',
              'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
    month_name = months[month_num - 1]
    return month_name[position] if position < len(month_name) else ' '

def get_week_number(date):
    return date.isocalendar()[1]

def generate_calendar_data(start_date):
    calendar.setfirstweekday(calendar.MONDAY)
    data = []
    
    # Generate 12 months of data starting from start_date
    current_date = start_date
    for _ in range(12):
        month_data = {
            'month': current_date.month,
            'year': current_date.year,
            'weeks': [],
            'month_letters': [
                get_month_letter(current_date.month, 0),
                get_month_letter(current_date.month, 1),
                get_month_letter(current_date.month, 2)
            ]
        }
        
        # Get the calendar for current month
        cal = calendar.monthcalendar(current_date.year, current_date.month)
        
        # Get the last day of previous month
        last_month = current_date - relativedelta(months=1)
        _, last_day_prev = calendar.monthrange(last_month.year, last_month.month)
        
        for week in cal:
            week_dates = []
            first_day = None
            for day in week:
                if day != 0:
                    if first_day is None:
                        first_day = datetime(current_date.year, current_date.month, day)
                week_dates.append(str(day) if day != 0 else '')
                
            if first_day:
                week_num = get_week_number(first_day)
            else:
                continue
                
            month_data['weeks'].append({
                'week_num': week_num,
                'dates': week_dates
            })
            
        data.append(month_data)
        current_date += relativedelta(months=1)
        
    return data

@app.route('/')
def index():
    # Default to next January
    next_year = datetime.now().year + 1 if datetime.now().month == 12 else datetime.now().year
    default_date = datetime(next_year, 1, 1)
    return render_template('index.html', default_date=default_date.strftime('%Y-%m'))

@app.route('/get_calendar')
def get_calendar():
    date_str = request.args.get('start_date', '')
    try:
        start_date = datetime.strptime(date_str, '%Y-%m')
    except ValueError:
        next_year = datetime.now().year + 1 if datetime.now().month == 12 else datetime.now().year
        start_date = datetime(next_year, 1, 1)
    
    calendar_data = generate_calendar_data(start_date)
    return jsonify(calendar_data)

if __name__ == '__main__':
    # Use production config when deployed
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
