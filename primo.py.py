cont=0
a=int(input("Digite el primer número: "))
for i in range (1,a+1):
  
  
  if a%i==0:
    cont=cont+1
    print("encontré un divisor")
    

if(cont>2):
  print("NO es primo")
else:
  print("SI es primo")
