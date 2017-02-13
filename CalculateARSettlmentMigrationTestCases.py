def printTransactionQueues():
   print("Transaction Queue Count: " + str(len(transactionQueues)))
   for transactionQueue in transactionQueues:
       print(transactionQueue)
   print()

transactions=("P", "I", "I", "R", "R")

print("Step 1: Calculate all possibilities")
transactionQueues=[[]]
for transaction in transactions:
    newTransactionQueues=[]
    for transactionQueue in transactionQueues:
        for index in range(len(transactionQueue) + 1):
            newTransactionQueue=transactionQueue.copy()
            newTransactionQueue.insert(index, transaction)
            newTransactionQueues.append(newTransactionQueue)
    transactionQueues=newTransactionQueues
printTransactionQueues()

print("Step 2: Remove the queues in which R is before P")
newTransactionQueues=[]
for transactionQueue in transactionQueues:
    if transactionQueue.index("P") > transactionQueue.index("R"):
        continue
    newTransactionQueues.append(transactionQueue)
transactionQueues=newTransactionQueues
printTransactionQueues()

print('''Step 3: Merge "I"->"I" to "I", "R"->"R" to "R"''')
newTransactionQueues=[]
for transactionQueue in transactionQueues:
    newTransactionQueue=[]
    previousTransaction=""
    for transaction in transactionQueue:
        if previousTransaction != transaction:
            newTransactionQueue.append(transaction)
        previousTransaction=transaction
    newTransactionQueues.append(newTransactionQueue)
transactionQueues=newTransactionQueues
printTransactionQueues()

print("Step 4: Remove duplicated queues")
newTransactionQueues=[]
for transactionQueue in transactionQueues:
    for newTransactionQueue in newTransactionQueues:
        if len(transactionQueue) != len(newTransactionQueue):
            continue
        else:
            for i in range(len(transactionQueue)):
                if transactionQueue[i] != newTransactionQueue[i]:
                    break
            else:
                # transactionQueue exists in newTransactionQueues
                break
    else:
        # transactionQueue does not exist in newTransactionQueues
        newTransactionQueues.append(transactionQueue)
transactionQueues=newTransactionQueues
printTransactionQueues()

print("Step 5: Add index to I and R")
for transactionQueue in transactionQueues:
    indexI=indexR=1
    for i in range(len(transactionQueue)):
        if transactionQueue[i] == "I":
            transactionQueue[i]="I"+str(indexI)
            indexI+=1
        elif transactionQueue[i] == "R":
            transactionQueue[i]="R"+str(indexR)
            indexR+=1
printTransactionQueues()
