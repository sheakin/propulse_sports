from django import template

register = template.Library()

@register.filter(name='splitter')
def splitter(list_data, chunk_size):
    arr = []
    i = 0
    for data in list_data:
        arr.append(data)
        i=i+1
        if i==chunk_size:
            yield arr
            i=0
            arr=[]
    if arr:
        yield arr
