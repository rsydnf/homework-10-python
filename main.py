from fibonacci import doFibonacci

def main():
    numTerms = int(input("Enter the number of Fibonacci terms: "))
    seq = doFibonacci(numTerms)
    print ("The Fibonacci sequence is:"+", ".join(map(str, seq)))

if __name__ == "__main__":
    main()
