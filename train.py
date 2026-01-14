# from playwright.sync_api import sync_playwright, expect
#
# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False)
#     page = browser.new_page()
#
#     # 1. Открыть страницу логина
#     page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
#
#     # 2. Найти элементы на странице логина
#     login_email_input = page.get_by_test_id('login-form-email-input').locator('input')
#     login_password_input = page.get_by_test_id('login-form-password-input').locator('input')
#     login_button = page.get_by_test_id('login-page-login-button')
#     registration_link = page.get_by_test_id("login-page-registration-link")
#
#     # 3. Проверить наличие элементов на странице логина
#     expect(login_email_input).to_be_visible()
#     expect(login_password_input).to_be_visible()
#     expect(login_button).to_be_visible()
#
#     # 4. Нажать на ссылку "Registration"
#     registration_link.click()
#
#     # 5. Найти элементы на странице регистрации
#     registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
#     registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
#     registration_button = page.get_by_test_id('registration-page-registration-button')
#
#     # 6. Проверить наличие элементов на странице регистрации
#     expect(registration_email_input).to_be_visible()
#     expect(registration_password_input).to_be_visible()
#     expect(registration_button).to_be_visible()

from playwright.sync_api import sync_playwright, expect  # Импорт Playwright для синхронного режима и проверки

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()  # Создаем новую страницу

    # Переходим на страницу авторизации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    # Проверяем, что кнопка Registration не активна
    login_button = page.get_by_test_id('registration-page-registration-button')
    expect(login_button).to_be_disabled()
 # Находим поле "Email" и заполняем его
    email_input = page.get_by_test_id('registrationogiform-email-input').locator('input')
    email_input.fill("user@gmail.com")
    # Находим поле "Username" и заполняем его
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    email_input.fill("username")
    # Находим поле "Password" и заполняем его
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")
login_button = page.get_by_test_id('registration-page-registration-button')
expect(login_button).not_to_be_disabled()







