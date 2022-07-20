def TripleDouble(num1,num2):

  # code goes here
  num1 = str(num1)
  num2 = str(num2)

  for i in num1:
    if i*3 in num1 and i*2 in num2:
      return 1
  return 0

# keep this function call here 
print(TripleDouble(input()))
