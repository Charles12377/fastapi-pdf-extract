def get_full_name(first_name:str,last_name:str):
    full_name=first_name.title() + ' ' +last_name.title()
    return full_name

print(get_full_name('kobe','bryant'))

#简单类型
def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_e

#typing模块
from typing import Any

def get_function(data:Any):
    print(data)

get_function(5)

#泛型类型
"""
def process_items(items:list[str]):
    for item in items:
        print(item.title())

process_items(['a','b','c','d'])
"""

#元组和集合
"""
def process_items(items_t:tuple[int,int,str],items_s:set[bytes]):
    return items_t,items_s

print(process_items((1,2,'a'),{b'hello', b'world'}))
"""

#字典
"""
def process_items(prices:dict[str,float]):
    for item_name,item_price in prices.items():
        print(item_name)
        print(item_price)

process_items({'apple':5.0})
"""

#联合类型
def process_item(item:int|str):
    print(item)

process_item(3)
process_item('eeee')

#可能为None
def say_hi(name:str|None=None):
    if name is not None:
        print(f'Hey {name}!')
    else:
        print('Hello World')

say_hi('john')
say_hi()

#类作为变量的类型
class Person:
    def __init__(self,name:str):
        self.name=name

def get_person_name(one_person:Person):
    return one_person.name

print(get_person_name(Person('johnn')))

#带元数据注解的类型提示
from typing import Annotated

def say_hello(name:Annotated[str,"this is just metadata"]) -> str:
    return f"Hello {name}"

print(say_hello(222))