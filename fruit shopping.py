print('Welcome to Grace Grocery Store....')
stock = {'mango': {'price': 50, 'qty': 100},
         'carrot': {'price': 100, 'qty': 100},
         'pawpaw': {'price': 200, 'qty': 100},
         'pineapple': {'price': 100, 'qty': 100},
         'apple': {'price': 200, 'qty': 100},
         'cucumber': {'price': 200, 'qty': 100}}

wallet = 5000
cart = {}
trial = 0

while True:
    total = 0
    option = input('0: Exit\n1: Add to Cart\n2: Remove from Cart\n3: Show Cart\n4: Checkout\nEnter option:')

    if option == '0':
        print('Thank you for your patronage....')
        break


    elif option == '1':
        while True:
            for product in stock:
                print(product, stock[product]['price'], stock[product]['qty'])

            item = input('Enter item(Press C to cancel):').lower()
            if item == 'c':
                break
            else:
                if item in stock:
                    if item in cart:
                        qty = int(input('How many more?: '))
                        cart[item]['qty'] += qty
                        cost = stock[item]['price'] * qty
                        cart[item]['cost'] += cost
                        stock[item]['qty'] -= qty
                    else:
                        qty = int(input("How many?: "))
                        cost = stock[item]['price'] * qty
                        cart[item] = {'cost': cost, 'qty': qty}
                        stock[item]['qty'] -= qty
                else:
                    print('Item not in stock! Try again')
            break

    elif option == '2':
        item = input('Enter item you want to remove:').lower()

        if item in cart:
            qty = int(input('How many would you like to remove? '))

            rem = cart[item]['qty'] - qty
            if rem > 0:
                cart[item]['qty'] = rem
                cost = stock[item]['price'] * qty
                cart[item]['cost'] -= cost
                stock[item]['qty'] += qty
            elif rem == 0:
                stock[item]['qty'] += qty
                del cart[item]
            else:
                print("You don't have that much in your cart")
        else:
            print('Item not in cart!')



    elif option == '3':
        if len(cart) == 0:
            print('Cart is empty!')
        else:
            for item in cart:
                print(item, cart[item]['qty'])
                total += cart[item]['cost']

        print(f'Total {total}')


    elif option == '4':
        for item in cart:
            print(item, cart[item]['qty'])
            total += cart[item]['cost']

        print(f'Total {total}')

        if total > wallet:
            print('Insufficient funds...\n remove some items in cart')
        else:
            print('Wallet: {}\nBalance: {}'.format(wallet, (wallet - total)))
            cart.clear()

    else:
        print('Invalid option...')
        trial += 1
    if trial == 3:
        print('You have reached maximum amount of attempts(3)')
        break