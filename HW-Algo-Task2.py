from collections import deque

def is_palindrome(text: str) -> bool:
    """
    Перевіряє, чи є рядок паліндромом, ігноруючи регістр та пробіли.
    Використовує deque з модуля collections.
    """
    # Очищуємо рядок: залишаємо лише літери та цифри, переводимо в нижній регістр
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())
    
    # Додаємо всі символи до двосторонньої черги
    char_deque = deque(cleaned_text)
    
    # Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
            
    return True

# Приклади перевірки роботи функції
if __name__ == "__main__":
    test_cases = [
        "А роза упала на лапу Азора",
        "Madam",
        "Я несу гусеня",
        "Аргентина манит манегра",
        "12321",
        "Де помити мопед?",
        "Хата на канатах"
    ]
    
    print("=== Перевірка рядків на паліндром ===")
    for test_str in test_cases:
        result = is_palindrome(test_str)
        print(f"Рядок: '{test_str}' -> Паліндром? {str(result).upper()}")