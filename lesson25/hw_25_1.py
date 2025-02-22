# 1. Получить 80 пост
import requests
URL = 'https://jsonplaceholder.typicode.com/'
post_response = requests.get(f"{URL}posts/80")
print("1. Получить 80 пост:", post_response.json())

# 2. Получить все комментарии к  посту 60
comments_response = requests.get(f"{URL}comments?postId=60")
print("2. Получить все комментарии к  посту 60:", comments_response.json())

#3. Создать новый пост
new_post_data = {
        "userId": "007",
        "title": "new added post",
        "body": "this is a new added post 101"
}
headers = {"Content-Type": "application/json"}
create_response = requests.post(f"{URL}posts", headers = headers, json=new_post_data)
print("3. Создать новый пост: ", create_response.json())
print(create_response.json())

#Получить созданный пост
get_new_post_response = requests.get(f"{URL}posts/101")
print("Вывести созданный пост:", get_new_post_response.text) #выводит пустой словарь?????????????????это норм?????

#4. Удалить пост 7
delete_response = requests.delete(f"{URL}posts/7")
print("4. Удалить пост 7", delete_response.json()) #выведет  (пустые скобки)
print(delete_response.status_code)

