from my_module2 import *
testA()

#　因为testB没有加紧my_module2模块中的__all__ 列表中，无法引用
testB()