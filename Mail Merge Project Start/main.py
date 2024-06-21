#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
with open("C:/Users/myvp1/Documents/CV/mail_merge_project/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.readlines()
    
with open("C:/Users/myvp1/Documents/CV/mail_merge_project/Mail Merge Project Start/Input/Letters/starting_letter.txt") as data:
    letter_name = data.read()

for name in names:
    
    new_name = name.strip()
    new_letter = letter_name.replace("[name]", new_name)
    output_path = f"C:/Users/myvp1/Documents/CV/mail_merge_project/Mail Merge Project Start/Output/ReadyToSend/starting_letter_{new_name}.txt"
    with open(output_path, "x") as new_file:
        new_file.write(new_letter)
    
    