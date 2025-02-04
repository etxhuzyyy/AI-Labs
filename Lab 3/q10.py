# Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead
# of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three
# and five print "FizzBuzz".
# Sample Output : fizzbuzz
# 1
# 2
# fizz 4
# buzz


def fizz_buzz():
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
            
def main():
    fizz_buzz()
    
if __name__ == "__main__":
    main()
    
# Output: 1
#         2
#         Fizz
#         4
#         Buzz