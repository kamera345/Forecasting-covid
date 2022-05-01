
# def subsets(str):
#     output = []  
#     n = len(str)
#     for i in range(n):    
#         for j in range(i,n):  
#             output.append(str[i:(j+1)]);  
    
#     return output 

# str = input('Enter the String')

# result = subsets(str)
# for i in range(len(result)):
#     print(result[i])

# def arithmeticSeries(a1, a2, N):
#     d = a2-a1
#     return a1 + (N-1)*d

# a1 = int(input('Enter a1'
# ))
# a2 = int(input('Enter a2'))

# N = int(input('Enter Nth term'))

# print(arithmeticSeries(a1, a2, N))

# def areaCircle(radius):
#     pi = 3.14

#     return pi*radius*radius 

# try:
#     radius = float(input("Enter the radius of a circle:"))
#     print(areaCircle(radius))
# except:
#     print('Invalid Input')



def subString(str):
  output=[]
  def permute(a, b):
    output.append(a)
    if len(b)==0:
       return
    for i in range(len(b)):
      permute(b[i]+a, b[:i])
  permute("",str)
  return output

str = input('Enter string')
result = subString(str)
print(result)