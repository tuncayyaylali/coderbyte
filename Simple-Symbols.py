def SimpleSymbols(strParam):

  # code goes here
  for i in range(len(strParam)):
    if strParam[0].isalpha() or strParam[-1].isalpha():
      return "false"
    if strParam[i].isalpha() and (strParam[i-1] not in ["+","="] or strParam[i+1] not in ["+","="]):
      return "false"
  return "true"

# keep this function call here 
print SimpleSymbols(raw_input())
