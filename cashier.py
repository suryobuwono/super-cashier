from tabulate import tabulate
from re import sub


class Transaction:

    num_customer = 0
    bookkeeping = {}

    def __init__(self):
        """Initialize a new transaction object for a unique customer."""
        Transaction.num_customer += 1
        self.customer_id = f"Customer {Transaction.num_customer}"
        self.data = {}  # stores item_name: [quantity, price, total_price]
        self.transaction = {
            "No.": None,
            "Item": None,
            "Quantity": None,
            "Unit Price": None,
            "Total Price": None
        }


    def add_item(self):
        """Adds a new item to the shopping cart."""
        # Input item name
        try:
            print("Ensure no typo when entering item name.")
            item_name = str(input("  Item name: ")).lower()
            item_name = sub(r"[^A-Za-z\s]", "", item_name).strip()

            if not item_name:
                print("\nYou are not allowed to leave this field empty.")
                return
            if item_name in self.data:
                print(f"\nItem '{item_name}' already exists in the cart. Use 'update_item()' to modify it.")
                return
        except Exception:
            print("\nPlease re-enter item name using only letters.")
            return

        # Input item quantity
        try:
            print("\nEnter quantity using numbers only. Example: 6")
            item_qty = input("  Item quantity: ")
            item_qty = int(sub(r"\D", "", str(item_qty)))
            if item_qty == 0:
                print("\nItem quantity cannot be 0.")
                return
        except Exception:
            print("\nPlease re-enter quantity using only digits.")
            return

        # Input item price
        try:
            print("\nEnter item price using numbers only, no thousand separators. Example: 20000")
            item_price = input("  Unit price: ")
            item_price = int(sub(r"\D", "", str(item_price)))
            if item_price == 0:
                print("\nUnit price cannot be 0.")
                return
        except Exception:
            print("\nPlease re-enter unit price using only digits.")
            return

        # Store item in data dictionary
        total_price = item_qty * item_price
        self.data[item_name] = [item_qty, item_price, total_price]

        # Display result
        print(" ")
        print(f"\nItem '{item_name}' has been successfully added to your cart.")
        self.__show_trx(item_name, item_qty, item_price, total_price)


    def update_item(self):
        """Allows user to update name, quantity, or price of an existing item."""
        try:
            print("Which item detail would you like to update?")
            feature = str(input("(name / quantity / price)\n")).lower()
            feature = sub(r"[^A-Za-z\s]", "", feature).strip()
            if feature not in ["name", "quantity", "price"]:
                print("\nPlease choose from: name, quantity, or price")
                return
        except Exception:
            print("\nPlease choose from: name, quantity, or price")
            return

        # Input item name
        try:
            item_name = str(input("\nItem name: ")).lower()
            item_name = sub(r"[^A-Za-z\s]", "", item_name).strip()

            if not item_name:
                print("\nYou are not allowed to leave this field empty.")
                return
            if item_name not in self.data.keys():
                print(f"\nItem '{item_name}' not found in your cart.")
                return
        except Exception:
            print("\nPlease re-enter name using only letters.")
            return

        # Dispatch update based on selected feature
        if feature == "name":
            self.__update_item_name(item_name)
        elif feature == "quantity":
            self.__update_item_qty(item_name)
        elif feature == "price":
            self.__update_item_price(item_name)


    def __update_item_name(self, item_name):
        """Update an existing item's name, used internally by update_item()."""
        # Input new name
        try:
            new_name = str(input("Enter new item name: ")).lower()
            new_name = sub(r"[^A-Za-z\s]", "", new_name).strip()
            if not new_name:
                print("\nYou are not allowed to leave this field empty.")
                return
        except Exception:
            print("\nPlease re-enter name using only letters.")
            return

        # Store new name replacing old name
        self.data[new_name] = self.data.pop(item_name)
        
        # Display result
        print(f"\nItem name '{item_name}' has been changed to '{new_name}'.")
        item_qty, item_price, total_price = self.data[new_name]
        self.__show_trx(new_name, item_qty, item_price, total_price)


    def __update_item_qty(self, item_name):
        """Update quantity for an existing item, used internally by update_item()."""
        # Input new quantity
        try:
            new_item_qty = input("Enter new quantity: ")
            new_item_qty = int(sub(r"\D", "", str(new_item_qty)))
            if new_item_qty == 0:
                print("\nQuantity cannot be 0.")
                return
        except Exception:
            print("\nPlease re-enter quantity using only digits.")
            return        
        
        # Store new quantity and update total price
        self.data[item_name][0] = new_item_qty
        self.data[item_name][2] = self.data[item_name][0] * self.data[item_name][1]
        
        # Display result
        print(f"\nQuantity for '{item_name}' has been changed to {new_item_qty}.")
        item_qty, item_price, total_price = self.data[item_name]
        self.__show_trx(item_name, item_qty, item_price, total_price)


    def __update_item_price(self, item_name):
        """Update price for an existing item, used internally by update_item()."""
        # Input new price
        try:
            new_item_price = input("Enter new unit price: ")
            new_item_price = int(sub(r"\D", "", str(new_item_price)))
            if new_item_price == 0:
                print("\nUnit price cannot be 0.")
                return
        except Exception:
            print("\nPlease re-enter unit price using only digits.")
            return        

        # Store new price and update total price
        self.data[item_name][1] = new_item_price
        self.data[item_name][2] = self.data[item_name][0] * self.data[item_name][1]

        # Display result
        print(f"\nUnit price for '{item_name}' has been changed to {Transaction.format_rupiah(new_item_price)}")
        item_qty, item_price, total_price = self.data[item_name]
        self.__show_trx(item_name, item_qty, item_price, total_price)


    def delete_item(self):
        """Deletes an item from the cart."""
        try:
            item_name = str(input("Which item do you want to remove?\n")).lower()
            item_name = sub(r"[^A-Za-z\s]", "", item_name).strip()

            if not item_name:
                print("\nYou are not allowed to leave this field empty.")
                return
            if item_name not in self.data.keys():
                print(f"\nItem '{item_name}' not found in your cart.")
                return
        except Exception:
            print("\nPlease re-enter item name using only letters.")
            return
        
        try:
            print(f"\nAre you sure you want to remove '{item_name}'?")
            confirmation = str(input("(yes / no)\n")).lower()
            confirmation = sub(r"[^A-Za-z\s]", "", confirmation).strip()
            if confirmation not in ["yes", "no"] or not confirmation:
                print("\nRequest cancelled. Please choose 'yes' or 'no'.")
                return
        except Exception:
            print("\nRequest cancelled. Please choose 'yes' or 'no'.")
            return

        if confirmation == "no":
            print("\nRequest cancelled.")
            return
        else:
            self.data.pop(item_name)
            # Display result
            print(f"\nItem '{item_name}' has been removed from your cart.")      
            self.__show_all_trx()


    def reset_transaction(self):
        """Clears all items in the cart."""
        if not self.data:
            print("\nYour cart is already empty.")
            return        
        try:
            print("Are you sure you want to clear all items in your cart?")
            print("\nIf you choose 'yes', all items will be permanently deleted.")
            confirmation = str(input("(yes / no)\n")).lower()
            confirmation = sub(r"[^A-Za-z\s]", "", confirmation).strip()
            if confirmation not in ["yes", "no"] or not confirmation:
                print("\nRequest cancelled. Please choose 'yes' or 'no'.")
                return
        except Exception:
            print("\nRequest cancelled. Please choose 'yes' or 'no'.")
            return

        if confirmation == "no":
            print("\nRequest cancelled.")
            return
        else:
            self.data.clear()
            # Display result
            print("\nYour cart has been successfully cleared.")      
            print("\nUse 'add_item()' to add new items.")


    def check_order(self):
            """Displays all current items in the cart."""
            if not self.data:
                print("\nYour cart is empty. Use 'add_item()' to add products.")
                return
            self.__show_all_trx()
            print("\nPlease check your cart before proceeding to checkout. Use 'update_item()' if needed.")
            print("\nIf everything looks good, use 'total_price()' to complete your purchase.")


    def total_price(self):
        """
        Calculates the total cost, applies discount, and processes payment confirmation.
        
        Rules:
            - total price > 500_000: 10% discount
            - total price > 300_000: 8% discount
            - total price > 200_000: 5% discount
        """
        try:
            self.__format_transaction()
            gross = sum(self.transaction["Total Price"])
            discount = 0

            if gross > 500_000:
                discount = 0.10
            elif gross > 300_000:
                discount = 0.08
            elif gross > 200_000:
                discount = 0.05
            else:
                discount = 0

            cut_price = gross * discount
            nett = gross - cut_price        
            if gross == 0 or nett == 0:
                print("\nYou must add items to the cart before checkout.")
                print("\nUse 'add_item()' to start shopping.")
                return

            payment_table = {
                "Total before discount": Transaction.format_rupiah(gross),
                "Discount": Transaction.format_rupiah(cut_price),
                "Total after discount": Transaction.format_rupiah(nett)
            }
            table_rows = [[key, val] for key, val in payment_table.items()]
            print(tabulate(table_rows, tablefmt="grid", colalign=("left", "right")))
        
        except Exception:
            print("\nYou must add items to the cart before checkout.")
            print("\nUse 'add_item()' to start shopping.")
            return
        
        try:
            print(f"\nProceed with payment of {Transaction.format_rupiah(nett)}?")
            confirmation = str(input("(yes / no)\n")).lower()
            confirmation = sub(r"[^A-Za-z\s]", "", confirmation).strip()
            if confirmation not in ["yes", "no"] or not confirmation:
                print("\nRequest cancelled. Please choose 'yes' or 'no'.")
                return
        except Exception:
            print("\nRequest cancelled. Please choose 'yes' or 'no'.")
            return
        
        if confirmation == "no":
            print("\nYou can use 'total_price()' again when you're ready to checkout.")
            return
        else:           
            Transaction.bookkeeping[self.customer_id] = self.transaction
            self.data.clear()
            self.transaction = {
                "No.": None,
                "Item": None,
                "Quantity": None,
                "Unit Price": None,
                "Total Price": None
            }
            print("\nThank you! Your payment was successful. Your order will be processed shortly.")
            return


    def __show_trx(self, item_name, item_qty, item_price, total_price):
        """Displays the details of a single transaction item."""
        row = [[item_name, item_qty, item_price, total_price]]
        header = [key for key in self.transaction.keys() if key != "No."]
        row_table = tabulate(row, headers=header, tablefmt="grid")
        print(" ")
        print(row_table)
        print("\nPlease review the item details above.")
        print("\nUse 'update_item()' if you need to make corrections.")


    def __format_transaction(self):
        """Private method to format self.data into self.transaction."""
        number, name, quantity, item_price, total_price = [], [], [], [], []

        for i, (key, val) in enumerate(self.data.items(), start=1):
            number.append(i)
            name.append(key)
            quantity.append(val[0])
            item_price.append(val[1])
            total_price.append(val[2])

        self.transaction = {
            "No.": number,
            "Item": name,
            "Quantity": quantity,
            "Unit Price": item_price,
            "Total Price": total_price
        }


    def __show_all_trx(self):
        """Private method to display all items in the transaction."""
        self.__format_transaction()
        trx_table = tabulate(self.transaction, headers="keys", tablefmt="grid")
        print("\nCurrent contents of your cart:\n")
        print(trx_table)


    @staticmethod
    def format_rupiah(amount):
        """
        Format a number into Indonesian Rupiah format.
        Example: 120000 -> 'Rp 120.000,00'
        """
        formatted = f"{amount:,.2f}"
        formatted = formatted.replace(",","X").replace(".",",").replace("X",".")
        return f"Rp {formatted}"