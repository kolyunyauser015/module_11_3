import inspect


def introspection_info(obj):
    result = {}
    str_type = str(type(obj))
    result['type'] = str_type[str_type.find("'") + 1:str_type.rfind("'")]
    result['attributes'] = [n[0] for n in inspect.getmembers(obj)
                            if 'class' not in str(n[1])
                            if 'method' not in str(n[1])
                            ]
    result['method'] = [n[0] for n in inspect.getmembers(obj) if 'method' in str(n[1])]
    str_method = str(inspect.getmodule(introspection_info)).split()[1]
    result['module'] = str_method[str_method.find("'") + 1:str_method.rfind("'")]
    return result


number_info = introspection_info(42)
print(number_info)
