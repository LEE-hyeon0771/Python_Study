
import time

input("엔터를 누르고 10초를 셉니다.")

start = time.time()

input("10초 후에 다시 엔터를 누르세요.")
end = time.time()

et = end - start
print(f"당신이  실제 시간은 : {et:.2f}초")
print(f"오차는 {abs(et - 10):.10f}초")

