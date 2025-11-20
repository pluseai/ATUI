# ATUI - Automated Testing UI

Проект автоматизации тестирования UI для сайта effective-mobile.ru с использованием Python, Playwright и Allure.

## Требования

- Python 3.10
- Git (для клонирования репозитория)
- Docker (опционально, для запуска в контейнере)
- Allure Commandline (для просмотра отчетов)

## Установка Allure Commandline

### Windows (через Scoop)
```bash
scoop install allure
```

### Windows (через Chocolatey)
```bash
choco install allure
```

### Linux/Mac
```bash
# Скачайте последнюю версию с https://github.com/allure-framework/allure2/releases
# Или используйте пакетный менеджер:
# macOS
brew install allure
# Linux (Ubuntu/Debian)
sudo apt-get install allure
```

## Установка и запуск

### Локальный запуск

1. Клонируйте репозиторий (или используйте существующий проект):
```bash
git clone <repository-url>
cd ATUI
```

Если репозиторий еще не инициализирован:
```bash
git init
git add .
git commit -m "Initial commit"
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
```

3. Активируйте виртуальное окружение:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Установите зависимости:
```bash
pip install -r requirements.txt
```

5. Установите браузеры Playwright:
```bash
playwright install chromium
playwright install-deps chromium
```

6. Запустите тесты:
```bash
pytest --alluredir=allure-results -v
```

7. Просмотрите отчет Allure:
```bash
allure serve allure-results
```

### Запуск через Docker

1. Соберите Docker-образ:
```bash
docker build -t atui-tests .
```

2. Запустите тесты в контейнере:
- Windows (PowerShell):
```bash
docker run --rm -v ${PWD}/allure-results:/app/allure-results atui-tests
```
- Linux/Mac:
```bash
docker run --rm -v $(pwd)/allure-results:/app/allure-results atui-tests
```

3. Просмотрите отчет Allure:
```bash
allure serve allure-results
```

## Структура проекта

```
ATUI/
├── pages/              # Page Object модели
│   ├── __init__.py
│   ├── base_page.py    # Базовый класс для всех страниц
│   └── main_page.py    # Главная страница
├── tests/              # Тесты
│   ├── __init__.py
│   └── test_main_page.py
├── conftest.py         # Фикстуры pytest
├── pytest.ini          # Конфигурация pytest
├── requirements.txt    # Зависимости проекта
├── Dockerfile          # Docker образ для запуска тестов
├── .gitignore          # Git ignore файл
└── README.md           # Документация
```

## Тесты

Проект содержит UI тесты для главной страницы effective-mobile.ru, проверяющие:
- Переход в раздел "О нас" (#about)
- Переход в раздел "Контакты" (#contact)
- Переход в раздел "Услуги" (#services)
- Переход в раздел "Вакансии" (#specializations)
- Переход в раздел "Отзывы" (#testimonials)

Каждый тест проверяет:
- Корректность URL с якорем после перехода
- Видимость соответствующего раздела на странице
- Успешность клика по навигационной ссылке

## Запуск конкретных тестов

Запуск только smoke тестов:
```bash
pytest -m smoke
```

Запуск только UI тестов:
```bash
pytest -m ui
```

Запуск конкретного теста:
```bash
pytest tests/test_main_page.py::TestMainPageNavigation::test_navigate_to_about_us
```

## Отчеты

Проект использует Allure для генерации подробных отчетов о выполнении тестов. Отчеты сохраняются в директории `allure-results` и могут быть просмотрены с помощью команды `allure serve allure-results`.

Для генерации статического HTML отчета:
```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## Технологии

- **Python 3.10** - язык программирования
- **Playwright 1.48.0** - фреймворк для автоматизации браузера
- **pytest 7.4.4** - фреймворк для тестирования
- **Allure 2.13.2** - система отчетности
- **Docker** - контейнеризация

## Паттерны и практики

- **Page Object Model** - для организации кода страниц
- **Allure отчетность** - для детальных отчетов
- **Фикстуры pytest** - для переиспользования кода
- **Маркеры pytest** - для категоризации тестов

## Проверка работоспособности

После установки всех зависимостей проверьте, что все работает:

```bash
pytest --version
playwright --version
allure --version
```

Все команды должны выполниться без ошибок.
