#VENDING MACHINE | Elizabeth Joy Mendoza | CC L4 | FTSC AUH

class VendingMachine:
    def __init__(self, products, prices): 
        # This is the constructor method that initializes the vending machine with a list of products and their corresponding prices. It also initializes the balance to 0.
        self.products = products
        self.prices = prices
        self.balance = 0

    def insert_money(self, amount): # This allows the user to insert money into the vending machine. It updates the balance by adding the inserted amount and returns a message confirming the amount inserted.
        self.balance += amount
        return "You have inserted " + str(amount) + " dirham."

    def select_product(self, product): 
        # This is used to select a product for purchase. It checks if the selected product is available in the vending machine's product list. If the balance is sufficient to purchase the selected product, it deducts the price from the balance and returns a message confirming the successful purchase along with the remaining balance. If the balance is insufficient or the product is not available, appropriate error messages are returned.
        if product in self.products:
            if self.balance >= self.prices[product]:
                self.balance -= self.prices[product]
                # prints output of name of item or product and shows exact change of dirham and thanks the consumer or user
                return "Dispensing " + product + ". Your change is " + str(self.balance) + " dirham." + " Thank you for your purchase!"
            else:
                return "Insufficient balance. Please insert more money."
        else:
            return "Product not available."


# item name and prices for the program to take reference from 
vending_machine = VendingMachine(['coca cola', 'sprite', 'fanta','water', 'apple juice', 'cold coffee', 'doritos', 'mentos mint', 'bubblegum','cheese lays', 'takis', 'cheese puffs', 'korean dalgona', 'hot doritos', 'gummy bears'], {'bubblegum': 2.4, 'fanta': 2.0, 'gummy bears': 1.0, 'hot doritos': 5.6, 'korean dalgona': 3.5,'coca cola': 2.0, 'doritos': 5.5, 'mentos mint': 2.0, 'sprite': 2.0, 'takis': 5.2, 'cheese lays': 3.5, 'apple juice': 4.0, 'cold coffee': 2.5, 'cheese puffs': 7.0, 'water': 2.5})

print('VENDING MACHINE \n\fITEM   PRICE \nDRINKS\ncoca cola: 2.0 \nsprite: 2.0 \nfanta: 2.0 \nwater: 2.5 \napple juice: 4.0 \ncold coffee: 2.5 \n\fCHIPS \ndoritos: 5.5 \ncheese lays: 3.5 \ntakis: 5.2 \ncheese puffs: 7.0 \nhot doritos: 5.6 \n\fSWEETS \nmentos mint: 2.0 \nbubblegum: 2.4 \nkorean dalgona: 3.5 \ngummy bears: 1.0')
# asks input from the user, first money amount, next prompt if the input is true, is the product purchase.
amount = float(input("Enter the amount of money to insert: "))
print(vending_machine.insert_money(amount))

choice = input("Enter the product you want to purchase: ")
print(vending_machine.select_product(choice))