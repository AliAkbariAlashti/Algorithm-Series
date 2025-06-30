def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
print("GCD of 48 and 18:", gcd(48, 18))