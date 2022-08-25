from flask import Blueprint, render_template, redirect, url_for
from c_meet.models.schedules import Schedule
from flask_login import (current_user, login_required)
import datetime


schedule = Blueprint('schedule', __name__)

@schedule.route('/')
@login_required
def show_today_calender() :
    today = datetime.date.today()
    year = today.year
    month = today.month
    return redirect(url_for('schedule.show_calender', date= str(year) +"-" + str(month)))

@schedule.route('/<date>')
@login_required
def show_calender(date) :
    year, month = date.split('-')
    year = int(year)
    month = int(month)
    
    prev_month = month-1
    prev_year = year
    if(prev_month == 0):
        prev_month = 12
        prev_year = year - 1

    next_month =  month + 1   
    next_year = year  
    if next_month == 13:
        next_month = 1
        next_year = year + 1
    max_day_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    max_day = max_day_list[month-1]
    if month == 2:
        if int(year) %400 == 0  or (int(year) % 100 != 0 and int(year) % 4 == 0):
            max_day = max_day + 1
       

    return render_template('schedule.html',year = str(year),month = str(month),max_day = max_day, prev = str(prev_year) +"-" + str (prev_month), next = str(next_year) +"-" + str(next_month) )
