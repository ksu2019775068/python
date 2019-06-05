n=int(input("시작 값을 입력하세요: "))
m=int(input("끝 값을 입력하세요: "))
k=int(input("배수를 입력하세요: "))

def k_sum(n,m,k):
    sum=0
    for i in range(n, m+1):
        if i%k==0:
            sum=sum+i
    return sum

hap=k_sum(n,m,k)
print("%d에서 %d까지 %d의 배수의 합은 %d입니다." %(n,m,k,hap))

    
