def caesar_cipher():
    plain_text = input("Write for convert: ")
    shift = int(input("Set movement distance: "))
    cipher_text = ""

    for char in plain_text:
        # 알파벳인 경우만 암호화
        if char.isalpha():
            # 대문자로 통일하여 ASCII 코드 값으로 변환 후 이동 거리 더하기
            code = (ord(char.upper()) - 65 + shift) % 26
            # 변환한 ASCII 코드 값에 다시 65를 더하여 알파벳으로 변환
            cipher_char = chr(code + 65)
        else:
            cipher_char = char

        cipher_text += cipher_char

    return cipher_text

cipher_text = caesar_cipher()
print("Your password is.. :", cipher_text)

