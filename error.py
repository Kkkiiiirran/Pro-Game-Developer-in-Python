# # try
    
# # except 

# # finally

tasks = ["red"]
while True:
    choice = int(input("enter your choice"))


    if choice == 1:
        remove= "red"

   
        try:
            tasks.remove(remove)
            print(10/0)
        
        except ValueError:
            print("element not found")
        
        except ZeroDivisionError as z:
            print("division by zero not allowed", )



        print("done")
        break

        
try:
    raise ArithmeticError("Arithmetic error occurred")
except ArithmeticError as e:
    print(e)


print(10/0)
