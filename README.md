# Super Cashier: Python Self-Service Checkout System  

**Super Cashier** is a Python-based self-service cashier system designed for online supermarket shopping. The program allows customers to manage their shopping cart (add, update, or remove items) and checkout seamlessly with automated discounts. It also keeps a transaction record that can later be used by supermarket management for bookkeeping purposes and popular item analytics.


---

## Objectives

### Learning Objectives
- Demonstrate proficiency in **Object-Oriented Programming (OOP)** with Python.
- Apply clean coding principles according to **PEP8 guidelines**.
- Utilize **exception handling** and **input sanitization** via `try-except` and `re.sub`.
- Strengthen data manipulation skills using **dictionaries** and **lists**.
- Practice building **interactive CLI tools** for real-world scenarios.


### Program Objectives (Features)

#### User Features
- `add_item()` — Add an item (name, quantity, unit price) to the cart.
- `update_item()` — Update item name, quantity, or price interactively.
- `delete_item()` — Delete a specific item from the cart.
- `reset_transaction()` — Clear the cart entirely.
- `check_order()` — View cart contents in a clean tabulated format.
- `total_price()` — Checkout process with automatic discount calculation:
  - > Rp 200.000 → 5% discount  
  - > Rp 300.000 → 8% discount  
  - > Rp 500.000 → 10% discount  

#### Bookkeeping Features
- `bookkeeping` — Class-level dictionary that records all successful transactions.

---

## Tools & Libraries
- Python 3 — Core programming language
- `tabulate` — For displaying clean and readable tables in CLI
- `re` — For regex sanitization of user inputs

---

## Program Structure

### 1. `cashier.py`
This is the main script containing the core implementation of the `Transaction` class with all user-facing methods. Each customer session is an object of this class, with methods to manage their cart and complete the transaction.

### 2. `test_case_supercashier.ipynb` 
A Jupyter Notebook file containing real-world test scenarios to demonstrate and validate each feature of the `Transaction` class. It covers all customer actions from item input to checkout, and also includes corner cases and validation handling.

---

## How It Works (User Journey)

### Program Flow

1. To access the features, user firstly creates a new transaction instance using the `Transaction()` class.
   ![image](https://github.com/user-attachments/assets/458adbfe-fdea-48d9-bd19-8e8860d06187)
   
2. User can repeatedly input items using `add_item()` (with name, quantity, and price). Each time an item is successfully added, the screen will display a table and a message as below.
   ![image](https://github.com/user-attachments/assets/67b40e17-eab1-4e83-a23b-83b34a0fcecc)

3. If needed, user may correct typos using `update_item()`. This allows user to update name, quantity, or price of an existing item. Internally, it will dispatch update based on selected feature using three private methods: `__update_item_name()`, `__update_item_qty()`, or `__update_item_price()`.
   ![image](https://github.com/user-attachments/assets/142a1728-9440-41ce-9bb5-7e8c54cd753c)

4. User can remove an item from the cart with `delete_item()` or clear all items with `reset_transaction()`.
   ![image](https://github.com/user-attachments/assets/f5cb6d34-eba2-4cc2-b60a-38c92bbbadc2)

5. To verify the cart before checkout, `check_order()` will display the current basket.
   ![image](https://github.com/user-attachments/assets/be7507fe-83f4-4cd5-a7ed-200d67621567)

6. Final price is calculated and discounts applied through `total_price()`, followed by user confirmation.
   ![image](https://github.com/user-attachments/assets/7fdbe14a-0ba4-491e-8ccc-6756930eacf0)

7. The final transaction is stored in a global `bookkeeping` dictionary for store records.


### Key Design Choices
- **Input Sanitization:** Regex removes unwanted characters (e.g., numbers from item names).
- **Interactive Prompts:** Users are guided via terminal on-screen prompts instead of direct parameter inputs.
- **Private Methods:** Internal methods like __update_item_name() handle specific updates under update_item().

---

## Performance

### Test Cases
**Test 1: Add Items**

Add 3 items to the cart:
- Fried Chicken (Qty: 2, Price: Rp 20,000)
- Toothpaste (Qty: 3, Price: Rp 15,000)
- Instant Noodle (Qty: 5, Price: Rp 3,000)
![image](https://github.com/user-attachments/assets/5d4d9bd1-7201-4cae-bd46-2f8521374337)

**Test 2: Delete Item**

Remove Toothpaste using `delete_item()`.
![image](https://github.com/user-attachments/assets/7121fb38-9757-41fc-acbf-755542c6a81a)

**Test 3: Reset Cart**

Clear all items with `reset_transaction()`.
![image](https://github.com/user-attachments/assets/c1fd3653-a117-47d4-a9b0-a66b2d92b949)

**Test 4: Full Workflow**

1. Re-add previous items plus a Toy Car for Rp 200,000.
2. Correct a misspelled item name (*Fried Chicken → Grilled Chicken*) via `update_item()`.
3. Checkout with `total_price()` (discount auto-applied: Rp 285,000 total).
4. Verify the transaction record in `Transaction.bookkeeping`.
![image](https://github.com/user-attachments/assets/ebcc0f6d-4d59-441d-b733-ef6af60a4579)

### Edge Cases Handled
- **Direct Checkout:** Blocked if cart is empty.
- **Typos:** Non-alphabetic characters are stripped from item names; the same also for non-digits from item quantities and prices.
- **Case Sensitivity:** "*Chicken*" and "*chicken*" are treated as the same item.
- **Zero Values:** Quantity/price cannot be 0.

---

## How to Run the Program Yourself

1. Download both files:
   - `cashier.py`
   - `test_case_supercashier.ipynb`
2. Place both files in the **same local directory**.
3. Open `test_case_supercashier.ipynb` in **Jupyter Notebook** or **VS Code with Jupyter support**.
4. Run the notebook cells step by step to explore and test all features.
5. Follow on-screen prompts interactively to complete transactions.

---

## Acknowledgement
This project was created as part of the final assignment for the **Basic Python Programming & Python for Software Engineering** class at **Sekolah Data Pacmann**, under the **Bright Future Program (BFP)** initiative.

---

## Authorship
**S.B. Suryo Buwono**
(c) 2025 – All Rights Reserved
