
import pandas
import random
import datetime as dt
import smtplib

birthday_data = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_data.set_index(['month', 'day']).to_dict(orient='index')

now = dt.datetime.now()
month = now.month
day = now.day

file_paths = [
              "C:/Users/myvp1/Documents/CV/Birthday_Wisher/letter_templates/letter_1.txt", 
              "C:/Users/myvp1/Documents/CV/Birthday_Wisher/letter_templates/letter_2.txt", 
              "C:/Users/myvp1/Documents/CV/Birthday_Wisher/letter_templates/letter_3.txt"
              ]

if (month, day) in birthday_dict:
    name = birthday_dict[(month, day)]["name"]
    email = birthday_dict[(month, day)]["email"]
    with open(random.choice(file_paths), "r") as file:
        contents = file.read()
        new_content = contents.replace("[NAME]", name)
    
        new_file_path = f"C:/Users/myvp1/Documents/CV/Birthday_Wisher/letter_templates/{name}letter.txt"
        try:
            with open(new_file_path, "w") as new_file:
                new_file.write(new_content)
                
        except FileNotFoundError:
            with open(new_file_path, "a") as new_file:
                new_file.write(new_content)
            
        with open(new_file_path, "r") as data:
            content = data.read()
            
    my_email = "gvic0302@gmail.com"
    password = "nqjhuyepukchgbru"
    
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject: Early Birthday Message \n\n{content}")
        
            
        



