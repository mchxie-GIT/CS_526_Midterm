import sys

def check_snowfall(n, totals):
    if n < 3:
        return "NO"
        
    #Subtract totals to get each three-day amount
    for i in range(n - 2):
        three_days = totals[i + 2]
        if i > 0:
            three_days -= totals[i - 1]

        if three_days * 2 > totals[-1]:
            return "YES"

    return "NO"

def main():
    with open(sys.argv[1]) as file:
        n = int(file.readline())
        values = file.readline().split()

    totals = [float(value) for value in values]
    answer = check_snowfall(n, totals)
    print(" ".join(values) + " solution: " + answer)

if __name__ == "__main__":
    main()
