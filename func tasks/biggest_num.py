def largest_num(first, second, third):
  return max(first,second,third)

def inputs():
  x = int(input("Enter first number: "))
  y = int(input("Enter second number: "))
  z = int(input("Enter third number: "))
  return x, y, z

def main():
  x, y, z = inputs()
  print("The largest of the numbers is {}".format(largest_num(x, y, z)))

main()