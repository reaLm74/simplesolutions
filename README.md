# Simplesolutions

## Технологии

- Python
- Django
- Django REST
- Stripe
- Docker

<details> 
<summary> Поставленная задача </summary>

Реализовать Django + Stripe API бэкенд со следующим функционалом и
условиями:

- Django Модель Item с полями (name, description, price)
- API с двумя методами:
    - GET /buy/{id}, c помощью которого можно получить Stripe Session Id для
      оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью
      python библиотеки stripe должен выполняться запрос
      stripe.checkout.Session.create(...)
      и полученный session.id выдаваться в результате запроса
    - GET /item/{id}, c помощью которого можно получить простейшую HTML
      страницу, на которой будет информация о выбранном Item и кнопка Buy. По
      нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение
      session_id и далее с помощью JS библиотеки Stripe происходить редирект на
      Checkout форму stripe.redirectToCheckout(sessionId=session_id)

Бонусные задачи:

- Запуск используя Docker
- Использование environment variables
- Просмотр Django Моделей в Django Admin панели
- Запуск приложения на удаленном сервере, доступном для тестирования
- Модель Order, в которой можно объединить несколько Item и сделать платёж в
  Stripe на содержимое Order c общей стоимостью всех Items
- Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в
  зависимости от валюты выбранного товара предлагать оплату в соответствующей
  валюте

</details>

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
