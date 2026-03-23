#step10_main.py

'''
현재 파일 즉 Step10_main.py 에서 run 해서 실행을 하면 

__name__ 은 "__main__" 이라는 문자열이 들어 있다.

따라서 __name__ 을 확인해 보면 해당 파일이 main 으로 실행되었는지 여부를 알 수 있다

다른 곳에서 import 했을때 실행되지 않는 코드 블럭을 만들때 사용한다.
'''

print(__name__)

"main 블럭": {
    "prefix": "ifmain",
    "body": [
        "if __name__ == \"__main__\" :",
        "    pass"
    ],
    "description": "main 블럭"
}


