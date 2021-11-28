def getInputSentence():
    sentence= (input("Please enter your sentence: "))
    return sentence

def isVowel(user_input):
    return user_input.upper() in ['A', 'E', 'I', 'O', 'U']

def isConso(user_input):
    return user_input.upper() in ['B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'S', 'T', 'V', 'X', 'Z', 'H', 'R', 'W', 'Y']
 

def countVowels(str):
    count = 0
    for i in range(len(str)):
        if isVowel(str[i]):
            count += 1
    return count   

def countConso(str):
    count = 0
    for i in range(len(str)):
        if isConso(str[i]):
            count += 1
    return count 

def countWord():
        word_list= str.split(user_input)
        number_of_words= len(word_list)
        return number_of_words

user_input= getInputSentence()
vowels_num= countVowels(user_input)
conso_num= countConso(user_input)
word_count= countWord()

print(f"The number of vowels in this sentence is {vowels_num}.")
print(f"The number of consonants in this sentence is {conso_num}.")
print(f"The number of words in this sentence is {word_count}.")