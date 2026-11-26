import os
import pandas as pd
import matplotlib.pyplot as plt


print("=== Задание 1: DataFrame с текстами ===")
data = {
    "text": [
        "Отличный сервис, всё работает быстро и без сбоев",
        "Ужасное приложение, постоянно зависает и вылетает!",
        "Поддержка ответила быстро, проблему решили за час",
        "Не рекомендую, потратил деньги зря",
        "Функционал удобный, интерфейс приятный, всё нравится",
        "Дизайн хороший, но тормозит на старом телефоне",
        "Полное разочарование, ничего не работает как надо",
        "Лучшее обновление за год, спасибо разработчикам!",
        "Всё супер, приложение стало заметно быстрее",
        "Служба поддержки на высоте, отвечает за пять минут",
    ]
}
df = pd.DataFrame(data)
print(df.head())


print("\n=== Задание 2: ручная разметка ===")

labels = [1, 0, 1, 0, 1, 1, 0, 1, 1, 1] 
df["label"] = labels
print(df[["text", "label"]].head())


print("\n=== Задание 3: длина текста ===")
df["text_length"] = df["text"].str.len()
print(df[["text", "text_length"]].head())


print("\n=== Задание 4: количество слов ===")
df["word_count"] = df["text"].str.split().str.len()
print(df[["text", "text_length", "word_count"]].head())


print("\n=== Задание 5: баланс классов ===")
balance = df["label"].value_counts()
print(balance)

total = len(df)
print(f"Позитивных: {int((df['label'] == 1).sum())} из {total} ({(df['label'] == 1).mean() * 100:.1f}%)")
print(f"Негативных: {int((df['label'] == 0).sum())} из {total} ({(df['label'] == 0).mean() * 100:.1f}%)")

print("\nВывод: Датасет слегка несбалансирован (70% позитива, 30% негатива).")
print("Это умеренный дисбаланс, приемлемый для учебы. При сильном перекосе (95/5)")
print("модель могла бы 'читерить', всегда предсказывая позитив.")


print("\n=== Задание 6: итоговый датасет ===")

final = df[["text_length", "word_count", "label"]].copy()
final.to_csv("labeled_dataset.csv", index=False, encoding="utf-8-sig")
print(final.head(10))
print("Файл labeled_dataset.csv сохранён.")


print("\n=== Задание 7 (бонус): признак 'есть восклицательный знак' ===")

df["has_exclamation"] = df["text"].str.contains("!").astype(int)
print(df[["text", "has_exclamation"]].head())


print("\n=== Задание 8 (бонус): график баланса классов ===")
os.makedirs("images", exist_ok=True)

balance.plot(kind="bar", color=["#4C72B0", "#C44E52"])
plt.title("Баланс классов")
plt.xlabel("Метка (1 - позитив, 0 - негатив)")
plt.ylabel("Количество отзывов")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("images/classes.png", dpi=150)
plt.show()
plt.close()
print("График сохранён в images/classes.png")