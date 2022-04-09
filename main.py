import pandas

# Todo 1:Creating the Dictionary of the Phonetic alphabets

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dic = {row.letter: row.code for (index, row) in data.iterrows()}
# print(data_dic)

# Todo 2:User Interaction
letter = input("Enter the Word to get it's  phonetics : ")
letter = letter.upper()

words = list(letter)
phonetic_list = [data_dic[n] for n in words]
print(phonetic_list)
