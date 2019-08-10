# Her fibonacci sayısı kendinden önceki sayı ile kendisinin toplamı kadar yeni bir sayı yaratarak devam eder
# (1),1,(1+1=)2,(1+2=)3,(2+3=)5,(3+5=)8,.......

a = 1
b = 1

fibonacci = [a,b]

for sayi in range(20):
    a,b=b,a+b
    fibonacci.append(b)
    print("A : ",a,"B : ",b)

print(fibonacci)