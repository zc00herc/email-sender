import smtplib
import datetime as dt
import random
import pandas as pd

now = dt.datetime.now()
day_of_week = now.weekday()
MY_EMAIL = "email@gmail.com"
MY_PASSWORD = "string"

with open("quotes.txt") as quotes:
    quote_list = quotes.readlines()
    clean_quote_list = [quote.strip() for quote in quote_list]

random_quote = random.choice(clean_quote_list)

birthdays = pd.read_csv("birthdays.csv")
bday_dict = birthdays.to_dict(orient="records")
for birthday in bday_dict:
    date = dt.datetime(year=birthday["year"],month=birthday["month"],day=birthday["day"])
    if now.month == birthday["month"] and now.day == birthday["day"]:
        with open("letter.txt") as letter:
            letter_body = letter.read()
            modified_letter = letter_body.replace("[NAME]", birthday["name"])
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            # Add security encryption
            connection.starttls()

            connection.login(user=MY_EMAIL,password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday["email"],
                msg="Subject:Happy Birthday\n\n"
                    f"{modified_letter}\n\n"
                    f"{random_quote}"
            )
