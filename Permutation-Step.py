def PermutationStep(num):
  from itertools import permutations
  perm = permutations(str(num))
  result=[]
  for i in perm:
    result.append(int(''.join(list(i))))
  final_list = []
  for i in result:
    if i > num:
      final_list.append(i)
  if len(final_list) == 0:
    return -1
  else:
    return min(final_list)

# keep this function call here 
print(PermutationStep(input()))
