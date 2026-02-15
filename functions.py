def sayhello():#tuppo ma rakheko ramro 
    print("hello user")
    print("k xa")
print("Top")
sayhello() #yo garyo vaney first ma top ani sayhello ani last ko
print("no") 

def sayhello(name,age):
    print("hello" + name+",you are " +age)
sayhello("mila","35")
sayhello("ram","55")

def cube(num):
    return num*num*num

print(cube(4))

def cube(num):
    return num*num*num
    
result = cube(4)

print(cube(4))
def kam():
    print("hello man")
    
print("im a god of coding")
kam()
print("we are the champion")

def bam(name,num):
    print("we are"+name+"with best coding skills if i convert into number"+num )
bam("mike","25")

def cube(num):
    return num*num*num  
    print("code")#run hudaina

result = cube(4)
print(result)

num4 = 10
def addition(x,y=0,z=1):
 addition(2)




z = 30
def b():
    global z
    z = z + 5
    print("inside function",z)
    b()
    print("outside functions",z)


def b(*varj):#tuples jasari kaam garxa
    print(varj)
    b(1,5,7,8,97,8,7)
def c(**kaks):
    print(kaks)
    c(name="man",age=12)