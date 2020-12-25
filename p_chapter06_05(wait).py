# Chapter06-05
# Futures 동시성
# 비동기 작업 실행
# 동기 : A -> B A가 끝날때까지 B가 실행되지 않음
# 비동기 : A -> B A가 시작하고, B도 같이 시작함
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> (File)Network I/O 관련 작업 -> 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상

# python 3.2 이전에는 아래 두가지 사용
# import threading
# import multiprocessing

# 해당 코딩들이 어려워 rapping -> Future
# future : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.futures
# 1. 멀티스레딩/멀티프로세싱 API 통일 -> 매우 사용하기 쉬움
# 2. 실행 중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념


# 2가지 패턴 실습
# concurrent.futures 사용법1 : Map - 각 Worker들이 작업이 끝나거나, Error등으로 인해 정지할 수 있음.
# concurrent.futures 사용법2 : wait, as_completed

# GIL : Global Interpreter Lock -> 두 개 이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스 하는 경우 문제점을 방지하기 위해 GIL 실행
# 즉 Resource 전체에 락이 걸린다. -> Context Switch(문맥 교환) 비용

# GIL 우회 : multiprocessing 사용, CPython

import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed
# futures 안에 threading, multiprocessing 이 들어있음

work_list = [10000,100000,10000000,1000000000]
# 순차적으로 하면 10000 끝나고 100000, 1000000 순으로 진행됌

# 동시성 합계 계산 메인 함수
# 누적 합계 함수(Generator)
def sum_generator(n):
    return sum(n for n in range(1,n+1))
    # 이 함수가 동시에 4개가 실행되게끔 해야함

# wait
# as_completed
def main():
    # Worker Count
    worker = min(10,len(work_list))

    # Start Time
    start_time = time.time()
    # Futures
    future_list = []

    # 작업 내용, ProcessPoolExecutor - ThreadPoolExecutor로 전환 가능
    with ProcessPoolExecutor() as excutor:
        for work in work_list:
            # future 반환
            future = excutor.submit(sum_generator, work)
            # scheduling
            future_list.append(future)
            # scheduling 확인
            print('Scheduled for {} : {}'.format(work, future))
            print()

        # Wait 결과 출력
        result = wait(future_list, timeout=7) # 7초 까지만 진행하고 그 이후론 실패로 간주
        # 성공
        print('Completed Task : ' + str(result.done))
        # 실패
        print('Pending ones after waitting for 7 sec : '+str(result.not_done))
        # 결과 값 출력
        print([future.result() for future in result.done])
    # end Time
    end_time = time.time() - start_time

    # 출력 포맷
    msg = '\nTime : {:.2f}s'

    #최종 시간 출력
    print(msg.format(end_time))

# 실행
if __name__ == '__main__':
    main()
