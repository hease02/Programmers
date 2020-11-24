def solution(phone_book):
    answer = True
    book = []

    phone_book = sorted(phone_book)

    for phone in phone_book:
        tel = ""

        for p in phone:
            tel = tel + p

            if tel in book:
                answer = False
                return answer
        book.append(phone)

    return answer

phone_book = ["97674223", "1195524421", "119"]
# phone_book = ["123","456","789"]
# phone_book = ["123","12","1235","567","88"]
print(solution(phone_book))
