# from playwright.sync_api import sync_playwright, expect  # Импорт Playwright для синхронного режима и проверки
#
# # Запуск Playwright в синхронном режиме
# with sync_playwright() as playwright:
#     # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
#     browser = playwright.chromium.launch(headless=False)
#     page = browser.new_page()  # Создаем новую страницу
#
#     # Переходим на страницу авторизации
#     page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
#
#     # Находим поле "Email" и заполняем его
#     email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
#     email_input.fill("user.name@gmail.com")
#     # Находим поле "Username" и заполняем его
#     username = page.locator('//div[@data-testid="login-form-username-input"]//div//input')
#     username_input.fill("username")
#     # Находим поле "Password" и заполняем его
#     password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
#     password_input.fill("password")
#     registration_button = page.get_by_test_id('registration-page-registration-button')
#     registration_button.click()
#     # Ожидание редиректа и проверка заголовка
#     page.wait_for_url("**/dashboard")
#     expect(page.get_by_test_id('dashboard-page-title')).to_have_text("Dashboard")
#
#     print("✅ Тест пройден успешно!")
#
#     # Пауза на 5 секунд, чтобы увидеть результат
#     page.wait_for_timeout(5000)

# from playwright.sync_api import sync_playwright
#
# from playwright_2registration import registration_button
# from playwright_authorization import browser, email_input
# from train import username_input



from playwright.sync_api import sync_playwright
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path='browser-state.json')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless= False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

page.wait_for_timeout(50000)









