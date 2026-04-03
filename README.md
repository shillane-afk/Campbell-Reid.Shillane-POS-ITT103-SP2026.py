Authors: Oshane Crawford, Shillane Campbell-Reid

Date Created: April 3, 2026

Course: ITT103

GitHub Public URL to Code: https://github.com/ocrawford-tech/Crawford.Oshane-POS-ITT103-SP2026.git

                         :https://github.com/shillane-afk/Campbell-Reid.Shillane-POS-ITT103-SP2026.py?tab=readme-ov-                             file#readme
  

PROGRAM OVERVIEW
  
The Point of Sale (POS) system, designed for Best Buy Retail Store, enables cashiers to manage customer transactions efficiently. The system facilitates product selection, cart management (add and remove items), cart review, and transaction completion.



FEATURES OF THE CODE

The system manages product listings with prices and stock, enabling users to add items to a cart while preventing over-ordering. Cart contents, subtotals, discounts for large purchases, and applicable taxes are displayed. The system processes payments, calculates change, generates receipts, and updates stock levels post-transaction, while also monitoring and reporting low stock situations. It supports handling several transactions sequentially.



HOW TO RUN THE PROGRAM

To execute the Python program, first verify that Python is installed on the system. Next, open a terminal or command prompt and navigate to the directory containing the "AgileArchitects-POS-ITT103-SP2026.py" file. Finally, run the program by entering the command "python AgileArchitects-POS-ITT103-SP2026.py" and adhere to the on-screen menu options.



ASSUMPTIONS

The cashier is expected to accurately input product codes upon system prompt. Payment submissions will be restricted to numeric values only. System use will be limited to trained cashiers within a controlled operational environment.



LIMITATIONS

The program exhibits several limitations in its design and functionality. Notably, the absence of a persistent database results in data loss upon program termination. Furthermore, the console-based interface lacks graphical elements, and the system does not incorporate user authentication measures. Error handling is also limited, potentially leading to instability when encountering unexpected inputs.



MODIFICATIONS / DESIGN NOTES

The e-commerce application employs lists for managing products and cart items, alongside functions for enhanced modularity. Input validation is implemented using try/except blocks, ensuring data integrity. Discounts and tax calculations are incorporated to provide accurate pricing. Receipt formatting is included for clear transaction records. Stock update logic is executed post-checkout to maintain accurate inventory levels.


I CERTIFY THAT I HAVE NOT GIVEN OR RECEIVED ANY UNAUTHORIZED ASSISTANCE
ON THIS ASSIGNMENT.
