import json
class ExpensesStorage:
    def __init__(self , filename):
        self.filename = filename

    def save(self , expenses):
        data = [expense.to_dict() for expense in expenses]
        with open(self.filename , "w") as file:
            json.dump(data , file , indent= 4)

        
    def load(self):
        try:
            with open(self.filename , "r") as file:
                return json.load(file)
        except:
            return []