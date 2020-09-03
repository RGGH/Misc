import math


#modu = 50
#ans = 99%modu
#print(ans)

# double modu and subtract 1 to get start number
# to get modulus 1007 
# answer you want = 1007
# take required answer,
# add 1
# multiply by 2
# so 
rans = 10000000007
print("required answer is ",rans)

w = (rans + 1)*2
v = (w/2)+1

print(f"W= {w} and V= {v}")
ans2 = w%v

print(f"w%v={ans2}")
# 1007+1 x 2 = 2016
# 2016/2 + 1 = 1009

#ans2=2016%1009
print(math.floor(ans2))
