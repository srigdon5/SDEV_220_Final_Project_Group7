"~~~~~~~~~~Things to Do~~~~~~~~~~~~"

"""
1. GUI_Patron
    *The Calendar combobox.get() functions and the date_var are coming up as undefined
    *Unsure as to the cause

2. GUI_Return
    * Search boxes need refined
        * Does Item ID refer the actual Item ID in the database, or does it refer to the
           IBSN/ISAN? Or maybe the Title?
        * Staff ID is not required since a staff member would more than likely be logging
           into the master system to access this program
        * The return_item() has item_id and patron_id for their arguments. Outside of the
           obvious issue with relating item_id between GUI and backend, how would we obtain the patron_id with our given boxes?
        * Are we going to be committing to calculating fees for condition? We have function
           add_fee() in the library_back.py, but I wouldn't want to add it if we aren't.

3. GUI_Books
    * I added a series of if statments that will suspend the validation checks depending on 
       there is value in the variable. This way we can search without needing exact info. However, running the search with nothing but a book title prompts the error
       "TypeError: 'method' object is not iterable". I need assistance in retifying.

4. GUI_Checkout (Optional)
    * The window successfully checks out items and places them under a patron's list, but the 
       function doesn't check to see if the patron already has 3 items out. It requires an 
       honest input. Database doesn't update with limit being reached either. Currently the database shows that Bob Ross has four items checked out
    * Query doesn't check to see if item_id exists.

"""