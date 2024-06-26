import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_key = data["letter"]
data_value = data["code"]

letter_code = {row.letter: row.code for (index, row) in data.iterrows()}
user_input = input("Enter a name: ").upper()
code_words = [letter_code[word] for word in user_input]
# final_output = [code ]
print(code_words)
