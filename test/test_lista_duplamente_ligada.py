# ATENÇÃO: Não altere o código de arquivo
import os.path
import sys
from pytest import raises
from lista_duplamente_ligada_ordenada import ListaDuplamenteLigadaOrdenada


# ---- INÍCIO: teste método is_empty()

def test_is_empty_true():

    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()

    result = lista_duplamente_ligada.is_empty()
    expected = True

    assert result == expected and lista_duplamente_ligada.size() == 0


def test_is_empty_false():

    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada(3)
    lista_duplamente_ligada.add(1)
    lista_duplamente_ligada.add(2)

    result = lista_duplamente_ligada.is_empty()
    expected = False

    assert result == expected and lista_duplamente_ligada.size() == 2

# ---- FIM: teste método is_empty()


# ---- INÍCIO: teste método is_full()

def test_is_full_true():

    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada(1)
    lista_duplamente_ligada.add(1)

    result = lista_duplamente_ligada.is_full()
    expected = True

    assert result == expected and lista_duplamente_ligada.size() == 1


def test_is_full_false():

    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada(3)
    lista_duplamente_ligada.add(1)
    lista_duplamente_ligada.add(2)

    result = lista_duplamente_ligada.is_full()
    expected = False

    assert result == expected and lista_duplamente_ligada.size() == 2

# ---- FIM: teste método is_full()


# ---- INÍCIO: teste método first()

def test_first_com_item():

    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()
    lista_duplamente_ligada.add(1)

    result = lista_duplamente_ligada.first().dado
    expected = 1

    assert result == expected


def test_first_sem_item():

    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()

    result = lista_duplamente_ligada.first()
    expected = None

    assert result == expected


def test_first_com_item_ordem_aleatoria():

    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()
    lista_duplamente_ligada.add(3)
    result = lista_duplamente_ligada.first().dado
    expected = 3
    assert result == expected

    lista_duplamente_ligada.add(1)
    result = lista_duplamente_ligada.first().dado
    expected = 1
    assert result == expected

    lista_duplamente_ligada.add(2)
    result = lista_duplamente_ligada.first().dado
    expected = 1
    assert result == expected

# ---- FIM: teste método first()


# ---- INÍCIO: teste método last()

def test_last_com_item():

    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()
    lista_duplamente_ligada.add(1)

    result = lista_duplamente_ligada.last().dado
    expected = 1

    assert result == expected


def test_last_sem_item():

    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()

    result = lista_duplamente_ligada.last()
    expected = None

    assert result == expected


def test_last_com_item_ordem_aleatoria():

    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()
    lista_duplamente_ligada.add(3)
    result = lista_duplamente_ligada.last().dado
    expected = 3
    assert result == expected

    lista_duplamente_ligada.add(5)
    result = lista_duplamente_ligada.last().dado
    expected = 5
    assert result == expected

    lista_duplamente_ligada.add(4)
    result = lista_duplamente_ligada.last().dado
    expected = 5
    assert result == expected

# ---- FIM: teste método last()


# ---- INÍCIO: teste método add()

def test_add_em_lista_cheia():

    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada(1)

    lista_duplamente_ligada.add(1)

    result = lista_duplamente_ligada.contains(1)
    expected = True

    assert result == expected
    with raises(Exception):
        lista_duplamente_ligada.add(2) # deve gerar erro


def test_add_em_lista_vazia():

    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()

    result = lista_duplamente_ligada.add(1)
    result = lista_duplamente_ligada.add(2)
    expected = True

    assert result == expected and lista_duplamente_ligada.size() == 2


def test_add_em_lista_para_verificar_ordem_aleatoria():

    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada(10)

    lista_duplamente_ligada.add(3)
    lista_duplamente_ligada.add(4)
    lista_duplamente_ligada.add(2)
    lista_duplamente_ligada.add(5)
    lista_duplamente_ligada.add(1)

    result = lista_duplamente_ligada.display()
    expected = [
        1,
        2,
        3,
        4,
        5
    ]

    assert result == expected


