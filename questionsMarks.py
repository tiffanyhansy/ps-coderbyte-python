def QuestionsMarks(strParam):
  question_marks = 0
  last_number = 0
  found = False #적어도 하나의 합이 10이 되는 숫자 쌍이 존재? 
  
  for c in strParam:
    
    #문자열 전체가 정수일 때 
    if c.isdigit(): 
      n = int(c)  #숫자를 정수로 변환 
      if last_number + n == 10:
        found = True
        if question_marks != 3:
          return False
        
      question_marks = 0  #숫자 사이 ? 수를 0으로 초기화 
      last_number = n #현재 숫자를 이전 숫자로 변경 
      
    #문자가 ? 일 때 ? 개수 카운터 증가 
    elif c == '?': 
      question_marks += 1
      
  #found_any를 소문자로 변환하여 반환 (True -> true)
  return str(found).lower()

# keep this function call here 
print(QuestionsMarks(input()))