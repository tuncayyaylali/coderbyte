import sys 

def CoinDeterminer(num):

  # code goes here
  coins=[1,5,7,9,11]
  m = len(coins)
  if num==0:
    return 0
  
  res = sys.maxsize

  for i in range(0,m):
    if (coins[i]<=num):
      sub_res = CoinDeterminer(num-coins[i])
      if (sub_res!=sys.maxsize and sub_res + 1 < res):
        res = sub_res +1

  return res

# keep this function call here 
print CoinDeterminer(raw_input())
