# 1. Получить случайного кота
import requests
URL = 'https://api.thecatapi.com/v1/'
API_KEY = 'live_4bwbA4U2ZzSAm9yM4Gd8mRRBwuuZxkOfNMxI3V75pTZix2dUC4SfsxWpEVs6lluo'
headers = {"x-api-key": API_KEY}
def show_favourite_cats():
    favourite_list_response = requests.get(f"{URL}favourites", headers=headers)
    print("Список избранных котов:")
    print(favourite_list_response.json())

cat_response = requests.get(f"{URL}images/search?limit=1", headers = headers)
print("Cat response: ", cat_response.json())
cat_data = cat_response.json()
cat_id = cat_data[0]['id'] # вытягиваю id из 2мерного списка
print(f"1. Получили кота с id = {cat_id}")


#  2. Проголосовать за кота
# проголосовать за определенного кота
vote_data = {'image_id': cat_id,
             "sub_id": "some info",
             "value": 1} # 1 - like, 0 - dislike
vote_response = requests.post(f"{URL}votes?sub_id={cat_id}", headers = headers, json = vote_data)
print(f"2. Голосование за кота с id = {cat_id}:")
print(vote_response.json())

# показать голоса
response1 = requests.get(f"{URL}votes", headers = headers)
print("Показать все голоса:")
print(response1.json())
print(response1.status_code)


# 3. Добавить кота в избранное
favourite_data = {
    "image_id":cat_id,
    "sub_id":"some data"
}
favourite_response = requests.post(f"{URL}favourites", headers = headers, json = favourite_data)
favourite_data = favourite_response.json()
favourite_id = favourite_data ['id'] # вытягиваю id из словаря
print(f"3. Добавление кота с favourite_id = {favourite_id} в избранное:")
print(favourite_data)
# Вывод списка избранных
show_favourite_cats()


# 4. Удаление кота из избранных:
delete_response = requests.delete(f"{URL}favourites/{favourite_id}", headers = headers)
if delete_response.status_code == 200:
    print(f"4. Кот с favourite_id = {favourite_id} удален из избранных")
else:
    print(f"4. Ошибка удаления из избранного: {delete_response.status_code}, {delete_response.text}")
# Вывод списка избранных
show_favourite_cats()





