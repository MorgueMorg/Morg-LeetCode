# #Рекурсивный метод

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         # Прописываю условия в которых:
#         # Если нет ни первого, ни второго списка возвратить none
#         if not l1 and not l2: return None
#         # Если нет одного, вернуть второй
#         if not l1: return l2
#         if not l2: return l1
#         # Если оба списка есть, то сравнить списки и юзать рекурсию
#         # Функция next() возвращает следующий элемент итератора
#         if l1.val > l2.val: 
#             l2.next = self.mergeTwoLists(l1, l2.next)
#             return l2
#         else:
#             l1.next = self.mergeTwoLists(l2, l1.next)
#             return l1

###################################################################################################################

# #Итеративный метод 

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # val с род класса ноды
        # dummy -> узел списка, curr -> указатель на него
        dummy = curr = ListNode(None)
        # Цикл для итераций
        while l1 and l2:
            #Если l1 меньше l2, тогда ставлю curr рядом с l1 и меняю curr и l1 в следующие узлы.
            if l1.val < l2.val:
                curr.next = l1
                curr, l1 = curr.next, l1.next
            # Если l1 больше l2, тогда ставлю curr рядом с l2 и меняю curr и l2 в следующие узлы соответственно.
            else: 
                curr.next = l2
                curr, l2 = curr.next, l2.next
        # Если l1 все еще существует, ставлю curr рядом с l1, инчае ставлю curr рядом с l2.
        curr.next = l1 if l1 else l2
        # Возвращаю узел следующего списка
        return dummy.next