# Bulb simulator program

bulb_on = False  # The bulb is initially OFF

while True:
    print("\nBulb is currently", "ON 💡" if bulb_on else "OFF ⚫")
    print("1. Turn ON the bulb")
    print("2. Turn OFF the bulb")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        if bulb_on:
            print("The bulb is already ON.")
        else:
            bulb_on = True
            print("The bulb is now ON 💡")
    elif choice == '2':
        if not bulb_on:
            print("The bulb is already OFF.")
        else:
            bulb_on = False
            print("The bulb is now OFF ⚫")
    elif choice == '3':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
