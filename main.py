import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


print("=== Задание 2: Подготовка данных для регрессии ===")
np.random.seed(42)  
hours = np.random.uniform(0, 12, 30)  
grade = 40 + 5 * hours + np.random.normal(0, 5, 30)  

X = hours.reshape(-1, 1)  
y = grade                 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("Обучающая выборка:", X_train.shape)
print("Тестовая выборка:", X_test.shape)


print("\n=== Задание 3: Обучение модели ===")
model = LinearRegression()
model.fit(X_train, y_train)

print("Наклон (k):", round(model.coef_[0], 2))
print("Свободный член (b):", round(model.intercept_, 2))


print("\n=== Задание 4: Предсказания ===")
y_pred = model.predict(X_test)
print("Предсказания (первые 3):", np.round(y_pred[:3], 1))
print("Реальные (первые 3):     ", np.round(y_test[:3], 1))

new_hours = np.array([[6.0]])  
prediction = model.predict(new_hours)[0]
print("За 6 часов модель обещает:", round(prediction, 1))



print("\n=== Задание 5: Оценка MAE ===")
mae = mean_absolute_error(y_test, y_pred)
print("MAE:", round(mae, 2))
print(f"Модель ошибается в среднем на {round(mae, 1)} балла.")




print("\n=== Задание 6: Классификация kNN ===")
np.random.seed(42)
n = 30
age = np.random.randint(14, 60, n)
minutes = np.random.randint(10, 400, n)


buy = ((age < 35) & (minutes > 120)).astype(int) 

flip = np.random.choice(n, 3, replace=False)
buy[flip] = 1 - buy[flip]

df = pd.DataFrame({"age": age, "minutes": minutes, "bought": buy})
print("Баланс классов:", df["bought"].value_counts().to_dict())

Xk = df[["age", "minutes"]]
yk = df["bought"]

Xk_train, Xk_test, yk_train, yk_test = train_test_split(
    Xk, yk, test_size=0.3, random_state=42, stratify=yk
)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(Xk_train, yk_train)
pred = knn.predict(Xk_test)

print("Accuracy kNN:", round(accuracy_score(yk_test, pred), 2))

new_user = pd.DataFrame({"age": [25], "minutes": [300]})
print("Новый пользователь 25 лет, 300 минут -> купит?", knn.predict(new_user)[0])


print("\n=== Задание 7: Построение графика ===")
os.makedirs("images", exist_ok=True)

plt.figure(figsize=(7, 4))
plt.scatter(X_train[:, 0], y_train, label="Обучающие данные", alpha=0.7)
plt.scatter(X_test[:, 0], y_test, color="red", label="Тестовые данные", alpha=0.7)


xs = np.linspace(0, 12, 100)
plt.plot(xs, model.intercept_ + model.coef_[0] * xs, "g-", label="Линия регрессии")

plt.xlabel("Часы подготовки")
plt.ylabel("Оценка")
plt.title("Линейная регрессия: часы -> оценка")
plt.legend()
plt.grid(alpha=0.3)
plt.savefig("images/regression.png", dpi=150, bbox_inches="tight")
plt.show()
plt.close()
print("График сохранён в images/regression.png")