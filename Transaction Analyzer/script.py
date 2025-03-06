data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

def print_transactions(transactions):
  for amount, statement in transactions:
    print(f"${amount} - {statement}")

def print_summary(transactions):
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_deposited = sum(deposits)
  total_withdrawn = sum(withdrawals)
  balance = total_deposited + total_withdrawn
  print (total_deposited)
  print(total_withdrawn)
  print (balance)

def analyze_transactions(transactions):
  transactions.sort()
  largest_withdrawal = transactions[0]
  largest_deposit = transactions[-1]
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposit = sum(deposits)
  withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_withdrawals = sum(withdrawals)
  if len(deposits) == 0:
    average_deposit = 0
  else:
    average_deposit = total_deposit / len(deposits)
  if len(withdrawals) == 0:
    average_withdrawal = 0
  else:
    average_withdrawal = total_withdrawals / len(withdrawals)
  print(largest_withdrawal)
  print(largest_deposit)
  print(average_deposit)
  print(average_withdrawal)
  

while True:
  print("Choose an option: 1.print 2.analyze 3.stop")
  choice = input()
  if choice == "print":
    print_summary(data)
  elif choice == "analyze":
    analyze_transactions(data)
  elif choice == "stop":
    break
  else:
    print("Invalid choice")
