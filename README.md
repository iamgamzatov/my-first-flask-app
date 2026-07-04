# Flask Web Application on AWS Elastic Beanstalk 🚀

Простое веб-приложение (страница-визитка), разработанное на микрофреймворке Flask и успешно развернутое в облачной инфраструктуре Amazon Web Services (AWS).

## 🛠 Технологический стек
* **Backend:** Python, Flask
* **Frontend:** HTML5, CSS3 (Адаптивный дизайн, Glassmorphism эффект)
* **Cloud Infrastructure:** AWS Elastic Beanstalk, AWS EC2
* **IDE:** PyCharm

## 🌍 Живая демонстрация
Проект развернут и доступен в глобальной сети по адресу:
`http://my-first-flask-env.eba-npgrppep.eu-north-1.elasticbeanstalk.com`

## 📋 Особенности реализации для AWS
Для успешного деплоя на платформу AWS Elastic Beanstalk в проекте были выполнены следующие архитектурные требования:
1. Главный модуль переименован в `application.py`, а объект Flask инициализирован как `application = Flask(__name__)`.
2. Настроена автоматическая генерация зависимостей в файл `requirements.txt`.
3. Сформированы и настроены соответствующие IAM роли (`Service role` и `EC2 instance profile`) для управления ресурсами инстансов.
4. Исправлена проблема кодировки UTF-8 в заголовках HTML для корректного отображения кириллицы в облачной среде Linux.

## 🚀 Как запустить локально
1. Клонировать репозиторий.
2. Создать и активировать виртуальное окружение.
3. Установить зависимости: `pip install -r requirements.txt`
4. Запустить приложение: `python application.py`