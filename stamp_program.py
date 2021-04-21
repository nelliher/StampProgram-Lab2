"""
start
get the numbers of sheets
sheet / 5
round answer to next number
output the result to the master
end
"""
def calculate(sheet):
  answer = sheet / 5
  rounded = round(answer)
  print("sheet is : ", sheet)
  print("the answer is :", answer)
  print("rounded is :", rounded)
  print("====================================")
  return rounded 

output = calculate(10000)

print("the return statement is:", output)
