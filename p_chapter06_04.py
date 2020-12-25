# Chapter06-04
# Futures 동시성
# 비동기 작업 실행
# 동기 : A -> B A가 끝날때까지 B가 실행되지 않음
# 비동기 : A -> B A가 시작하고, B도 같이 시작함
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> (File)Network I/O 관련 작업 -> 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상

# python 3.2 이전
# import threading
# import multiprocessing

# 해당 코딩들이 어려워 rapping -> Future
# future : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.futures
# 1. 멀티스레딩/멀티프로세싱 API 통일 -> 매우 사용하기 쉬움
# 2. 실행 중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념


# 2가지 패턴 실습
# concurrent.futures 사용법1 : Map
# concurrent.futures 사용법2 : wait, as_completed

# GIL : Global Interpreter Lock -> 두 개 이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스 하는 경우 문제점을 방지하기 위해 GIL 실행
# 즉 Resource 전체에 락이 걸린다. -> Context Switch(문맥 교환) 비용

# GIL 우회 : multiprocessing 사용, CPython

import os
import time
from concurrent import futures
# futures 안에 threading, multiprocessing 이 들어있음

work_list = [10000,100000,1000000,10000000]
# 순차적으로 하면 10000 끝나고 100000, 1000000 순으로 진행됌

# 동시성 합계 계산 메인 함수
# 누적 합계 함수(Generator)
def sum_generator(n):
    return sum(n for n in range(1,n+1))
    # 이 함수가 동시에 4개가 실행되게끔 해야함

def main():
    # Worker Count
    worker = min(10,len(work_list))

    # Start Time
    start_time = time.time()

    # 작업 내용, ProcessPoolExecutor - ThreadPoolExecutor로 전환 가 (매우 간단)
    with futures.ProcessPoolExecutor() as excutor:
        result = excutor.map(sum_generator, work_list)
        # map -> 작업순서를 유지하고, 즉시 실행

    # end Time
    end_time = time.time() - start_time

    # 출력 포맷
    msg = '\n Result -> {} Time : {:.2f}s'

    #최종 결과 출력
    print(msg.format(list(result),end_time))

# 실행
if __name__ == '__main__':
    main()
