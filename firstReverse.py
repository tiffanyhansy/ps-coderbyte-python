def FirstReverse(strParam):

  newList = []
  for i in range(len(strParam)):
    newList.append(strParam[len(strParam)-i-1])
    i += 1

  # code goes here
  return ''.join(newList)

# keep this function call here 
print(FirstReverse(input()))