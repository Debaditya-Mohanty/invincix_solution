l=[]
def palindromestring(input, j, k):
  count = 0
  
  while j >= 0 and k < len(input):
    if input[j] != input[k]:
      break
    l.append(input[j: k + 1])
    count += 1

    j -= 1
    k += 1

  return count


def palindrome_substrings(input):
  count = 0
  for i in range(0, len(input)):
    count += palindromestring(input, i - 1, i + 1)
    count += palindromestring(input, i, i + 1)

s = "‘DGAABBAAKGHV’";
p=palindrome_substrings(s))

max_len = -1
for ele in l:
    if len(ele) > max_len:
        max_len = len(ele)
        res = ele




