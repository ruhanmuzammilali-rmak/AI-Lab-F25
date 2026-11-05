def rule_based(score, document_complete, fee_status,attendance):
  
  if score >=70 and document_complete ==True and fee_status=="paid" and attendance>=75:
    return "review"
  else:
    return "hold"
def Reason(score, document_complete, fee_status,attendance):
  reasons = []

  if document_complete == False:
    reasons.append ("incomplete documents")
  if score < 70 :
    reasons.append("your score below 70")
  if fee_status.lower() != "paid":
    reasons.append("you not pay tha fee")
  if attendance < 75:
    reasons.append("your attendance is short")
  if len(reasons)==0:
    return ("all conditions are satisfiy")
  else:
    return (", ".join(reasons))
test_cases = [
    ("pass-case",80, True, "paid", 82,"review"),

    ("fee-unpaid", 80,True,"unpaid",82,"hold"),
    ("short-attendance",80,True,"paid",73,"hold"),
    ("boundry",70,True,"paid",75,"review")
]
for name,score ,doc,fee,atten,expt in test_cases:
  actual = rule_based(score, doc, fee, atten)
  reason = Reason(score, doc, fee, atten)
  print(f"test name: {name}")
  print(f"user-input: score = {score} documents_complete = {doc} fee_status = {fee}, attendance = {atten}")
  print(f"expected: {expt}")
  print(f"actual: {actual}")
  print(f"reason: {reason}")
  if expt == actual:
    print("Result: Pass")
  else:
    print("Result: Fail")