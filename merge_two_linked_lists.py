# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def addNode(self, lst, node):
        node.next= None 
        if lst.val is None: # meaning the list is empty
            lst.val= node.val
        else:
            tail_node= self.getTailNode(lst)
            tail_node.next= node

    def addList(self, lst, list_to_add):
        tail_node= self.getTailNode(lst)
        tail_node.next= list_to_add

    def getTailNode(self, lst):
        if lst.val is None:
            return None
        current_node= lst
        while current_node.next: 
            current_node= current_node.next
        return current_node

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        merged_list= ListNode(None)

        # base cases
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        # iterative case
        current_node_1= list1
        current_node_2= list2

        while current_node_1 and current_node_2:
            if current_node_1.val <= current_node_2.val:
                next_node= current_node_1.next
                self.addNode(merged_list, current_node_1)
                current_node_1= next_node
            elif current_node_1.val > current_node_2.val:
                next_node= current_node_2.next
                self.addNode(merged_list, current_node_2)
                current_node_2= next_node
        
        if current_node_1 and not current_node_2:
            self.addList(merged_list, current_node_1)
        
        elif not current_node_1 and current_node_2:
            self.addList(merged_list, current_node_2)

        return merged_list

l5= ListNode(4, None)
l4= ListNode(3, l5)
list2= ListNode(1, l4)

l3= ListNode(4, None)
l2= ListNode(2, l3)
list1= ListNode(1, l2)

solution= Solution()
result= solution.mergeTwoLists(list1, list2)

result_list= []
current_node= result
while current_node:
    result_list.append(current_node.val)
    current_node= current_node.next

print(result_list)
