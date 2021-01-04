from challenges.challenge_anagrams import is_anagram


def test_validar_se_as_palavras_nao_sao_um_anagrama():
    first_string = "pedra"
    second_string = "perdaaa"
    assert is_anagram(first_string, second_string) is False


def test_validar_se_as_palavras_sao_um_anagrama():
    first_string = "pedra"
    second_string = "perda"
    assert is_anagram(first_string, second_string) is True


def test_validar_se_passar_primeira_palavra_em_branco_retorna_false():
    first_string = ""
    second_string = "perda"
    assert is_anagram(first_string, second_string) is False


def test_validar_se_passar_segunda_palavra_em_branco_retorna_false():
    first_string = "pedra"
    second_string = ""
    assert is_anagram(first_string, second_string) is False
