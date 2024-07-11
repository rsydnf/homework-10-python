from fibonacci import fibonacci

def main():
    numTerms = int(input("Enter the number of Fibonacci terms: "))
    seq = fibonacci(numTerms)
    print ("The Fibonacci sequence is:"+", ".join(map(str, seq)))

if __name__ == "__main__":
    main()
