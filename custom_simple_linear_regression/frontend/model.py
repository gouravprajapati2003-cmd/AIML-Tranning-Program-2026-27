class MyLr:
    def __init__(self):
        self.m = 0
        self.c = 0
    def fit(self,x, y):
        n = len(x)
        sum_xy = 0
        sum_x_x = 0
        for i in range(n):
            sum_xy = sum_xy + x[i]*y[i]
        for i in x:
            sum_x_x = sum_x_x + i*i
        denominator = n*sum_x_x - sum(x) * sum(x)
        slope = (n*sum_xy - sum(x) * sum(y)) / denominator
        intercept = (sum(y) * sum_x_x - sum(x) * sum_xy)/ denominator
        print("Slope...")
        print(slope)
        print("Intercept...")
        print(intercept)
        self.m = slope
        self.c = intercept
    def predict(self, x):
        print(self.m)
        print(self.c)
        y = self.m * x + self.c
        print("result")
        print(y)
        return y;