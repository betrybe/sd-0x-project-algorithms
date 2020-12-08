from challenges.challenge_palindromes_recursive import is_palindrome_recursive


def test_validar_se_a_palavra_e_um_palindromo_retorna_true():
    word = "ANA"
    print(is_palindrome_recursive(word, 0, len(word) - 1)) is True
    word = "SOCOS"
    print(is_palindrome_recursive(word, 0, len(word) - 1)) is True
    word = "REVIVER"
    print(is_palindrome_recursive(word, 0, len(word) - 1)) is True


def test_validar_se_a_palavra_nao_e_um_palindromo_retorna_false():
    word = "AGUA"
    print(is_palindrome_recursive(word, 0, len(word) - 1)) is False


def test_validar_se_nao_passar_palavra_retorna_false():
    word = ""
    print(is_palindrome_recursive(word, 0, len(word) - 1)) is False
