#How to send emails using python
# import smtplib

# my_email = "gvic0302@gmail.com"
# password = "nqjhuyepukchgbru"

# with smtplib.SMTP("smtp.gmail.com", 587) as connection: #Always add Port Number 587 for gmail
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="myvp18@gmail.com", msg="Subject: Attaininng Heaven\n\nDo you believe in heaven")


# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()

# date_of_birth = dt.datetime(year=2003, month=11, day=18)
import datetime as dt
import smtplib
import random

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 6:
    
    try:
        with open("quotes.txt", "r") as file:
            contents = file.readlines()
            mail_to_send = random.choice(contents)
        
        print(mail_to_send)
        my_email = "gvic0302@gmail.com"
        password = "nqjhuyepukchgbru"
        
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="nabilibrahim49@gmail.com", msg=f"Subject: FMonday Motivation\n\n{mail_to_send}")
            
    except FileNotFoundError:
        print("Error File Not found")
        
else:
    print("")