# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head # Проверка на пустой список
        odd = head # Первый узел
        even = head.next # Если в листе один узел, то это будет None
        eHead = even # Переменная где начинаются четные узлы
        
        while even and even.next: # Цикл поначалу бесполезен, если только один узел
            odd.next = odd.next.next
            even.next = even.next.next
            # После двух операций выше, чёт/нечёт остаются на тех же местах
            # Поэтому двумя операциями ниже, меняем их на след узел
            odd = odd.next
            even = even.next
        # Нечетный указатель сейчас указывает на последний узел списка нечетных узлов
        odd.next = eHead
        # Возвращаю нечет в начале самого списка
        return head