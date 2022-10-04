# main application file

from argparse import ArgumentParser


# return true if x is an even integer
def isEven(x):
    return (x % 2 == 0)


# main function
def main():
    parser = ArgumentParser()

    parser.add_argument('x', type=int, help="an integer which will have its parity determined")
    parser.add_argument(
        '--version', 
        action='version', 
        version='odd-or-even 0.1.0', 
        help="prints out this program's version information and then quits"
    )

    args = parser.parse_args()

    # determine the parity of the int & output the result
    if(isEven(args.x)):
        print("even")
    else:
        print("odd")

# execute main()
if __name__ == "__main__":
    main()