n,t = map(int, input().split())
books = list(map(int, input().split()))
maxBooks=currentBooks=left=0

for right in range(len(books)):
    currentBooks+=books[right]
    while currentBooks>t:
        currentBooks -= books[left]
        left += 1
    maxBooks = max(maxBooks, right - left + 1)

print(maxBooks)
