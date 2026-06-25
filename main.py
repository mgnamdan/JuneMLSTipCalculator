# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# HELPER FUNCTIONS AND IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def calculateTip(billAmt, tip):
    return billAmt * (tip / 100)


def printTotal(tipPercent, tipAmt, tipTotal):
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print(f" {tipPercent}%: {tipAmt:.2f} --> Your total would be: {tipTotal:.2f}" )
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION DEFINITION
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    # 1. Take in bill amount (x)
    # 2. Figure out tip amount (x)
    #   --> Default with 10%, 15%, 20%
    # 3. Print out tip and bill total with tip (x)

    print("")
    print("Enter your bill total:")
    rawTotal = float(input(" --> ").strip("$"))

    print("")
    print("How much would you like to tip?")
    tipPercent = float(input(" --> ").strip())

    tipAmt = calculateTip(rawTotal, tipPercent)
    tipTotal = rawTotal + tipAmt

    printTotal(tipPercent, tipAmt, tipTotal)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION CALL
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
main()
