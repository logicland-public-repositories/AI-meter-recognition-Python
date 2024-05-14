# AI-meter-recognition

В цьому репозипорії зберігаються приклади з інтеграції сервісу Meter-recognition підприємства Logicland на мові програмування Python.
На цьому профілі у GitHub можна знайти приклад інтеграції на ще 3 мови: PHP, Java, C# 

Тут зберігається 2 файли написані на відповідній мові програмування:

1. record_recognition.py - це файл який реалізує функцію "record_recognition(string url, string login, string password, string image_path)" яка і виконує взаємодвію з нашим сервісом. Отож вам потрібно просто інтегрувати цей файл у структуру вашого проєкту і викликати функцію "record_recognition()" коли вам необхідно відправити фотографію на розпізнавання.
Аргумети функції:
    * url - посилання до нашого сервісу.
    * login - назва вашої ліцензії.
    * password - пароль до вашого акаунту (для цього сервісу він може відрізнятися від паролю до інших сервісів таких як "abon.com.ua" чи "Logic Land абонентська служба").
    * image_path - локальний шлях до місця збереження фотографії у файловій системі.

У випадку успішного розпізнавання фотографії "record_recognition()" поверне стрічку(String) у форматі JSON де показники будуть знаходитись за ключем "reading" та надійність цього значення за ключем "reliability"
	
2. example.py - це файл у якому зображений можливий метод використання функції "record_recognition()". Ми наполегливо рекомендуємо звернути увагу на ці приклади та на методи обробки вихідних данних. Кожен з прикладів можна запустити з консолі та перевірити їх роботу.
Для цього необхідно ввести команду:
```
python example.py -u <url with 'http://'> -l <your license> -p <your password> -i <local path to image>
```


Для роботи цього сервісу вам необхідно мати встановленим: ваше Python оточення, pip та Зовнішню бібліотеку requests. Якщо бібліотека requests у вас відсутня її слід встановити. Для цього рекомендовано скористатися командою:

```
pip install requests
```
