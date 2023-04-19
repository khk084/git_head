# 문제 (1)
su = 5
dan = 800
print('su 주소 :', id(su))
print('dan 주소 :', id(dan))
print('금액 =', int(su)*int(dan))

# 문제 (2)
word1 = input('첫번째 단어: ')
word2 = input('두번째 단어: ')
word3 = input('세번째 단어: ')
print('='*30)
abbr = word1[:1] + word2[:1] + word3[:1]
print('약자 :', abbr)

