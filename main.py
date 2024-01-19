import requests


def get_kurs(api_key, val_kor, suma, val_vych):
    url = (f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{val_kor}')
    try:
        response = requests.get(url)
        if response.status_code == 200:
            resp = response.json()
            kof = resp['conversion_rates'][val_vych]
            rezult = kof * suma
            print(f"{suma} {val_kor} = {rezult}")

        else:
            print(f"Помилка отримання відповіді. Код помилки - {response.status_code}")

    except Exception as e:
        print(f"Виникла помилка: {e}")


api_key = 'e1cbc8528df8fe34212e78cf'
val_kor = input("Введіть валюту, яку хочете обміняти:")
suma = int(input("Введіть суму, яку хочете обміняти:"))
val_vych = input("Введіть валюту, на яку хочете обміняти свої кошти:")

get_kurs(api_key, val_kor, suma, val_vych)
