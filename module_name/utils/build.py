import importlib
import warnings
from typing import Callable
from module_name.utils.check_type import check_class_args


@check_class_args
class Builder:
    """
    @brief: 用于注册和获取类或者函数

    @example:
    >>> builder = Builder()
    >>> builder.register('model', MyModel)
    >>> builder.build('model', **kwargs)
    MyModel()
    """
    def __init__(self, name: str):
        self._name = name
        self._cache = {}
        self._index = {}

    def __repr__(self):
        string = f"Builder({self._name})\n"
        for i, (name, func_or_class) in enumerate(self._cache.items()):
            string += f"  {i}: {name}\n"
        return string

    def __contains__(self, name: str):
        return name in self._cache

    def get(self, name: str):
        """
        @brief: 根据name从builder中获取对应的类或者函数

        @param name: 名称
        @return: 类或者函数
        """
        if name not in self._cache:
            if name not in self._index:
                raise ValueError(f"{name} not registered in {self.name}")
            
            # try to lazy import
            module_path, module_name = self._index[name]
            # what if the module is not decorated?
            if module_name is None:
                module = importlib.import_module(module_path)
            elif module_name is not None:
                module = importlib.import_module(module_path)
                module = getattr(module, name)

            if name not in self._cache:
                warnings.warn(f"Module {module_path} not decorated")
                return module

        return self._cache[name]

    def build(self, name: str, **kwargs):
        """
        @brief: 根据name从builder中获取对应的类或者函数，并返回

        @param name: 名称
        @param kwargs: 参数
        @return: 类或者函数

        @example:
        >>> builder = Builder()
        >>> builder.register('model', MyModel)
        >>> builder.build('model', **kwargs)
        MyModel()
        """
        class_or_func = self.get(name)
        return class_or_func(**kwargs)

    def register(self, name: str, func_or_class: Callable = None, override: bool = False):
        """
        @brief: 将name对应的类或者函数注册到builder中

        @param name: 名称
        @param func_or_class: 类或者函数
        @param override: 是否覆盖已有的注册

        @example:
        >>> # 直接注册
        >>> builder = Builder()
        >>> builder.register('model', MyModel)
        >>> builder.build('model', **kwargs)
        >>> 
        >>> # 装饰器用法
        >>> @builder.register('model')
        >>> class MyModel:
        >>>     def __init__(self, **kwargs):
        >>>         pass
        >>> builder.build('model', **kwargs)
        """
        if name in self._cache and not override:
            raise ValueError(f"Model {name} already registered")

        if func_or_class is not None:
            self._cache[name] = func_or_class
        else:
            def decorator(func_or_class):
                self._cache[name] = func_or_class
                return func_or_class
            return decorator
    
    def register_index(self, name: str, path: str, module: str, override: bool=False):
        if name in self._index and not override:
            raise ValueError(f"{name} already registered")
        
        if path is None:
            raise ValueError(f"Path is None")

        self._index[name] = (path, module)

    @property
    def name(self):
        return self._name
