original = input("문장 입력:" )
replace = input("교체 원본 단어: " )
want = input("교체 목적 단어: " )
oriIdx = original.find(replace)
frontStr = original[:oriIdx]
endStr = original[oriIdx + len(replace):]
result = frontStr + want  + endStr
print("완성 문장" + result)
