# Singleton Design Pattern

# test
add a .replit file with the following lines
```
language = "python3"
run = "python -m unittest discover -v"
```
## decorator way of doing this
```
def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class MyClass(BaseClass):
    pass
```
*There are may other ways, refer to [here](https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python) in stackoverflow