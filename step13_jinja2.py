# Step13_jinja2.py

"""
Template 문자열을 정의하고 어떤 데이터를 Template 문자열에 전달해서
결과 문자열을 얻어내는 작업을 jinja2 를 이용해서 테스트 해보자
 
설치 후에 사용해야 한다
pip install jinja2
"""
 
from jinja2 import Template
 
# 테스트용 template 을 만든다.
my_template = """
번호 : {{ num }}
이름 : {{ name }}
주소 : {{ addr }}
"""
 
# template 에 출력할 데이터를 준비한다.
mem1 = {"num": 1, "name": "김구라", "addr": "노량진"}
mem2 = {"num": 2, "name": "해골", "addr": "행신동"}
 
# Template 클래스의 생성자에 my_template 문자열을 넣어서 객체를 생성한다.
temp = Template(my_template)
 
# render() 에 데이터를 전달해서 결과 문자열을 얻는다.
result1 = temp.render(mem1)
print(result1)
 
result2 = temp.render(mem2)
print(result2)
 