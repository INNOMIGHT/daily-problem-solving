from collections import defaultdict

def invalidTransactions(transactions):
    out = [] #list of all the invalid transactions to return 
    names = defaultdict(lambda: defaultdict(set)) #{name: {time: city}}
    
    
    for t in transactions:
        name,time,amount,city = t.split(",")
        names[name][time].add(city)
        names[name][time].add(amount)
        names[name][name].add(time)
        
    #-if a certain person is at more than one city at a time then we know it's an invalid transaction
	#-if the city we're at is not in the set it means the transaction has been made at two places within the 60 min limit
	
	#I want to preface the rest of this solution by saying this has worked so far but I'm unsure if there's ever a testcase
	#in which this would not function correctly. This was a very tricky question and it definitely took me a while 
	#to even come up with a working solution
    print(names)
    for t in transactions:
        name, time, amount, city = t.split(",")
        if int(amount) > 2000:
            out.append(t)            
        else:
            for num in names[name].keys():
                if -60 <= int(time) - int(num) <= 60 and (len(names[name][num]) > 1 or city not in names[name][num]):
                    out.append(t)
                    break
    print(out)


invalidTransactions(["john,20,800,stockholm","john,50,100,beijing"])