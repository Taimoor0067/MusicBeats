def function(age):
    firstage=int(input("Enter the your age: "))
    secondage=int(input("Enter the your friend age: "))
    total=sum(firstage,secondage)
    print("Together you are",total,'yearold')

def sum(num1, num2):
    result = num1 + num2
    return result

function('age')
