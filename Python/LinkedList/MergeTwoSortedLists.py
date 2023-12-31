class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        temp = head

        while list1 and list2:
            if(list1.val < list2.val):
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next

            temp = temp.next
        
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        
        return head.next
    
s = Solution()
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list2 = ListNode(1)
list2.next = ListNode(2)
list2.next.next = ListNode(3)
s.mergeTwoLists(list1, list2)