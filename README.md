```bash
Implementação de projeto em python utilizando a Clean Architecture 
```
```bash
├── src
│   ├── data
│   │   ├── find_pet
│   │   │   ├── find.py
│   │   │   ├── find_test.py
│   │   │   └── __init__.py
│   │   ├── find_user
│   │   │   ├── find.py
│   │   │   ├── find_test.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── interfaces
│   │   │   ├── __init__.py
│   │   │   ├── pet_repository_interface.py
│   │   │   └── user_repository_interface.py
│   │   ├── register_pet
│   │   │   ├── __init__.py
│   │   │   ├── register.py
│   │   │   └── register_test.py
│   │   ├── register_user
│   │   │   ├── __init__.py
│   │   │   ├── register.py
│   │   │   └── register_test.py
│   │   └── test
│   │       ├── __init__.py
│   │       ├── find_user_spy.py
│   │       ├── find_pet_spy.py
│   │       ├── register_pet_spy.py
│   │       └── register_user_spy.py
│   ├── domain
│   │   ├── __init__.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── pets.py
│   │   │   └── users.py
│   │   ├── test
│   │   │   ├── __init__.py
│   │   │   ├── mock_pets.py
│   │   │   └── mock_users.py
│   │   └── use_cases
│   │       ├── __init__.py
│   │       ├── find_pet.py
│   │       ├── find_user.py
│   │       ├── register_pet.py
│   │       └── register_user.py
│   ├── infra
│   │   ├── config
│   │   │   ├── db_base.py
│   │   │   ├── db_config.py
│   │   │   └── __init__.py
│   │   ├── entities
│   │   │   ├── __init__.py
│   │   │   ├── pets.py
│   │   │   └── users.py
│   │   ├── __init__.py
│   │   ├── repo
│   │   │   ├── __init__.py
│   │   │   ├── fake.py
│   │   │   ├── pet_repository.py
│   │   │   ├── pet_repository_test.py
│   │   │   ├── user_repository.py
│   │   │   └── user_repository_test.py
│   │   └── test
│   │       ├── __init__.py
│   │       ├── pet_repository_spy.py
│   │       └── user_repository_spy.py
│   ├── __init__.py
│   ├── main
│   │   ├── adapter
│   │   │   ├── api_adapter.py
│   │   │   └── __init__.py
│   │   ├── composer
│   │   │   ├── __init__.py
│   │   │   ├── find_pet_composite.py
│   │   │   ├── find_user_composite.py
│   │   │   ├── register_pet_composite.py
│   │   │   └── register_user_composite.py
│   │   ├── configs
│   │   │   ├── app.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── interface
│   │   │   ├── __init__.py
│   │   │   ├── route.py
│   │   │   ├── validation_composite.py
│   │   │   └── validation_interface.py
│   │   ├── routes
│   │   │   ├── api_route.py
│   │   │   └── __init__.py
│   │   └── validations
│   │       ├── find_validations.py
│   │       └── __init__.py
│   └── presenters
│       ├── controllers
│       │   ├── __init__.py
│       │   ├── find_pet_controller.py
│       │   ├── find_pet_controller_test.py
│       │   ├── find_user_controller.py
│       │   ├── find_user_controller_test.py
│       │   ├── register_pet_controller.py
│       │   ├── register_pet_controller_test.py
│       │   ├── register_user_controller.py
│       │   └── register_user_controller_test.py
│       ├── erros
│       │   ├── http_errors.py
│       │   └── __init__.py
│       ├── helpers
│       │   ├── http_models.py
│       │   └── __init__.py
│       └── __init__.py
└── requirements.txt
└── run.py
└── storage.db
```
