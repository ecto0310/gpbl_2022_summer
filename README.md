# c_meet

## DBの構築
```sh
docker compose exec server python3 manage.py init_db
```

## 起動
```sh
docker compose up -d
```
- logを見ながら作業したい時は
```sh
docker compose up
```
