password-manager/
├── src/
│   ├── __init__.py
│   ├── main.py              # Точка входа
│   ├── crypto/              # Модуль шифрования
│   │   ├── __init__.py
│   │   ├── aes.py           # Реализация AES шифрования
│   │   └── key_derivation.py # Функции для PBKDF2
│   ├── storage/             # Работа с хранилищем
│   │   ├── __init__.py
│   │   ├── repository.py    # CRUD операции
│   │   └── models.py        # Модели данных
│   ├── ui/                  # Терминальный интерфейс
│   │   ├── __init__.py
│   │   ├── cli.py           # Основной CLI
│   │   ├── prompts.py       # Интерактивные подсказки
│   │   └── table_output.py  # Красивый вывод таблиц
│   └── utils/               # Вспомогательные функции
│       ├── __init__.py
│       ├── config.py        # Конфигурация приложения
│       └── helpers.py       # Разные хелперы
├── tests/                   # Тесты
│   ├── test_crypto.py
│   ├── test_storage.py
│   └── test_ui.py
├── requirements.txt         # Зависимости
├── LICENSE
└── README.md
