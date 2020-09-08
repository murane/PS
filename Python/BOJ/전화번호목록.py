def solution(phone_book):
    phone_book = list(map(str,phone_book))
    phone_book.sort()
    flg=True
    for i in range(len(phone_book)-1):
        length = min(len(phone_book[i]),len(phone_book[i+1]))
        for j in range(length):
            if phone_book[i][j]!=phone_book[i+1][j]:
                flg=True
                break
            elif phone_book[i][j]==phone_book[i+1][j]:
                flg=False
        if not flg:
            return flg
            
    
    return flg

if __name__ == '__main__':
    book=["88","12","1235","567","123"]
    solution(book)
    