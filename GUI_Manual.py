import tkinter as tk
from tkinter import scrolledtext


def display_user_manual():
    manual_window = tk.Tk()
    manual_window.title('EVPL Management System - User Manual')
    manual_window.geometry('600x400')
    manual_window.configure(bg="#fff")

    manual_text = scrolledtext.ScrolledText(manual_window, wrap=tk.WORD, width=70, height=20, font=('Arial', 12))
    manual_text.pack(padx=20, pady=20)

    manual_content = """
    EVPL Management System - User Manual

    1. Register an Account:
       - Go to "Sign Up" and enter your credentials.

    2. Log In and Seek Training:
       - Once logged in, seek training from your supervisor.

    3. Major Procedures:
       a. Adding Items to the Library's System:
          - Navigate to the corresponding section.
          - Provide item details and click "Add."

       b. Removing Items from the Library System:
          - Navigate to the corresponding section.
          - Enter the item details and click "Remove."

       c. Returning Items from Customers:
          - Visit "Return" in the Dashboard.
          - Input item and staff details.
          - Click "RETURN."

       d. Checking Out Items to Customers:
          - Visit "Checkout" in Books/Movies.
          - Enter item and customer details.
          - Click "CHECKOUT."

       e. Tracking Fees:
          - View and manage fees in the respective sections.

       f. Browsing the Library's System:
          - Explore available items using the "Search" feature.

       g. Adding Patrons:
          - To add a new patron, go to the "Add Patron" section.
          - Provide patron details and click "ADD PATRON."

       h. Adding Fees:
          - To add fees to a patron's account, visit the "Manage Fees" section.
          - Enter the patron's ID and fee amount, then click "ADD FEE."

       i. Paying Fees:
          - To pay fees, go to the "Manage Fees" section.
          - Enter the patron's ID and the amount to pay, then click "PAY FEE."

    For further assistance or information, please contact EVPL Library directly:
    - By phone: [800-444-3333]
    - In person: Visit during business hours.

    Thank you for using EVPL Management System!
    """

    manual_text.insert(tk.INSERT, manual_content)

    # Start the Tkinter event loop for this window
    manual_window.mainloop()

# Call the function to display the user manual
display_user_manual()
