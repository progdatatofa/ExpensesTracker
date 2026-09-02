from expense import Expense

class ExpensesManager():
    def __init__(self, storage):
        self.storage = storage
        self.expenses = []
        self.load_xist()

     

    def load_xist(self):
        data = self.storage.load()
        for item in data:


            expense = Expense(
                item["ID"],
                item["Description"],
                item["Amount"],
                item["Category"],
                item["Date"]


            )
            self.expenses.append(expense)
            



    def add_expenses(self , description, amount , category , date):
        expense_id = len(self.expenses) + 1
        expense = Expense(
            expense_id,
            description,
            amount,
            category,
            date
        )
        self.expenses.append(expense)
        self.storage.save(self.expenses)


    def get_all_expenses(self):
        return self.expenses
           


        

    def search_expenses(self , search_description):
        result = []
        for expense in self.expenses:
            if expense.description.lower() == search_description.lower():
                result.append(expense)
        return result



    def update_expense(self, expense_id , new_desc , new_amount , new_category , new_date):
        
        for expense in self.expenses:
            if expense.expense_id == int(expense_id):
                
                

                
                
                expense.description = new_desc
                expense.amount = new_amount
                expense.category = new_category
                expense.date = new_date

                
                
                self.storage.save(self.expenses)
                return True
        return False
                
        
        

    def delete_expense(self, expense_id):
        
        
        
        for expense in self.expenses:
            if expense.expense_id == int(expense_id):
                
                self.expenses.remove(expense)
                self.update_delete_id()
                self.storage.save(self.expenses)
                
                return True
        return False
        
        


    def update_delete_id(self):
        counter = 1
        for expense in self.expenses:
            expense.expense_id = counter
            counter += 1


    def calculate_total_expenses(self):
        total = 0
        
        for expense in self.expenses:
            total += expense.amount
            
        return total
    
    


    def show_highest_expense(self):

        if not self.expenses:
            
            return None

        current = 0
        highest_expense = None
        
        for expense in self.expenses:
            if expense.amount > current:
                current = expense.amount
                highest_expense = expense
            
        return highest_expense




        
    
        


    def get_expeses_by_category(self , category):
        
        category_results = []
        for expense in self.expenses:
            if expense.category.lower() == category.lower():
                category_results.append(expense)
        return category_results
                

   



    def total_category(self , categoty):
        total = 0
        results = None
        
        for expense in self.expenses:
            if expense.category.lower() == categoty.lower():

                
                total += expense.amount
            results = total
        return results
       

                    
