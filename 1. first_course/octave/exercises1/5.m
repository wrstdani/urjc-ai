g = @(x)sin(x)+cos(x)+x.^2+((x.^2)./(x+1))
a = 2
fsolve(g, a)
