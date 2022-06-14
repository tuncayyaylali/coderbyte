def EvenPairs(strParam):

  # code goes here
  for i in range(len(strParam)-1):
    if strParam[i].isnumeric() and strParam[i+1].isnumeric():
      if int(strParam[i]) % 2 == 0 and int(strParam[i+1]) % 2 == 0:
        return "true"
  for i in range(len(strParam)-2): 
    if strParam[i].isnumeric() and strParam[i+1:i+3].isnumeric():
      if int(strParam[i]) % 2 == 0 and int(strParam[i+1:i+3]) % 2 == 0:
        return "true"
      elif  int(strParam[i:i+2]) % 2 == 0 and int(strParam[i+2]) % 2 == 0:
        return "true"    
  return "false"

# keep this function call here 
