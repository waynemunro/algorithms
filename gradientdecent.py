points = [(2,4), (3,1), (4,2), (1,3)]
# points = [(2,4),  (4,2)]

def F(W):
    return sum((W * x -y) ** 2 for x, y in points)

def dF(W):
    return sum(2*(W * x -y) * x for x, y in points)

# Gradient Descent
W = 0
eta = 0.01
for t in range(100):
    value = F(W)
    gradient = dF(W)
    W = W - eta * gradient
    print("iteration {}: W = {}, F(W) = {}".format(t, W, value))

