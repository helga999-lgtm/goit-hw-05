import sys
import os

def parse_log_line(line: str) -> dict:
    """Парсить один рядок логу у словник."""
    parts = line.split(' ', 3)
    if len(parts) < 4:
        return {}
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2].upper(),
        'message': parts[3].strip()
    }

def load_logs(file_path: str) -> list:
    """Завантажує логи з файлу, ігноруючи порожні або некоректні рядки."""
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{file_path}' не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Відбулася помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    """Фільтрує список логів за вказаним рівнем (case-insensitive)."""
    # Використання елемента функціонального програмування: filter
    return list(filter(lambda log: log['level'] == level.upper(), logs))

def count_logs_by_level(logs: list) -> dict:
    """Підраховує кількість входжень кожного рівня логування."""
    counts = {}
    for log in logs:
        level = log['level']
        counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts: dict):
    """Виводить результати підрахунку у вигляді таблиці."""
    print(f"{'Рівень логування':<17} | {'Кількість':<10}")
    print("-" * 18 + "|" + "-" * 11)
    # Сортуємо для стабільного виводу
    for level in sorted(counts.keys()):
        print(f"{level:<17} | {counts[level]:<10}")

def main():
    # Перевірка наявності хоча б одного аргументу (шлях до файлу)
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_файлу> [рівень_логування]")
        return

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)

    # Виведення загальної статистики
    display_log_counts(counts)

    # Якщо вказано другий аргумент (рівень логування)
    if len(sys.argv) > 2:
        search_level = sys.argv[2].upper()
        filtered = filter_logs_by_level(logs, search_level)
        
        print(f"\nДеталі логів для рівня '{search_level}':")
        for log in filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()