def test_add_em_lista_para_verificar_ordem_crescente():

    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada(10)

    lista_duplamente_ligada.add(1)
    lista_duplamente_ligada.add(2)
    lista_duplamente_ligada.add(3)
    lista_duplamente_ligada.add(4)
    lista_duplamente_ligada.add(5)

    result = lista_duplamente_ligada.display()
    expected = [
        1,
        2,
        3,
        4,
        5
    ]

    assert result == expected


def test_add_em_lista_para_verificar_ordem_decrescente():

    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada(10)

    lista_duplamente_ligada.add(5)
    lista_duplamente_ligada.add(4)
    lista_duplamente_ligada.add(3)
    lista_duplamente_ligada.add(2)
    lista_duplamente_ligada.add(1)

    result = lista_duplamente_ligada.display()
    expected = [
        1,
        2,
        3,
        4,
        5
    ]

    assert result == expected

# ---- FIM: teste método add()


# ---- INÍCIO: teste método remove()

def test_remove_em_lista_vazia():

    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()

    with raises(Exception):
        lista_duplamente_ligada.remove() # deve gerar erro


def test_remove_em_lista_com_item_presente_no_meio():
    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            lista_duplamente_ligada.add(item[:-1])

    result = lista_duplamente_ligada.remove('3')
    expected = True

    assert expected == result

    result = lista_duplamente_ligada.display()
    expected = [
        '1',
        '2',
        '4',
        '5'
    ]

    assert expected == result


def test_remove_em_lista_com_item_presente_no_inicio():
    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            lista_duplamente_ligada.add(item[:-1])

    result = lista_duplamente_ligada.remove('1')
    expected = True

    assert expected == result

    result = lista_duplamente_ligada.display()
    expected = [
        '2',
        '3',
        '4',
        '5'
    ]

    assert expected == result


def test_remove_em_lista_com_item_presente_no_fim():
    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            lista_duplamente_ligada.add(item[:-1])

    result = lista_duplamente_ligada.remove('5')
    expected = True

    print("LISTA: ",lista_duplamente_ligada.display())
    assert expected == result

    result = lista_duplamente_ligada.display()
    expected = [
        '1',
        '2',
        '3',
        '4'
    ]

    assert expected == result


def test_remove_em_lista_sem_item_presente():
    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            lista_duplamente_ligada.add(item[:-1])

    result = lista_duplamente_ligada.remove('9')
    expected = False

    assert expected == result


def test_remove_em_lista_com_itens_ate_esvaziar():
    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            lista_duplamente_ligada.add(item[:-1])

    for x in range(5):
      lista_duplamente_ligada.remove(str(x+1))

    with raises(Exception):
        lista_duplamente_ligada.remove(1) # deve gerar erro

# ---- FIM: teste método remove()


# ---- INÍCIO: teste método contains()

def test_contains_em_lista_vazia():
    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()

    result = lista_duplamente_ligada.contains(1)
    expected = False

    assert expected == result


def test_contains_em_lista_com_item_presente():
    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()
    lista_duplamente_ligada.add(1)

    result = lista_duplamente_ligada.contains(1)
    expected = True

    assert expected == result


def test_contains_em_lista_sem_item_presente():
    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()
    lista_duplamente_ligada.add(1)

    result = lista_duplamente_ligada.contains(2)
    expected = False

    assert expected == result

# ---- FIM: teste método contains()


# ---- INÍCIO: teste método display()

def test_display_em_lista_com_elementos_string():
    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            lista_duplamente_ligada.add(item[:-1])

    result = lista_duplamente_ligada.display()
    expected = [
        "1",
        "2",
        "3",
        "4",
        "5",
    ]

    assert result == expected


def test_display_em_lista_com_elementos_int():
    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()

    lista_duplamente_ligada.add(1)
    lista_duplamente_ligada.add(2)
    lista_duplamente_ligada.add(3)

    result = lista_duplamente_ligada.display()
    expected = [
        1,
        2,
        3,
    ]

    assert result == expected


def test_display_em_lista_sem_elementos_ao_criar_lista_duplamente_ligada():
    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()

    result = lista_duplamente_ligada.display()
    expected = []
    
    assert result == expected


def test_display_em_lista_sem_elementos_ao_esvaziar_lista_duplamente_ligada():
    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()

    lista_duplamente_ligada.add(1)
    lista_duplamente_ligada.add(2)
    lista_duplamente_ligada.remove(2)
    lista_duplamente_ligada.remove(1)

    result = lista_duplamente_ligada.display()
    expected = []
    
    assert result == expected

