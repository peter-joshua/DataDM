# DataDM
数据脱敏工具

功能：
	支持 固话、身份证、密码、自定义敏感关键字的脱敏
	
使用方法：
	
	在类或方法中使用@DataWM即可对传入方法中的参数进行脱敏处理

例：

```python
@DataWM
class Test:
    def test(self,val):
        return val
@DataWM
def test(val):
    return val
if __name__ == '__main__':
    result=test("1518330763")
    print(result)
    t=Test(123456)
    print(t)
结果：
	151*******3
	123**6
```

作用场景：

​	适用于对关键字进行脱敏处理，可自定义关键字
