# n = int(input("n = ")) # 숫자를 입력 

# a = 0 # a 를 0 으로 둔다. 

# for i in range(1,n+1): # 1 부터 입력 한 숫자+1 까지 반복
#   if n % i == 0:  #만약 n 이 i 로 나누었을때 나머지가 0 일때
#     a += 1 # a 를 하나씩 추가 한다. 

# if a == 2: # 만약 a 의 값이 2개 가 나왔을 때 
#   print("True") # True 로 출력
# else: # 값이 2개 이상 이면
#   print("False") # False 로 출력 



##########################################################

def search4vowels(word:str) -> set:
  ''' return a boolean based on any vowels found '''
  vowels = set('aeiou')
  return vowels.intersection(set(word))
  ''' 결과값으로 셋이 나올수도 있어요!!! '''

help(search4vowels)

search4vowels('hitch-hiker')
search4vowels('galaxy')
search4vowels('life, the universe and everything')
search4vowels('sky')

##############################################

l = list()
l

d = dict()
d

s = set()
s

t = tuple()
t

################################################

def search4vowels(phrase:str) -> set:
  ''' Return any vowels found in a supplied phrase. '''
  vowels = set('aeiou')
  return vowels.intersection(set(phrase))
  ''' 결과값으로 셋이 나올수도 있어요!!! '''

def search4letters(phrase:str, letters:str) -> set:
  """ Return a set of the 'letters' found in 'phrase'. """
  return set(letters).intersection(set(phrase))

search4letters('hitch-hiker', 'aeiou')
search4letters('galaxy', 'xyz')
search4letters('life, the universe, and everything','o')

################################################

def search4letters(phrase:str, letters:str=('aeiou')) -> set:   # 만약 2번째 인수가 없으면 'aeiou' 로 찾아라. 있으면 그 인수에 맞게 찾아라.
  """ Return a set of the 'letters' found in 'phrase'. """
  return set(letters).intersection(set(phrase))

search4letters('hitch-hiker')
search4letters(letters='xyz', phrase='galaxy') # 포지션 상관 없이 xyz 를 letter로 표기 하고, galaxy 를 phrase 표기 했기 때문에 값이 제대로 나온다.
search4letters('life, the universe, and everything','o')

import random
random.randint(0,225)

################################################

import vsearch
vsearch.search4letters('hitch-hiker')
vsearch.search4letters('galaxy')
vsearch.search4letters('life, the universe, and eveyrthing', 'o')
