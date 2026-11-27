from math import exp, isclose

speed = [100*x/(2+x) for x in (1,2,4)]
growth = [(t,100/(1+exp(-.5*(t-4))),100*exp(-exp(-.5*(t-4))))
          for t in range(9)]
f = ((96-60)/2)/(60/20)
p = (1+2*f/20)**-10
print(speed, growth)
print(f,p)
assert speed[1]==50 and growth[4][1]==50 and f==6
assert isclose(p,.009094947017729282)
