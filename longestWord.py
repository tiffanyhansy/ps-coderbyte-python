def LongestWord(sen):

  max = 0
  for word in sen.split():
    if(len(word) > max and word.isalpha()):
      max = len(word)
      sen = word

  # code goes here
  return sen

# keep this function call here 
print(LongestWord(input()))