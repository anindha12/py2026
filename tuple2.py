def palind(r):
    e = len(r) -1
    s = 0   
    while e > s:        
        if r[s] != r[e]:
            return False
        s += 1
        e -= 1
    return True 

r = input("Enter a Word or Number: ")

if palind(r):
    print("The string is a palindrome.")
else:   
    print("The string is not a palindrome.")
