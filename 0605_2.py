while True:
    print("="*30)
    print("1,n까지 정수의 합")
    print("2.n~m까지 k의 배수의 합")
    print("3.구구단 출력")
    print("4.종료")
    print("="*30)
    menu=int(input("정수를 입력하세요(1~4):"))

    if menu==1:
        n=int(input("하나의 정수를 입력하시오: "))

        sum=0
        for i in range(n+1):
            sum=sum+i
        print("1부터 %d까지의 합은 %d" %(n,sum))

    if menu==2:
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

    if menu==3:
        dan=int(input("원하는 단은: "))
        i=1

        while i<=9:
            print("%d*%d=%d" %(dan,i,dan*i))
            i=i+1

    if menu==4:
        print("프로그램을 종료합니다 띠로리.....")
        break
