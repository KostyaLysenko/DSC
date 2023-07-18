from Tree import Node
from example_string import reverse, capital
root = Node(5)
root.left=Node(2)
root.right=Node(6)


def test_insert():
    root.insert(7)
    assert root.travers_in_order() == '2 5 6 7 '

def test_travers_max():
    assert root.travers_max_order()==root.travers_in_order()

def test_delete_key():
    assert root.delete_key(2)==root.travers_in_order()
# def test_reverse():
#     assert reverse("hellow") == "wolleh"
#
# def test_reverse_for_empty_string():
#     assert reverse(("")) == ""
#
# def test_capitel():
#     assert capital("hhh sss vvv") == "Hhh sss vvv"
