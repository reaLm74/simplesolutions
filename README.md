# Тестовое задание для Python-разработчика simplesolutions

## Технологии

- Python
- Django
- Django REST
- Stripe
- Docker

## Как запустить проект:

### Клонирование репозитория:
```sh
git clone https://github.com/realn74/simplesolutions
```
<details> <summary> Шаблон наполнения .env </summary>

```
YOUR_DOMAIN='http://127.0.0.1:8000'

STRIPE_PUBLIC_KEY='pk_test_51gdsghdshshgsGigsgsgsdgsdgsgslw1m16Cub2e3mCxylmeDi6s00Xj82A0UM'
STRIPE_SECRET_KEY='sk_test_51OI8jWGgsggsdf3CtBDxHgigAPTWcl3UCshTbUtAxiTjHrif3DnZA00lOVaDLo5'
```
</details>

### Запуск приложения в Docker
Собрать контейнер
```
docker-compose build
```
Запустить docker-compose.yaml
```
docker-compose up
```

Проект запущен и доступен: [http://127.0.0.1:8080/](http://127.0.0.1:8080/)

Пересборка контейнеров
```
docker-compose up -d --build
```
Удалить контейнеры
```
docker-compose down
```

### Админка

  ```
  http://127.0.0.1:8080/admin/
  ```

### Главная страница

  ```
  http://127.0.0.1:8080/index/
  ```
