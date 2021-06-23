List = ['Gene','Lex','Infini','Lambor','Linc']
print(f"(현재 차종: {List}")

List.append("Merce")
print(f"(1) Merce 차종 추가: {List}")

List.remove("Lex")
print(f"(2) Lex 차종 단종: {List}")

List.append("Gene 2019version")
print(f"(3) Gene 2019년형 추가: {List}")

print(f"(4) 두 번째로부터 네 번째 개발한 모델: {List[1:4:1]}")
