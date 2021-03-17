from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime


#------ กำหนดฟังก์ชั่น ส่วนที่จะแสดงผลหน้า index.html------------/
def index(request, year, month):
	name = "กรรณธรรม"
	lastname = 'มีธรรมชัย'
	month = month.capitalize()
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)

	#create a calrndar
	cal = HTMLCalendar().formatmonth(
		year,
		 month_number)

	# get ค่าวันเดือนปีปัจจุบัน
	now = datetime.now()
	current_year = now.year

		# ค่าเวลาปัจจุบัน
	time = now.strftime('%I:%M:%S %p')	
	return render(request,
		 'index.html', {
		 'name': name,
		 'lastname':lastname,
		 'year': year,
		 'month':month,
		 'month_number': month_number,
		 'cal': cal,
		 'current_year': current_year,
		 'time': time,
		 })	