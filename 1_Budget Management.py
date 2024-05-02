
class BudgetCategory:
    def __init__(self, category, budget):
        self.__category = category
        self.__budget = budget

    def set_category(self, new_category):
        self.__category = new_category
        
    def get_category(self):
        return self.__category
    
    def set_budget(self, new_budget):
        self.__budget = new_budget 
        
    def get_budget(self):
        return self.__budget
        
   ################################################################################ 

    def add_expense(self, amount):
        self.amount = amount
        if 0 < amount <= self.get_budget():
            self.set_budget(self.get_budget() - amount)
            print(f"Spent: ${amount}")
            print(f'Left budget: ${self.get_budget()}')
        elif amount > self.get_budget():
            print("You don't have that amount in your allocated budget.")
        else:
            print('Invalid input.')
            
    
   ################################################################################ 


    def display_category_summary(self):
    
        print(f'{self.__category}: allocated budget - ${self.__budget}, remaining budget - ${self.get_budget()}.')


# I must be setting allocated budget wrong. 
# When I run the function "display_category_summary" I get the value of the remaining budget instead.   

# Example usage
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()



