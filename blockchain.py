# Initializing blockchain list
blockchain = []
open_transactions = []

def get_Last_blockchain_value():
    """Return the last value of the current blockchain."""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_Transaction_value(transaction_Value, last_transaction_Value):
    """Append the last value and a new value to the blockchain list

    Arguments:
        value:      the amount that should be added.
        last_value: the last blockchain value (default value is [1]). 
     """
    if last_transaction_Value == None:
        last_transaction_Value = [1]
    blockchain.append([last_transaction_Value, transaction_Value])

def mine_block():
    pass

def get_Transaction_Value():
    """Return the input of the user as a float."""
    return float(input('Enter the amount please: '))

def get_user_choice():
    """Return the input selection [1 or 2] of the user as a string """
    user_Input = input("Your choice: ")
    return user_Input

def print_blockchain_elements():
    #Outputting block elements contained in the blockchain
    for block in blockchain:
            print('\nOutputting block')
            print(block)
    else:
        print('-' * 20)


def verify_chain():
    """Verify that the blockchain has not been altered. """
    is_Valid = True

    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_Valid = True
        else:
            is_Valid = False
    return is_Valid

#Get all transaction input values and add them to the blockchain list
waiting_for_input = True
while waiting_for_input:
    print('')
    #Selection interface
    print("Please choose:")
    print("1. Add new transaction value")
    print("2. Display blockchain blocks")
    print("4. Manipulate blockchain")
    print('3. Exit')
    print('-' * 20)

    user_Choice = get_user_choice()

    if user_Choice == '1':
        #Get transaction input and add to the blockchain list
        tx_value = get_Transaction_Value()
        add_Transaction_value(last_transaction_Value= get_Last_blockchain_value(), transaction_Value= tx_value)
        print('-' * 20)
    

    elif user_Choice == '2':
        print_blockchain_elements()
        
    elif user_Choice == '3':
        #Exit the loop
        print('-' * 20)
        waiting_for_input = False


    elif user_Choice == '4':
        if len(blockchain) >= 1:
            blockchain[0] = [2]

    else:
        print("Invalid input!\nPlease choose a value from the interface!")
    
    if not verify_chain():
        print("\nInvalid blockchain!")
        print_blockchain_elements()
        break
else:
    print("\nBlockchain list")
    print(blockchain)
    print("Done!\n")



    



