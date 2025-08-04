def countdown(start_number, final_message):
    start_number += 1
    countdown = start_number
    while countdown != 0:
        countdown -= 1
        print(countdown)
    if countdown == 0:
        print(final_message)


if __name__ == "__main__":
    start_number = int(input("Enter your starting number: "))
    final_message = input("Enter your final message: ")
    if start_number < 0:
        print("Please enter a positive integer.")
    else:
        countdown(start_number, final_message)
