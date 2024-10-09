import smtplib
import datetime as dt

my_email = "zack03965@gmail.com"
password = "aobx neto bpmq pyii"

with open("quotes.txt") as quotes:
    quote_list = quotes.readlines()
    clean_quote_list = [quote.strip() for quote in quote_list]


with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    # Add security encryption
    connection.starttls()

    connection.login(user=my_email,password=password)
    # connection.sendmail(
    #     from_addr=my_email,
    #     to_addrs="zack03965@yahoo.com",
    #     msg="Subject:You are the best\n\n"
    #         "This is the body of my email"
    # )


#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# if year == 2024:
#     print(day_of_week)
#
# date_of_birth = dt.datetime(year=2000,month=12,day=25)
# print(date_of_birth)