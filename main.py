# This function returns the entirety of "Dracula" as a string
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

#Store the text in a variable
draculaText = readBook()
#draculaText = "Hello there I am adding words to this so I can have some words word word wordity word"

#Split the text into individual words, and save as a new variable
words = draculaText.split()

#initialize the wordList Dictionary
wordList = {}

#iterate through the words variable, adding each new instance of a word to the wordList Dictionary
for word in words:
  #Set each word to be lowercase before checking if it is in the wordList
  word = word.lower()
  #if the word is not in wordList yet, add it to the dictionary with a value of 1
  if word not in wordList:
    wordList[word] = 1
  #if the word is in wordList, increase value by 1
  else:
    wordList[word] += 1

#Create default variables for the data we need to extract
mostFrequentWord = ""
largestValue = 0
fourLetter = []
fiveHundredClub = {}

#iterate through wordList to find most used word
for key, value in wordList.items():
  #check for most used word
  if value > largestValue:
    mostFrequentWord = key
    largestValue = value
    
  #check for 4 letter words
  if len(key) == 4:
    if key not in fourLetter:
      fourLetter.append(key)

  #check if the value is 500+
  if value >= 500:
    fiveHundredClub[key] = value
    


#Print results
print("=== Results ===")
print()
print(f"'{mostFrequentWord}' is the word that appears the most throughout the text, a total of {largestValue} times.")
print()
print(f"There are {len(fourLetter)} words that are four letters long")
print()
print("I noticed that these words show up 500 or more times:")
#for loop to print all words that appear 500+ times
for key, value in fiveHundredClub.items():
  print(f"{key} - {value}")
