# Chapter01-02
# 개발 가상환경 설정 테스트 코드

import pendulum
from datetime import datetime

pst = pendulum.timezone('America/Los_Angeles')
ist = pendulum.timezone('Asia/Seoul')

#타입 확인
print(type(pst))

#타임존 시간 출력
print('current date time in PST =',datetime.now(pst))
print('current date time in PST =',datetime.now(ist))

#타입 확인
print(type(ist))
