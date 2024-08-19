def create_phone_number(n):
    # your code here
    first_batch_numbers = []
    for number in n[:3]:
        first_batch_numbers.append(str(number))
        first_batch = "".join(first_batch_numbers)
    second_batch_numbers = []
    for number in n[3:6]:
        second_batch_numbers.append(str(number))
        second_batch = "".append(second_batch_numbers)
    third_batch_numbers = []
    for number in n[6:]:
        third_batch_numbers.append(str(number))
        third_batch = "".join(first_batch_numbers)

    phone_number = f"({first_batch}) {second_batch}-{third_batch}"
    print(phone_number)


create_phone_number(([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print("Hello")
print("Success at the moment, I guess...")

# lorem ipsum sit amor doler 
# ilum emet imidor