def Narcissistic_Number(num):
      sum=0
      length=len(str(num))
      temp=num
      while temp>0:
          digit=temp%10
          sum+=digit**length
          temp//=10
      if num==sum:
          return True
      return False
try:
    num=int(input("Enter a number: "))
    if Narcissistic_Number(num):
        print(f"{num} is a Narcissistic number.")
    else:
        print(f"{num} is not a Narcissistic number.")
except ValueError:
    print("Please enter a valid number.")