# ---- FIM: teste método display()


# ---- INÍCIO: teste método size()

def test_size_em_lista_ao_criar_lista():
    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()

    result = lista_duplamente_ligada.size()
    expected = 0
    
    assert result == expected


def test_size_em_lista_ao_inserir_itens():
    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()

    lista_duplamente_ligada.add(1)
    expected = 1
    assert lista_duplamente_ligada.size() == expected

    lista_duplamente_ligada.add(1)
    expected = 2
    assert lista_duplamente_ligada.size() == expected

    lista_duplamente_ligada.add(1)
    expected = 3
    assert lista_duplamente_ligada.size() == expected


def test_size_ao_remover_itens():
    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada()

    lista_duplamente_ligada.add(1)
    lista_duplamente_ligada.add(1)
    lista_duplamente_ligada.add(1)

    lista_duplamente_ligada.remove(1)
    result = lista_duplamente_ligada.size()
    expected = 2
    assert result == expected

    lista_duplamente_ligada.remove(1)
    result = lista_duplamente_ligada.size()
    expected = 1
    assert result == expected

    lista_duplamente_ligada.remove(1)
    result = lista_duplamente_ligada.size()
    expected = 0
    assert result == expected

# ---- FIM: teste método size()


# ---- INÍCIO: teste de alteração das ordem dos elementos da lista duplamente ligada

def test_add_remove_em_lista_alterando_itens_no_inicio():

    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada(10)

    lista_duplamente_ligada.add(2)
    lista_duplamente_ligada.add(4)
    lista_duplamente_ligada.add(1)
    lista_duplamente_ligada.add(3)
    lista_duplamente_ligada.add(5)


    # teste de remoção no início
    lista_duplamente_ligada.remove(1)
    result = lista_duplamente_ligada.first()
    expected = 2
    assert result.dado == expected and result.anterior == None


    # teste de alteração no início
    lista_duplamente_ligada.add(0)
    result = lista_duplamente_ligada.first()
    expected = 0
    assert result.dado == expected and result.anterior == None


def test_add_remove_em_lista_alterando_itens_no_fim():

    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada(10)

    lista_duplamente_ligada.add(1)
    lista_duplamente_ligada.add(4)
    lista_duplamente_ligada.add(2)
    lista_duplamente_ligada.add(5)
    lista_duplamente_ligada.add(3)

    # teste de remoção no fim
    lista_duplamente_ligada.remove(5)
    result = lista_duplamente_ligada.last()
    expected = 4
    assert result.dado == expected and result.prox == None

    # teste de alteração no fim
    lista_duplamente_ligada.add(6)
    result = lista_duplamente_ligada.last()
    expected = 6
    assert result.dado == expected and result.prox == None


def test_add_remove_em_lista_alterando_itens_no_meio():

    try:
        exists = os.path.exists("lista_duplamente_ligada_ordenada.py")
        assert exists == True
    except:
        sys.exit()

    lista_duplamente_ligada = ListaDuplamenteLigadaOrdenada(10)

    lista_duplamente_ligada.add(1)
    lista_duplamente_ligada.add(2)
    lista_duplamente_ligada.add(3)
    lista_duplamente_ligada.add(7)

    # teste de remoção no meio mais próximo do início
    lista_duplamente_ligada.remove(2)

    result = lista_duplamente_ligada.display() 
    expected = [
        1,
        3,
        7,
    ]
    assert result == expected

    # teste de alteração no meio
    lista_duplamente_ligada.add(6)
    
    result = lista_duplamente_ligada.display() 
    expected = [
        1,
        3,
        6,
        7,
    ]
    assert result == expected

    # teste de removendo o mais próximo do fim
    lista_duplamente_ligada.remove(6)
    
    result = lista_duplamente_ligada.display() 
    expected = [
        1,
        3,
        7,
    ]
    assert result == expected

    # teste de removendo o mais próximo do fim e início
    lista_duplamente_ligada.remove(3)
    
    result = lista_duplamente_ligada.display() 
    expected = [
        1,
        7,
    ]
    assert result == expected

# ---- FIM: teste de alteração das ordem dos elementos da lista duplamente ligada