# Pet Ware - Backend

## Commands

#### Initial project

- Run project

```js

docker-compose up

```

#### Migrations - Alembic

- Generate migration from model to Alembic 🛠

```js

docker-compose run fastapi-service /bin/sh -c "alembic revision --autogenerate"

```

- Apply migration to DB 💨

```js

docker-compose run fastapi-service /bin/sh -c "alembic upgrade head"

```

- Revert last migration ❌

```js

docker-compose run fastapi-service /bin/sh -c "alembic downgrade -1"

```