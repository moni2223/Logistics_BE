# Уеб приложение за логистична компания
## Обзор
Този проект е уеб приложение за логистична компания, която управлява пратки, служители и клиенти. То е изградено с Python и Flask.

## Структура на проекта
```
logistics-company-backend
├── app
│   ├── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── customer.py
│   │   ├── employee.py
│   │   └── shipment.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── customer_routes.py
│   │   ├── employee_routes.py
│   │   └── shipment_routes.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── customer_service.py
│   │   ├── employee_service.py
│   │   └── shipment_service.py
│   └── templates
│       └── index.html
├── config.py
├── requirements.txt
└── README.md
```


## Стартиране
python app.py

## default IP = 127.0.0.1:5000
## Функции
- Управление на клиенти: Създаване, извличане, обновяване и изтриване на записи за клиенти.
- Управление на служители: Създаване, извличане, обновяване и изтриване на записи за служители.
- Управление на пратки: Създаване, извличане, обновяване и изтриване на записи за пратки.

## Използвани технологии
- Python
- Flask
- SQLAlchemy (for database management)
- HTML/CSS (for front-end templates)
