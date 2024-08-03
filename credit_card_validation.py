

def valid_credit_card(number):
    number_str = str(number) #convert number to string
    length = len(number_str)

    if length<13 or length>16: #checking if card number have a valid length
        return False

    if not ((number_str.startswith("4") and length == 13) or
            (number_str.startswith("5") and length == 13) or
            (number_str.startswith("37") and length == 16) or
            (number_str.startswith("6") and length == 15)):
        return False

    sum_of_digits = 0

    for i in range(length):
        digit = int(number_str[i])

        if i % 2 == 1:
            digit *= 2

            if digit > 9:
                digit = sum(int(d) for d in str(digit))

        sum_of_digits += digit

    return sum_of_digits % 10 == 0




card_number = input("Enter the credit card number: ")

if valid_credit_card(card_number):
    print("CREDIT CARD NUMBER IS VALID")
else:
    print("CREDIT CARD IS INVALID")