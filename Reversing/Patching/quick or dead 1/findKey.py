from pythonds.basic.stack import Stack
x=0x9
def fib(x):
   if(x>1):
      y = x-1
      z=fib(y)
      a = x-2
      b=fib(a)
      return z+b
   else:
      return x

def iterFib(x):
   count = 0
   s=Stack()
   s.push(x)
   while(s.size() > 0):
      a = s.pop()
      if a>1:
         s.push(a-1)
         s.push(a-2)
      elif a == 1:
          count += 1
   return count
w=iterFib(x)
print(w)
