import datetime
import random


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method Get current url (Метод получения ссылки)"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("current url " + get_url)

    """Method assert word (Метод сравнения текста)"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print(f"Value: {value_word} == {word.text} PASSED")

    """Method get screenshot (Метод скриншота)"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d-%H.%M.%S')
        name_screenshot = 'screenshot ' + now_date + '.png'
        self.driver.save_screenshot(
            './screen/' + name_screenshot)

    """Method assert url (Метод сравнения ссылки)"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method generate random phone (Метод генерации номера телефона)"""

    def generate_random_phone_number(self):
        area_code = random.randint(100, 999)
        first_part = random.randint(100, 999)
        second_part = random.randint(1000, 9999)
        return f"8({area_code}){first_part}-{second_part}"

    """Method generate random name (Метод генерации имени)"""

    def generate_random_name(self):
        names = ["Иван", "Петр", "Мария", "Анна", "Сергей", "Ольга", "Александр", "Екатерина", "Дмитрий", "Наталья"]
        name = random.choice(names)
        return name
