transactions=("P", "I1", "I2", "R1", "R2")
transactionQueues=[["P"]]
for transaction in [x for x in transactions if x != "P"]:

    print("Transaction: " + transaction)

    newTransactionQueues=[]
    for transactionQueue in transactionQueues:

        print("Existing Transaction Queue: " + str(transactionQueue))

        for index in range(len(transactionQueue) + 1):
            newTransactionQueue=transactionQueue.copy()
            newTransactionQueue.insert(index, transaction)
            newTransactionQueues.append(newTransactionQueue)

    transactionQueues=newTransactionQueues


newTransactionQueues=[]
print()
print("Transaction Queue Count: " + str(len(transactionQueues)))
for transactionQueue in transactionQueues:
    print(transactionQueue)

    if (transactionQueue.index("P") > transactionQueue.index("R1")) or (transactionQueue.index("P") > transactionQueue.index("R2")):
        continue

    newTransactionQueue=[]
    previousTransaction=""
    currentTransaction=""
    for transaction in transactionQueue:
        currentTransaction = transaction
        if previousTransaction != "":
            if previousTransaction[0] == "I" and currentTransaction[0] == "I":
                newTransactionQueue.append("I")
                currentTransaction=""
            elif previousTransaction[0] == "R" and currentTransaction[0] == "R":
                newTransactionQueue.append("R")
                currentTransaction=""
            else:
                newTransactionQueue.append(previousTransaction)
        previousTransaction=currentTransaction
    newTransactionQueue.append(currentTransaction)

    newTransactionQueues.append(newTransactionQueue)

    
transactionQueues=newTransactionQueues
print()
print("Transaction Queue Count: " + str(len(transactionQueues)))
for transactionQueue in transactionQueues:
    print(transactionQueue)
