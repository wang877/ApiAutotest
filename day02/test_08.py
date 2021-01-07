'''
fixture 带参数

测试搜索功能：
    要搜索的字符串: 大写、小写、大小写混写
    搜索的方向： 向上、向下
    是否区分大小写： 是、否
'''
import pytest

# 要搜索的字符串：大写、小写、大小写混写
@pytest.fixture(params=["hello", "APPLE", "HelloWorld"])
def search_str(request):
    return request.param

#搜索的方向： 向上、向下
@pytest.fixture(params=["向上", "向下"])
def search_fx(request):
    return request.param

# 是否区分大小写： 是、否
@pytest.fixture(params=["是", "否"])
def search_dx(request):
    return request.param

# 用例中多个fixture带参数时，参数之间是全组合的关系，共执行3*2*2=12次
def test_search(search_str,search_fx,search_dx):
    print(f"搜索的字符串为：{search_str}, 搜索的方向：{search_fx}, 区分大小写：{search_dx} ")