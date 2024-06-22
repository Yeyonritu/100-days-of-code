# with open("C:/Users/myvp1/Documents/CV/weather_data.csv") as file:
#     data = file.readlines()
    
import csv
import pandas

# with open("C:/Users/myvp1/Documents/CV/weather_data.csv") as file:
#     data = csv.reader(file)
#     learn_work = []
#     temperatures = []
#     for i in data:
#         print(i)
#         if i[1] != "temp":
#             temperatures.append(int(i[1]))
    
#     print(temperatures)
# print(learn_work)
        
data = pandas.read_csv("C:/Users/myvp1/Documents/CV/weather_data.csv")
print(data)
print(data["temp"])

