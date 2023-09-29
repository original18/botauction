# botauction
Бот для участия в торгах на площадке росэлторг под Яндекс браузером.
Для работы необходимо:
- Создать файл .env с переменными:
url=https://etp.roseltorg.ru/
ex_path=Путь к склонированному репозиторию\\botauction\\project\\profile\\User Data
path_to_driver=Путь к склонированному репозиторию\\botauction\\project\\site_drivers\\yandex\\yandexdriver.exe
lk_main_page=https://etp.roseltorg.ru/supplier/auction/index
binary_location=C:\\Users\\{имя пользователя}\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe
executable_path=Путь к склонированному репозиторию\\botauction\\project\\site_drivers\\yandex\\yandexdriver.exe
login=ваш_логин
password=пароль
- скачать драйвер яндекс браузера в директорию проекта, адрес: Путь к склонированному репозиторию\\botauction\\project\\site_drivers\\yandex\\yandexdriver.exe
- сохранить расширения Вашего браузера со страницы браузера browser://extensions/,
в режиме разработчика упаковать расширение по пути: Путь к склонированному репозиторию\\botauction\\project\\site_drivers\\yandex\\
- установить виртуальное окружение командой python -m venv venv
- установить зависимости командой pip install -r requirements.txt

На данный момент бот заходит в ЛК в список заявок, функционал в процессе наполнения.

Технологии: Python 3.8.9, Selenium 