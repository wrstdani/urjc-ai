x = [-10, 0, 10]
g = @(x)sin(x)+cos(x)+x.^2+((x.^2)./(x+1))
plot(x, g(x))
