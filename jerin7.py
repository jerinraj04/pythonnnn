def find gcd(x, y): 
      while(y): 
       x, y = y, x % y 
      return x 
      l = [2, 4, 6, 8, 16] 
num1 = 1[0]
num2 = l[1] 
gcd = find_gcd(num1, num2) 
 for i in range(2, len(l)): 
 gcd = find gcd(gcd, l[i]) 
 print(gcd) 
  
