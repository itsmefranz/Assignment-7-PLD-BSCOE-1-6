def getInputSentence():
    sentence= (input("Please enter your sentence: "))
    return sentence

def isVowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']

def isConso(ch):
    return ch.upper() in ['B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'S', 'T', 'V', 'X', 'Z', 'H', 'R', 'W', 'Y']
 
# Returns count of vowels in str
def countVowels(str):
    count = 0
    for i in range(len(str)):
 
        # Check for vowel
        if isVowel(str[i]):
            count += 1
    return count   

def countConso(str):
    count = 0
    for i in range(len(str)):
 
        # Check for vowel
        if isConso(str[i]):
            count += 1
    return count 

user_input= getInputSentence()
vowels_num= countVowels(user_input)
conso_num= countConso(user_input)


print(f"The number of vowels in this sentence is {vowels_num}.")
print(f"The number of consonants in this sentence is {conso_num}.")
