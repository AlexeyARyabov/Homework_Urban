import inspect
class Myclass:
    count = 0
    my_str = 'string_1'
    my_tuple = (1, 3, 5, 7, 9)


    def my_func(self, args):
        my_list = []
        for word in args:
            my_list.append(len(word))
        return my_list

def introspection_info(obj):
    my_dict = {}
    my_dict.update({'type': type(obj)})
    methods = [m[0] for m in inspect.getmembers(obj, inspect.ismethod)]
    my_dict.update({'methods': methods})
    functions = [f[0] for f in inspect.getmembers(obj, inspect.isfunction)]
    my_dict.update({'functions': functions})
    module = [f[0] for f in inspect.getmembers(obj, inspect.ismodule)]
    my_dict.update({'module': module})
    '''attr = [a for a in inspect.getmembers_static(obj)]
    print(attr)'''
    print(my_dict)


some_list = ['alfa', 'beta', 'gamma', 'delta']
my_obj = Myclass()
introspection_info(my_obj)
introspection_info('obj')
introspection_info(56)
