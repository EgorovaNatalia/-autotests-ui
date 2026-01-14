from playwright.sync_api import sync_playwright
import time


def test_registration_button_state():
    with sync_playwright() as p:
        # Запускаем браузер
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            # Шаг 1: Открыть страницу регистрации
            print("📋 ШАГ 1: Открываю страницу регистрации...")
            time.sleep(1)
            page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

            # Ждем загрузки страницы
            print("⏳ Загружаю страницу...")
            page.wait_for_load_state('networkidle')
            time.sleep(3)
            print("✅ Страница загружена успешно!")
            time.sleep(1)

            # Отладочная информация - посмотрим что на странице
            print("\n🔍 Отладочная информация:")
            input_count = page.locator("input").count()
            print(f"Найдено полей ввода (input): {input_count}")

            # Выведем информацию о всех полях ввода
            for i in range(input_count):
                input_elem = page.locator("input").nth(i)
                input_type = input_elem.get_attribute("type") or "text"
                input_placeholder = input_elem.get_attribute("placeholder") or "нет"
                print(f"  Поле {i + 1}: type='{input_type}', placeholder='{input_placeholder}'")

            time.sleep(2)

            # Шаг 2: Проверить, что кнопка "Registration" находится в состоянии disabled
            print("\n📋 ШАГ 2: Проверяю, что кнопка 'Registration' disabled...")
            time.sleep(1)

            # Находим кнопку Registration
            print("🔍 Ищу кнопку Registration...")
            registration_button = page.locator("button:has-text('Registration')")

            # Проверяем, что кнопка существует
            if registration_button.count() == 0:
                print("❌ ОШИБКА: Кнопка 'Registration' не найдена")
                # Попробуем найти любую кнопку
                all_buttons = page.locator("button")
                print(f"Всего кнопок на странице: {all_buttons.count()}")
                for i in range(all_buttons.count()):
                    btn_text = all_buttons.nth(i).text_content()
                    print(f"  Кнопка {i + 1}: '{btn_text}'")
                return False

            print("✅ Кнопка найдена")
            time.sleep(1)

            # Проверяем состояние кнопки
            print("🔍 Проверяю состояние кнопки...")
            time.sleep(1)
            is_disabled = registration_button.is_disabled()

            if is_disabled:
                print("✅ Кнопка 'Registration' находится в состоянии disabled")
            else:
                print("❌ ОШИБКА: Кнопка 'Registration' должна быть disabled")
                return False

            time.sleep(2)

            # Шаг 3: Заполнить поле Email
            print("\n📋 ШАГ 3: Заполняю поле Email...")
            time.sleep(1)

            # Пробуем разные селекторы для поля Email
            email_selectors = [
                "input[type='email']",
                "input[placeholder*='email' i]",
                "input[placeholder*='Email' i]",
                "input[placeholder*='@' i]",
                "input:first-of-type",
                "input:nth-of-type(1)"
            ]

            email_field = None
            for selector in email_selectors:
                if page.locator(selector).count() > 0:
                    email_field = page.locator(selector).first
                    print(f"✅ Нашел поле Email с селектором: {selector}")
                    break

            if not email_field:
                print("❌ Не удалось найти поле Email")
                print("Пробую заполнить первое поле ввода...")
                email_field = page.locator("input").first

            print("⌨️  Ввожу email: user.name@gmail.com")
            email_field.fill("user.name@gmail.com")
            time.sleep(1)
            print("✅ Поле Email заполнено")
            time.sleep(1)

            # Шаг 4: Заполнить поле Username
            print("\n📋 ШАГ 4: Заполняю поле Username...")
            time.sleep(1)

            # Пробуем разные селекторы для поля Username
            username_selectors = [
                "input#username",
                "input[placeholder*='username' i]",
                "input[placeholder*='Username' i]",
                "input[placeholder*='user' i]",
                "input[placeholder*='name' i]",
                "input:nth-of-type(2)",
                "input:last-of-type"
            ]

            username_field = None
            for selector in username_selectors:
                if page.locator(selector).count() > 0:
                    username_field = page.locator(selector).first
                    print(f"✅ Нашел поле Username с селектором: {selector}")
                    break

            if not username_field:
                print("Пробую заполнить второе поле ввода...")
                if page.locator("input").count() >= 2:
                    username_field = page.locator("input").nth(1)
                else:
                    print("❌ Не удалось найти поле Username")
                    return False

            print("⌨️  Ввожу username: username")
            username_field.fill("username")
            time.sleep(1)
            print("✅ Поле Username заполнено")
            time.sleep(1)

            # Шаг 5: Заполнить поле Password
            print("\n📋 ШАГ 5: Заполняю поле Password...")
            time.sleep(1)

            # Пробуем разные селекторы для поля Password
            password_selectors = [
                "input[type='password']",
                "input[placeholder*='password' i]",
                "input[placeholder*='Password' i]",
                "input[placeholder*='пароль' i]",
                "input:last-of-type",
                "input:nth-of-type(3)"
            ]

            password_field = None
            for selector in password_selectors:
                if page.locator(selector).count() > 0:
                    password_field = page.locator(selector).first
                    print(f"✅ Нашел поле Password с селектором: {selector}")
                    break

            if not password_field:
                print("Пробую заполнить третье поле ввода...")
                if page.locator("input").count() >= 3:
                    password_field = page.locator("input").nth(2)
                else:
                    print("❌ Не удалось найти поле Password")
                    return False

            print("⌨️  Ввожу password: ••••••••")
            password_field.fill("password")
            time.sleep(1)
            print("✅ Поле Password заполнено")
            time.sleep(1)

            # Даем время для обновления состояния кнопки
            print("\n⏳ Ожидаю обновления состояния кнопки...")
            for i in range(3):
                print(f"⏰ {3 - i}...")
                time.sleep(1)

            # Шаг 6: Проверить, что кнопка "Registration" перешла в состояние enabled
            print("\n📋 ШАГ 6: Проверяю, что кнопка 'Registration' стала enabled...")
            time.sleep(1)
            print("🔍 Проверяю состояние кнопки...")
            time.sleep(1)
            is_enabled = not registration_button.is_disabled()

            if is_enabled:
                print("✅ Кнопка 'Registration' перешла в состояние enabled")
                time.sleep(1)
                print("\n🎉 ТЕСТ ПРОЙДЕН УСПЕШНО!")
                print("✨ Все шаги выполнены корректно!")
                return True
            else:
                print("❌ ОШИБКА: Кнопка 'Registration' должна быть enabled после заполнения формы")
                return False

        except Exception as e:
            print(f"❌ Произошла ошибка: {e}")
            # Сохраняем скриншот для отладки
            page.screenshot(path="error_screenshot.png")
            print("📸 Скриншот сохранен как 'error_screenshot.png'")
            return False
        finally:
            # Задержка перед закрытием браузера для наглядности
            print("\n⏳ Завершаю тест...")
            time.sleep(2)
            # Закрываем браузер
            browser.close()
            print("✅ Браузер закрыт")


if __name__ == "__main__":
    print("🚀 ЗАПУСК ТЕСТА: Проверка состояния кнопки Registration")
    print("=" * 60)
    start_time = time.time()
    success = test_registration_button_state()
    end_time = time.time()
    print("=" * 60)
    print(f"⏱️  Время выполнения: {end_time - start_time:.2f} секунд")
    if success:
        print("✅ Тест завершен успешно!")
    else:
        print("❌ Тест завершен с ошибками!")
    exit(0 if success else 1)