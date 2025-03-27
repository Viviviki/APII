from typing import Union

import math

from random import *

from fastapi import FastAPI, Query

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