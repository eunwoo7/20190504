def avg(a,b,c):
    avg = (a + b + c) / 3
    return avg

n1 = int(input("첫 번째 정수: "))
n2 = int(input("두 번째 정수: "))
n3 = int(input("세 번째 정수: "))

avg = avg(n1,n2,n3)
print(n1,",",n2,",",n3,"의 평균은",avg(n1,n2,n3),"입니다.")
      
