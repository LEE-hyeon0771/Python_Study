student = ["아이유", "폴킴", "황인욱"]

student.append("청하")
print(f"(1)=> {student}")

index = student.index("폴킴")
student.insert(index,"폴킴")
print(f"(2)=> {student}")

count = student.count("폴킴")
print(f"(3)=> {count}")

student.pop(3)
print(f"(4)=> {student}")

student.pop(2)
print(f"(5)=> {student}")

student.sort(reverse=True)
print(f"(6)=> {student}")
