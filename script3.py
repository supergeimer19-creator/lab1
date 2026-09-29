products = [
    {"name": "Ноутбук", "price": 25000.00, "quantity": 5},
    {"name": "Мишка", "price": 750.50, "quantity": 10},
    {"name": "Клавіатура", "price": 1200.00, "quantity": 8},
    {"name": "Навушники", "price": 1800.75, "quantity": 6},
    {"name": "Монітор", "price": 6500.00, "quantity": 4}
]

cart = []

ADMIN_LOGIN = "admin"
ADMIN_PASSWORD = "1234"

# Формат ціни
format_price = lambda price: f"{price:.2f} грн"


def show_catalog():
    print("\n========== КАТАЛОГ ==========")

    for i, product in enumerate(products, 1):
        print(
            f"{i}. {product['name']} | "
            f"{format_price(product['price'])} | "
            f"Залишок: {product['quantity']}"
        )


def show_cart():
    print("\n========== КОШИК ==========")

    if not cart:
        print("Кошик порожній.")
        return

    total = 0

    for i, item in enumerate(cart, 1):
        cost = item["price"] * item["quantity"]
        total += cost

        print(
            f"{i}. {item['name']} | "
            f"{item['quantity']} шт. | "
            f"{format_price(cost)}"
        )

    print(f"\nЗагальна сума: {format_price(total)}")


def add_to_cart():
    show_catalog()

    try:
        number = int(input("\nВведіть номер товару: "))

        if number < 1 or number > len(products):
            print("Такого товару немає.")
            return

        product = products[number - 1]

        if product["quantity"] <= 0:
            print("Цього товару немає в наявності.")
            return

        amount = int(input("Введіть кількість: "))

        if amount <= 0:
            print("Кількість повинна бути більше 0.")
            return

        if amount > product["quantity"]:
            print("Недостатньо товару на складі.")
            return

        existing = next(
            (item for item in cart if item["name"] == product["name"]),
            None
        )

        if existing:
            existing["quantity"] += amount
        else:
            cart.append({
                "name": product["name"],
                "price": product["price"],
                "quantity": amount
            })

        print("Товар додано до кошика.")

    except ValueError:
        print("Введіть правильне число.")


def remove_from_cart():
    show_cart()

    if not cart:
        return

    try:
        number = int(input("\nВведіть номер товару для видалення: "))

        if number < 1 or number > len(cart):
            print("Неправильний номер.")
            return

        removed = cart.pop(number - 1)

        print(f"Товар '{removed['name']}' видалено з кошика.")

    except ValueError:
        print("Введіть правильне число.")


def buy_products():
    if not cart:
        print("\nКошик порожній.")
        return

    show_cart()

    answer = input("\nПідтвердити покупку? (так/ні): ").lower()

    if answer != "так":
        print("Покупку скасовано.")
        return

    for item in cart:
        for product in products:
            if product["name"] == item["name"]:
                product["quantity"] -= item["quantity"]

    cart.clear()

    print("Покупку успішно здійснено!")


def admin_login():
    print("\n========== АДМІНІСТРАТОР ==========")

    login = input("Логін: ")
    password = input("Пароль: ")

    if login == ADMIN_LOGIN and password == ADMIN_PASSWORD:
        print("\nВхід успішний!")
        show_stock()
    else:
        print("Неправильний логін або пароль.")


def show_stock():
    print("\n========== ЗАЛИШКИ ==========")

    sorted_products = sorted(
        products,
        key=lambda product: product["name"]
    )

    for product in sorted_products:
        print(
            f"{product['name']} | "
            f"Ціна: {format_price(product['price'])} | "
            f"Залишок: {product['quantity']} шт."
        )


def main():
    while True:
        print("\n==============================")
        print("       МІНІ-МАГАЗИН")
        print("==============================")
        print("1. Переглянути каталог")
        print("2. Додати товар у кошик")
        print("3. Переглянути кошик")
        print("4. Видалити товар з кошика")
        print("5. Купити товари")
        print("6. Увійти як адміністратор")
        print("0. Вийти")

        choice = input("\nОберіть дію: ")

        if choice == "1":
            show_catalog()

        elif choice == "2":
            add_to_cart()

        elif choice == "3":
            show_cart()

        elif choice == "4":
            remove_from_cart()

        elif choice == "5":
            buy_products()

        elif choice == "6":
            admin_login()

        elif choice == "0":
            print("До побачення!")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
main()
