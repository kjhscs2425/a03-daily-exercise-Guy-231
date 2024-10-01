# 1) Update the comments and choose between "function", "variable", and "parameter"

import turtle

# `dance` is a ...\variable.
def dance():
  turtle.left(1000)
  turtle.right(500)

# `pi` is a  variable
pi = 3.1415926535

# `convert` is a ...[function
# and `celcius` is a parameter
def convert(celcius):  
   # `fahrenheit` is a  variable
  fahrenheit = celcius * 9 / 5 + 32
  print(fahrenheit)

# `draw_spiral` is a ...[function
# and `num_loops` is a variable
# and `distance` is a variable
# and `angle` is a ...variable
def draw_spiral(num_loops, distance, angle):
  for i in range(num_loops):
    for _ in range(2):
      # `arm_length` is a parameter
      arm_length = i*distance
      turtle.forward(arm_length)
      turtle.left(angle)

# `say_hello` is a parameter
# and `name` variable
def say_hello(name):
  print("Hello, " + name)
  print("How are you today?")

# 2. Call `say_hello`
#    a) Call `say_hello` with the argument "Dr. EB"
print("hello, " + "Dr. EB")
#    b) Call `say_hello` with your name as the argument
print("hello, " + "Guy")
#    c) Call `say_hello` with a friend's name as the argument
print("hello, " + "Edo")

# 3. Call `draw_spiral` with the following arguments:
#    a) use 5 for `num_loops`
#       use 10 for `distance`
#       use 45 for `angle`
draw_spiral(num_loops = 5, distance = 10, angle = 45)

#    b) use 11 for `num_loops`
#       use 5 for `distance`
#       use 120 for `angle`
draw_spiral(num_loops = 11, distance = 5, angle = 120)
#    c) use 20 for `num_loops`
#       use 1 for `distance`
#       use 60 for `angle`
draw_spiral(num_loops = 20, distance = 1, angle = 60)
turtle.exitonclick()
