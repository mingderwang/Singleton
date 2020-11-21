# Singleton Design Pattern
Global State and Singleton cause the code hard to test
[youtube](https://www.youtube.com/watch?v=-FRm3VPhseI&t=1747s)
To use DI as possible.
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

# try another way of implementation
https://github.com/tylerlaberge/PyPattyrn#singleton-pattern