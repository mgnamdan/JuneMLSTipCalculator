# 1. Take in bill amount (x)
# 2. Figure out tip amount (x)
#   --> Default with 10%, 15%, 20%
# 3. Print out tip and bill total with tip (x)

print("")
print("Enter your bill total:")
rawTotal = float(input(" --> "))

tenPercent = .1 * rawTotal
fifteenPercent = .15 * rawTotal
twentyPercent = .2 * rawTotal

print("")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("")
print(f"                  10%: {tenPercent} --> Your total would be: {rawTotal + tenPercent}" )
print(f"                  15%: {fifteenPercent} --> Your total would be {rawTotal + fifteenPercent}")
print(f"                  12%: {twentyPercent} --> Your total would be {rawTotal + twentyPercent}")
print("")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")