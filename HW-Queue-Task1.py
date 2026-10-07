import queue
import time
import uuid

# Створити чергу заявок
request_queue = queue.Queue()

def generate_request():
    """Генерує нову заявку з унікальним номером і додає її до черги."""
    request_id = str(uuid.uuid4())[:8]  # Генеруємо короткий унікальний ідентифікатор
    request_name = f"Заявка #{request_id}"
    request_queue.put(request_name)
    print(f"[ГЕНЕРАЦІЯ] {request_name} додано до черги.")

def process_request():
    """Видаляє заявку з черги та імітує її обробку."""
    if not request_queue.empty():
        request_name = request_queue.get()
        print(f"[ОБРОБКА] Початок обробки {request_name}...")
        time.sleep(1.5)  # Імітація часу на виконання завдання
        print(f"[УСПІХ] {request_name} успішно оброблена.")
        request_queue.task_done()
    else:
        print("[ІНФО] Черга порожня. Немає заявок для обробки.")

if __name__ == "__main__":
    print("=== Система обробки заявок запущена ===")
    print("Натисніть Ctrl + C для виходу з програми.\n")
    
    try:
        while True:
            # Імітуємо надходження нових заявок та їх обробку
            generate_request()
            process_request()
            print("-" * 40)
            time.sleep(1)  # Пауза між циклами
    except KeyboardInterrupt:
        print("\nРоботу програми завершено користувачем.")
