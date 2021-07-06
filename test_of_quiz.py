# def power_of_two():
#     user_input = input('Please enter a number: ')
#     try:
#         n = float(user_input)
#     except ValueError:
#         print('Your input was invalid.')
#     finally:
#         n_square = n ** 2
#         return n_square
# power_of_two()
#
#


# below is the AI 1.0 code, which works but cannot handle invalid input
# if the user input something other than an integer at first, the program will break due to a ValueError,
# caused by calling int() function on an non-integer input result
#
# Your task is to use the try-except-else-finally workflow to improve the existing code
# which can detect an invalid input in the beginning, and prints our an error message: ''
# then proceed to ask the user 'Do you want to play again? (y/N):' like the original function does
# below is the AI 1.0 code, which works but cannot handle invalid input
# if the user input something other than an integer at first, the program will break due to a ValueError,
# caused by calling int() function on an non-integer input result
#
# Your task is to use the try-except-else-finally workflow to improve the existing code
# which can detect an invalid input in the beginning, and prints our an error message: 'Please input integers only.'
# then proceed to ask the user 'Do you want to play again? (y/N):' like the original function does
def interact():
    while True:  # keep looping until user reach break statement
        try:
            user_input = int(input('Please input an integer:'))     # turn the user input into an integer
        except:
            print("Please input integers only.")
        else:
            print('{} is {}.'.format(user_input, 'even' if user_input % 2 == 0 else 'odd'))     # print out the message '{user_input} is {even/odd}.'
        finally:
            user_input = input('Do you want to play again? (y/N):')
            if user_input != 'y':   # quit if the user didn't input `y`
                print('Goodbye.')
                break   # break the while loop to quit




interact()

