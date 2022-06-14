def FindIntersection(strArr):

  # code goes here
  strArr_1 = set(strArr[0].split(", "))
  strArr_2 = set(strArr[1].split(", "))
  sonuc = strArr_1.intersection(strArr_2)
  liste =[]
  for i in sonuc:
    liste.append(int(i))
  liste.sort()
  return (",".join(map(str, liste)))
# keep this function call here 
print FindIntersection(raw_input())
