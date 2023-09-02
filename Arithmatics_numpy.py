
import numpy as np

num1 = np.arange(1,11)
num2 = np.random.randint(11,size=(10))

print("\nSummation")
print(f"  {num1}\n+ {num2} \n=",num1+num2)

print("\nSubstraction")
print(f"  {num1}\n- {num2} \n=",num1-num2)

print("\nMultiplication")
print(f"  {num1}\nx {num2} \n=",num1*num2)

print("\nDivision")
print(f"  {num1}\n/ {num2} \n=",num1/num2)

print("\nSquare")
print(f"  {num1} ^ 2 =",num1**2)
print(f"  {num2} ^ 2 =",num2**2)

print("\n")
print(f"Max {num1} =",np.max(num1))
print(f"Max {num2} =",np.max(num2))

print(f"Min {num1} =",np.min(num1))
print(f"Min {num2} =",np.min(num2))

print()
num3 = np.random.randint(11,size=(3,3))
print(f"Max column \n{num3} \n=",np.max(num3,0))
print(f"Max row \n{num3} \n=",np.max(num3,1))

print()
num3 = np.random.randint(11,size=(3,3))
print(f"Min column \n{num3} \n=",np.min(num3,0))
print(f"Min row \n{num3} \n=",np.min(num3,1))
