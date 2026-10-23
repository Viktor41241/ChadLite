products = [
    {"id": 1, "name": "Мышь", "category": "Переферия", "price": 1500, "quantity": 10},
    {"id": 2, "name": "Клавиатура", "category": "Переферия", "price": 3500, "quantity": 3},
    {"id": 3, "name": "Монитор", "category": "Дисплеи", "price": 25000, "quantity": 5},
    {"id": 4, "name": "Наушники", "category": "Аудио", "price": 4500, "quantity": 0},
    {"id": 5, "name": "Веб-камера", "category": "Видео", "price": 3000, "quantity": 2},
    {"id": 6, "name": "Микрофон", "category": "Аудио", "price": 6000, "quantity": 7},
    {"id": 7, "name": "Колонки", "category": "Аудио", "price": 2500, "quantity": 4},
    {"id": 8, "name": "USB-флешка", "category": "Переферия", "price": 800, "quantity": 20},
]

def search_product(serch_result):
    for product in products:
        if product['name'] == serch_result:
            print((product))

def main():
    print("0 - функция 1")
    func_start = input('Вызов функции: ')
    if func_start == '0':
        search_product(input('Введите название товара: '))

main()

def input_int(massage):
    while True:
        try:
            number = int(input(massage))
            return number 
        except ValueError:
            print("Ошибка! Введите целое число.")

def show_product(product):
    print(
      f'ID: {product["id"]} | '
      f'Название: {product["name"]} | '
      f'Категория: {product["category"]} | '
      f'Цена: {product["price"]} | ' 
      f'Количество: {product["quantity"]} | ' 
    )            
    