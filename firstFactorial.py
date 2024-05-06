def FirstFactorial(num):

  #a의 범위가 1부터 num까지일 때 
  for a in range(1, num):
    num *= a
    a += 1
    
  # code goes here
  return num

# keep this function call here 
print(FirstFactorial(input()))