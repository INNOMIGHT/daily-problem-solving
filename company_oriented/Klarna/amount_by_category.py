class AmountCalculator():

    def __init__(self, list_of_transactions, category, start_time, end_time):
        
        self.list_of_transactions = list_of_transactions
        self.category = category
        self.start_time = start_time
        self.end_time = end_time

    def calculate_amount(self):
        
        amount = 0
        for i in range(len(self.list_of_transactions)):
            if self.list_of_transactions[i].time > self.start_time:
                for j in range(i+1, len(self.list_of_transactions)):
                    if self.list_of_transactions[j].time < self.end_time:
                        amount += self.list_of_transactions[j].amount

        return amount
                
