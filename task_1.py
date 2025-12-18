# Лабораторная №1: Первичная инициализация
# Курс: Основы теории систем
# Студент: Зейнетдинов Альмир Маратович

def get_system_info():
    system_info = {
        "student_name": "Зейнетдинов Альмир Маратович",
        "academic_group": "ИВТИИбд-13",
        "github_link": "https://github.com/It-Is-Work"
    }
    return system_info

# Вывод информации для проверки
if __name__ == "__main__":
    info = get_system_info()
    print("Информация о системе:")
    for key, value in info.items():
        print(f"- {key}: {value}")
