#Calculate the compound interest for a given principal amount, interest rate, and time period.

def compoundInterest(pa, ir, p):
    sum = 0
    gainOrLoss = 0
    for index in range(p):
            gainOrLoss = (pa + sum) * (ir /pa)
            sum += gainOrLoss
    return sum

def simpleInterest(pa, ir, p):
      sum = pa * (ir / pa) * p
      return round(sum)

def userAmoutAndInterasteRateAndPeriod():
    try:
            principalAmount = int(input("Your principal amount : "))
            interestRate = int(input("The interest rate : "))
            period = int(input("The period : "))
            s = simpleInterest(principalAmount, interestRate, period)
            c = compoundInterest(principalAmount, interestRate, period)
            return s, c
            
    except ValueError:
            print("Something went wrong. Please try again")
            

def main():
    s, c = userAmoutAndInterasteRateAndPeriod()
    print("The sum of the interest component is ", s,". The sum of compound interest is ", c)

if __name__ == "__main__":
    main()