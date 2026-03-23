#step13_example.py

from jinja2 import Template

# 1. 테스트용 데이터 준비 (info 딕셔너리)
info:dict = {
    "num": 1,
    "name": "김구라",
    "body": {
        "height": 180,
        "weight": 80
    },
    "hobby": ["피아노", "당구", "프로그래밍"]
}

# 2. 출력 형식을 담은 템플릿 정의
my_template = '''
    번호: {{ num }}
    이름: {{ name }}
    키: {{ body.height }} cm
    몸무게: {{ body.weight }} kg
    취미:
    {% for item in hobby %}
        - {{ item }}
    {% endfor %}
'''

# 3. 템플릿 객체 생성 및 렌더링
temp: Template = Template(my_template)
result: str = temp.render(**info)

# 4. 결과 출력
print(result)

