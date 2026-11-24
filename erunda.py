

import pandas as pd




players = {
    "name":   ["Кхадгар", "Гаррош", "Вейл", "Тиранда", "Кэрн", "Джайна", "Сильвана", "Утер"],
    "level":  [72,        80,       35,      66,       48,      81,       77,        54],
    "klass":  ["Маг",     "Воин",   "Плут",  "Лучник", "Шаман",  "Маг",    "Лучник",  "Паладин"],
    "donate": [1200,      700,      150,     2100,     400,      3300,     2500,      900],
}

df = pd.DataFrame(players)
print("=== Задание 1: первые 2 строки ===")
print(df.head(2))





df.to_csv("dataset.csv", index=False, encoding="utf-8")


df2 = pd.read_csv("dataset.csv", encoding="utf-8")

print("\n=== Задание 2: info() о прочитанном датасете ===")
df2.info()






magi = df[(df["level"] > 50) & (df["klass"] == "Маг")]
print("\n=== Задание 3: маги выше 50 уровня ===")
print(magi)




top = df.sort_values("donate", ascending=False)
print("\n=== Задание 4: топ-3 по донатам ===")
print(top.head(3))





df["tax"] = df["donate"] * 0.13
print("\n=== Задание 5: колонка tax (13% от доната) ===")
print(df[["name", "donate", "tax"]])





avg = df.groupby("klass")["donate"].mean().sort_values(ascending=False)
print("\n=== Задание 6: средний донат по классам ===")
print(avg)





rich = df[df["level"] > 50].copy()
rich.to_csv("rich_players.csv", index=False, encoding="utf-8")
print("\n=== Задание 7 ===")
print(f"Сохранено: {len(rich)} строк")