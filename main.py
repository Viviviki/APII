from typing import Union

import math

from random import *

from fastapi import FastAPI, Query, HTTPException, Path
import pyd

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about")
def show_about_me(a:int = None, b:int =6):

    return {
        'name':'Vika',
        'age':'20',
        'hobby':'cook',
        's': a+b,
    }

@app.get("/rnd")
def show_random():
    return {"number":randint(1,10)}

# gt >
# ge >=
# lt <
# le <=

@app.get("/t_square")
def calculate_treug(a:int=Query(gt=0), b:int=Query(gt=0), c:int=Query(gt=0)):

    return {
        's': math.sqrt((((a+b+c)/2)*((a+b+c)/2-a))*((a+b+c)/2-b)*((a+b+c)/2-c)),
        'p': (a+b+c)/2,
    }

# 2 задание

items = [
      {"id":1,"name":"Тостер","price":100,"description":"Тостер жарит классно"},
      {"id":2,"name":"Мультиварка","price":200,"description":"Мультиварка классно готовит"},
      {"id":3,"name":"Блендер","price":300,"description":"Блендер классно работает"},
      {"id":4,"name":"Аэрогриль","price":400,"description":"Аэрогриль классно работает"},
]

@app.get("/items")
def spis_tov(name:str=Query(None,min_length=2),
            min_price: float | None =Query(None,gt=0), 
            max_price: float | None =Query(None,gt=0),
            limit: int=Query(10,lt=100)):
                if max_price:
                    if max_price < min_price:
                          raise HTTPException(400,"Максимальная цена не может быть меньше минимальной цены")
                
                k = []
                for i in items:
                    if name:
                          if name != i["name"]:
                                continue
                    if min_price:
                          if min_price > i["price"]:
                                continue
                    if max_price:
                          if max_price < i["price"]:
                                continue
                    k.append(i)

                return k[:limit]


@app.get("/items/{item_id}")
def poluch_inf(item_id:int = Path(gt=0)):
    for i in items:
        if i["id"] == item_id:
            return i
    raise HTTPException(400, "Товар не найден.")

@app.post("/items")
def sozd_tov(item: pyd.Item):
    item = dict(item)
    id = items[-1]["id"]+1
    item["id"] = id 
    items.append(item)
    return item


                  