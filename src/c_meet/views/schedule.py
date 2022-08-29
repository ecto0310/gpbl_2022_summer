from flask import Blueprint, render_template, redirect, url_for,flash
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
    today = datetime.date.today()
    day = today.day
    today_month = today.month
    today_year  = today.year
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

    schedule_list = [0] *31
    for user_schedule in current_user.schedules:
        user_schedule.date = str(user_schedule.date)
        user_schedule_year ,user_schedule_month , user_schedule_date = user_schedule.date.split('-')
        if int(user_schedule_year) != year or int (user_schedule_month) != month:
            continue
        schedule_list[int(user_schedule_date)-1] = 1  

    return render_template('schedule.html',today_month  = int(today_month),today_year = str(today_year),day = int(day), year = str(year), month = int(month),max_day = max_day, now = str(year) + "-" + str(month),prev = str(prev_year) +"-" + str(prev_month), next = str(next_year) +"-" + str(next_month) ,schedule_list = schedule_list)

@schedule.route('/<year_month>/<day>')
@login_required
def user_schedule(year_month ,day) :
    today = datetime.date.today()
    today_day = today.day
    today_month = today.month
    today_year  = today.year
    year, month = year_month.split('-')
    year = int(year)
    month = int(month)
    today_year = int(today_year)
    today_month = int(today_month)
    today_day = int(today_day)
    day = int(day)
    if ( year == today_year and month == today_month ) and today_day >day :
        flash('その日程は入力できません')
        return redirect(url_for('schedule.show_calender',date = year_month))
    if  year < today_year :
        flash('その日程は入力できません','error')
        return redirect(url_for('schedule.show_calender',date = year_month))
    if  year == today_year and month < today_month  :
        flash('その日程は入力できません','error')
        return redirect(url_for('schedule.show_calender',date = year_month))          
    schedule = Schedule(user_id = current_user.id ,date = str(year_month) + "-" + str(day)) 
    Schedule.create(schedule)
    flash("予定を入力しました")
    return redirect(url_for('schedule.show_calender',date = year_month))

@schedule.route('/<month>/<date>/d')
@login_required
def delete_user_schedule(month,date) :
    schedule = Schedule(user_id = current_user.id ,date = str(month) + "-" + str(date))
    Schedule.delete(schedule)
    flash('予定を削除しました')
    return redirect(url_for('schedule.show_calender',date = month))





