# AN INDIVIDUAL EXPENSE REPORISOTORY
class Expense:
    def __init__(self, expense_id , description , amount , category , date):
        self.expense_id = expense_id
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date


    # Store the contens in dictionary
   
    def to_dict(self):
       return{
          "ID" : self.expense_id,
          "Description" : self.description,
          "Amount" : self.amount,
          "Category" :  self.category,
          "Date" : self.date
       }
        