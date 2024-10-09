import smtplib

my_email = "zack03965@gmail.com"
password = "aobx neto bpmq pyii"

with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    # Add security encryption
    connection.starttls()

    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="zack03965@yahoo.com",
        msg="Subject:You are the best\n\n"
            "This is the body of my email"
    )
