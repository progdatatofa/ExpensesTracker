#TEST RUNNING FILE

from storage import ExpensesStorage
from manager import ExpensesManager

storage = ExpensesStorage("expenses.json")
manager = ExpensesManager(storage)



 # HELPER FOUNCTION HERE
def get_id():
    while True:
        try:
            expense_id = int(input("Enter ID: "))
            if expense_id <= 0:
                print("ID Is required.")
            else:
                return expense_id
        except ValueError:
            print("Invalid Type")
def get_description(prompt = "Enter Search Description: "):
    while True:
        description = input("Enter Description: ")
        if not description:
            print("Description Is Required.")
        else:
            return description
    

def get_amount():
    while True:
        try:
            amount = float(input("Enter Amount. "))

            if amount <= 0:
                print("Amount Must Be Greater Than Zero")
            else:
                return amount
        except ValueError:
            print("Invalid Type")

def get_category(prompt = "Enter Search Description: "):
    while True:
        category = input("Enter Category: ")
        if not category:
            print("Category Is Required.")
        else:
            return category
            
def get_date():
    while True:
        date = input("Enter Date: ")
        if not date:
            print("Date Is Required.")
        else:
            return date

def menu():




    while True:
        


        print(
                "\n===================================================\n"
                "          KULOFTOP EXPENSE TRACKER\n"
                "===================================================\n"
                "1. Add Expense\n"
                "2. View Expenses\n"
                "3. Search Expense\n"
                "4. Update Expense\n"
                "5. Delete Expense\n"
                "6. Calculate Total Expenses\n"
                "7. Show Highest Expense\n"
                "8. Show Expenses by Category\n"
                "9. Calculate Total Category\n"
                "10. Exit\n"
                
        )
        option = input("\n\nChoose Option 1 - 11: ")
        if option == "1":
            
            print("\n-------------------------------------------------------\n")
            print("Add Expenses")

            description = get_description()
            amount = get_amount()
            category = get_category()
            date = get_date()

           

            

            manager.add_expenses(description , amount , category , date)

            print("\n-------------------------------------------------------\n\n")

        elif option == "2":
            print("-------------------------------------------------------")
            print("View Expenses")
            viewers = manager.get_all_expenses()
            if not viewers:
                return []
            else:
                for expense in viewers:
                    print(f"ID: {expense.expense_id}")
                    print(f"Description: {expense.description}")
                    print(f"Amount: {expense.amount}")
                    print(f"Category: {expense.category}")
                    print(f"Date: {expense.date}")
            print("-------------------------------------------------------")

            
            

        elif option == "3":
            print("--------------------------------------------------------")
            search_description = get_description("Enter Description To Search: ")
            result = manager.search_expenses(search_description)
            if not result:
                print("No Result Found")
            else:
                for expense in result:
                    print(f"ID: {expense.expense_id}")
                    print(f"Description: {expense.description}")
                    print(f"Amount: {expense.amount}")
                    print(f"Category: {expense.category}")
                    print(f"Date: {expense.date}")
            print("--------------------------------------------------------")

        elif option == "4":
            print("--------------------------------------------------------")
            print("Update Expenses")
            expense_id = get_id()

            print("Update Expenses Here")
        
            new_desc = get_description()
                
            new_amount = get_amount()
        
            new_category = get_category()
            new_date = get_date()
            success = manager.update_expense(expense_id, new_desc, new_amount, new_category , new_date)
            if success:
                print("Expense Updated Succesifully.")
            else:
                print("Update ID Is Not Available.")
            print("--------------------------------------------------------")

            
            

        elif option == "5":
            print("--------------------------------------------------------")
            print("Delete Expenses")
            expense_id = get_id()
            if manager.delete_expense(expense_id):
                print("Expense Deleted Successifully.")
            else:
                print("Delete ID Is Not Available.")
            print("--------------------------------------------------------")


        elif option == "6":
            print("--------------------------------------------------------")
            print("Calculate Total Expenses")
            result = manager.calculate_total_expenses()
            print(f"The Total Expenses is: {result}")
            print("--------------------------------------------------------")


        elif option == "7":
            print("--------------------------------------------------------")

            print("Show Highest Expenses")
            highest_expense = manager.show_highest_expense()
            if highest_expense is None:
                print("No Expenses Available")
            else:
            
                print("Highest Expense")
                print("-------------------------")
                print(f"ID: {highest_expense.expense_id}")
                print(f"Description: {highest_expense.description}")
                print(f"Amount: {highest_expense.amount}")
                print(f"Category: {highest_expense.category}")
                print(f"Date: {highest_expense.date}")


            print("--------------------------------------------------------")

        elif option == "8":
            print("--------------------------------------------------------")
            print("Category Based Expenses")
            category = get_category()
            results  = manager.get_expeses_by_category(category)
            if not results:
                print("Expenses Not Available.")
            for result in results:
                print(f"ID: {result.expense_id}")
                print(f"Description: {result.description}")
                print(f"Amount: {result.amount}")
                print(f"Category: {result.category}")
                print(f"Date: {result.date}") 

            print("--------------------------------------------------------")

        

        elif option == "9":
            print("--------------------------------------------------------")

            print("Calculate Total Expenses In Each Category")
            category = get_category()
            result = manager.total_category(category)
            if result is None:
                print("No Expenses Available.")
            else:
                print(f"The Total Category Based Expenses is : {result}")
            print("--------------------------------------------------------")

        elif option == "10":
            print("Exit Here")
            break
        else:
            print("Invalid Option ")


   

    


menu()