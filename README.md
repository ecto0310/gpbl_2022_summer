# c_meet

## DBの構築
```sh
docker compose exec server python3 manage.py init_db
```

## デモデータの追加
```sh
docker compose exec server python3 manage.py demo_db
```

## グループの作成
```sh
docker compose exec server python3 manage.py create_group -d yyyy-mm-dd
```


## 起動
```sh
docker compose up -d
```
- logを見ながら作業したい時は
```sh
docker compose up
```
