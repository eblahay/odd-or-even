# main application file

# return true if x is an even integer
def isEven(x):
    # stores the remainder of "x / 2"
    return (x % 2 == 0)


# main function
def main():
    b = isEven(5)
    
    if(b == True):
        print("even")
    else:
        print("odd")

# execute main()
if __name__ == "__main__":
    main()