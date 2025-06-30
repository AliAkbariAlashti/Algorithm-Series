def gradient_descent(x, learning_rate=0.1, iters=100):
    for _ in range(iters):
        gradient = 2 * x  # Derivative of x^2
        x -= learning_rate * gradient
    return x

# Example usage
print("Minimized x for x^2:", gradient_descent(10))