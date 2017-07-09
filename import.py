# -*- coding: utf-8 -*-
import peewee

# データベースを指定
db = peewee.SqliteDatabase("data.db")

# ユーザーモデルを定義
class Quote(peewee.Model):
    code = peewee.TextField()
    price = peewee.TextField()
    name = peewee.TextField()
    time= peewee.TextField()

    class Meta:
        database = db

# ユーザーテーブル作成
Quote.create_table()

# tsvファイルを一行ずつ読み込んでタブで分割し，それぞれをデータベースに登録
for line in open("quote.csv", "r"):
    (code, price, name, time) = tuple(line[:-1].split(","))
    if price.isdigit(): # 一行目のコメント対応．
        Quote.create(code = code,
                    price = price,
                    name = name,
                    time = time)

