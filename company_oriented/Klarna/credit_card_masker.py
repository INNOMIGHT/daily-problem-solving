class CreditCardMasker():

    def __init__(self, credit_no):

        self.credit_no = credit_no

    def masked_number(self):

        length = len(str(self.credit_no))
        if length < 6:
            return self.credit_no
        masked_length = length - 5
        credit_card = str(self.credit_no)
        credit_card_arr = []
        for j in credit_card:
            credit_card_arr.append(j)
        for i in range(1, masked_length+1):
            if credit_card_arr[i].isdigit():
                credit_card_arr[i] = "*"
        
        return credit_card_arr


credit_card_no = CreditCardMasker("123A56789")
print(credit_card_no.masked_number())
            
        