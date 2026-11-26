import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams["font.family"] = "DejaVu Sans"

os.makedirs("images", exist_ok=True)

print("Строим график 1...")
days = ["Пн", "Вт", "Ср", "Чт", "Пт"]
work = [2, 3.5, 7, 5, 9]

plt.plot(days, work, "o-", color="steelblue", label="Сложность задач")
plt.xlabel("День недели")
plt.ylabel("Сложность")
plt.title("Сложность задач по дням")

plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("images/plot1.png", dpi=150)
plt.show()
plt.close() 







print("Строим график 2...")
np.random.seed(42)
level = np.random.randint(1, 100, 60)
donates = level * 15 + np.random.normal(0, 200, 60)

plt.scatter(level, donates, alpha=0.6, color="seagreen")
plt.xlabel("Уровень игрока")
plt.ylabel("Сумма донатов, руб.")
plt.title("Зависимость донатов от уровня")
plt.grid(True, alpha=0.3)
plt.savefig("images/scatter_donates.png", dpi=150)
plt.show()
plt.close()







print("Строим график 3...")
classes = ["Воин", "Маг", "Стрелок", "Паладин"]
counts = [14, 9, 11, 6]

plt.bar(classes, counts, color=["#4C72B0", "#DD8452", "#55A868", "#C44E52"])
plt.xlabel("Класс персонажа")
plt.ylabel("Количество игроков")
plt.title("Распределение игроков по классам")
plt.savefig("images/bar_classes.png", dpi=150)
plt.show()
plt.close()






print("Строим график 4...")
np.random.seed(7)
times = np.random.normal(loc=120, scale=25, size=500)

plt.hist(times, bins=30, color="steelblue", edgecolor="black")
plt.xlabel("Время выполнения, мс")
plt.ylabel("Количество задач")
plt.title("Распределение времени выполнения задач")
plt.savefig("images/hist_times.png", dpi=150)
plt.show()
plt.close()

print(f"Статистика времени: Среднее = {times.mean():.1f}, Мин = {times.min():.1f}, Макс = {times.max():.1f}")






print("Строим график 5...")
np.random.seed(42)
x = np.arange(1, 21)
y = x * 3 + np.random.normal(0, 10, 20)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(x, y, "o-")
axes[0].set_title("Линейный график")
axes[0].set_xlabel("Время")
axes[0].set_ylabel("Значение")

axes[1].scatter(x, y, color="crimson")
axes[1].set_title("Точечная диаграмма")
axes[1].set_xlabel("Время")
axes[1].set_ylabel("Значение")

plt.tight_layout()
plt.savefig("images/subplots.png", dpi=150)
plt.show()
plt.close()







print("Строим бонусный график из Pandas...")
try:
    
    
    
    
    df = pd.read_csv("dataset.csv")
    counts_pd = df["klass"].value_counts()
    
    plt.bar(counts_pd.index, counts_pd.values, color="slateblue")
    plt.title("Игроки по классам (из Pandas)")
    plt.xlabel("Класс")
    plt.ylabel("Количество")
    plt.savefig("images/pandas_bar.png", dpi=150)
    plt.show()
    plt.close()
    print("Бонусный график сохранен!")
except FileNotFoundError:print("Внимание: файл dataset.csv не найден. Бонусное задание пропущено.")

print("\nВсе графики построены и сохранены в папку 'images'!")