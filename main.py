import os
import json
import requests
import pandas as pd
from datetime import datetime

print("=== ЗАДАНИЕ 1: Первый GET-запрос ===")
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
print("Статус-код:", response.status_code)


if response.status_code == 200:
    data = response.json()
    
    print("\n=== ЗАДАНИЕ 2: Разбор ответа ===")
    print("Всего пользователей:", len(data))
  
    for user in data[:3]:
        print(user["name"], "-", user["email"])
    print("Город первого пользователя:", data[0]["address"]["city"])

    print("\n=== ЗАДАНИЕ 3: Данные API в DataFrame ===")
    df = pd.DataFrame(data)
    
    df = df[["id", "name", "username", "email", "phone", "website"]]
    print(df.head())

    print("\n=== ЗАДАНИЕ 4: Сохранение в CSV и JSON ===")
    os.makedirs("data", exist_ok=True) 
    
    df.to_csv("data/users.csv", index=False, encoding="utf-8")
    with open("data/users.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("Файлы сохранены:", os.listdir("data"))

    print("\n=== ЗАДАНИЕ 5: Грязные данные ===")
    dirty = [dict(u) for u in data] 
    dirty[0]["email"] = None        
    dirty.append(dirty[1])          
    
    df_dirty = pd.DataFrame(dirty)
    df_dirty = df_dirty[["id", "name", "email"]]
    
    print("Пропуски по колонкам:")
    print(df_dirty.isnull().sum())
    print("Найдено дубликатов:", df_dirty.duplicated().sum())

    print("\n=== ЗАДАНИЕ 6: Бэкап с датой в имени ===")
    def fetch_and_backup(url, folder="data"):
        """Делает GET-запрос и сохраняет ответ с датой в имени файла."""
        res = requests.get(url)
        if res.status_code != 200:
            print("Запрос не удался, код:", res.status_code)
            return None
        
        json_data = res.json()
        stamp = datetime.now().strftime("%Y-%m-%d")
        os.makedirs(folder, exist_ok=True)
        
        path = os.path.join(folder, f"users_{stamp}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)
            
        print("Бэкап сохранён:", path)
        return pd.DataFrame(json_data)

  
    df_backup = fetch_and_backup(url)
else:
    print("Не удалось получить данные. Код ошибки:", response.status_code)