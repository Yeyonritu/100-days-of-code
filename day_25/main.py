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
        
# data = pandas.read_csv("C:/Users/myvp1/Documents/CV/weather_data.csv")
# print(type(data))
# print(data["temp"])

# temp_list = data["temp"].to_list()
# sum = 0
# for i in temp_list:
#     sum += i
    
# average = sum/len(temp_list)
# print(round((average), 2))
# print(data["temp"].mean())
# print(data["temp"].max())

#Get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print((int(monday.temp) * (9/5)) + 32)

#Create a dataframe from scratch

# data_dict = {
#     "student": ["Amy", "James", "John"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

data = pandas.read_csv("C:/Users/myvp1/Documents/CV/day_25/Squirrel_data.csv")
# print(type(data))
gray_data = data["Primary Fur Color"] 
# print(gray_data)
gray_count = 0
black_count = 0
cinnamon_count = 0
for count in gray_data:
    if count == "Gray":
        gray_count+= 1
        
print(gray_count) # Also via using length

for count in gray_data:
    if count == "Black":
        black_count+= 1
        
print(black_count)

for count in gray_data:
    if count == "Cinnamon":
        cinnamon_count+= 1
        
print(cinnamon_count)

data_dict = {
    "Fur Color": ["grey", "black", "cinnamon"],
    "Count": [gray_count, black_count, cinnamon_count]
}

csv_file = pandas.DataFrame(data_dict)
csv_file.to_csv("squirrel_count.csv")