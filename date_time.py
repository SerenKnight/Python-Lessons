from datetime import datetime

date_format = "%d/%m/%Y"

date_today = datetime.strptime(input("What is the date today? "), date_format)
date_birth = datetime.strptime(input("When is your birthday? "), date_format)

delta = date_today - date_birth

print(delta.days)
