#Q.1:Given the head of a singly linked list, reverse the list, and 4
# return the reversed list.

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]


# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next   # store next node
            curr.next = prev        # reverse pointer
            prev = curr             # move prev forward
            curr = next_node        # move curr forward
        
        return prev  # new head


def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedListToList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

if __name__ == "__main__":
    arr = list(map(int, input("Enter linked list elements (space-separated): ").split()))
    head = createLinkedList(arr)
    
    sol = Solution()
    reversed_head = sol.reverseList(head)
    
    print("\n Reversed Linked List:")
    print(linkedListToList(reversed_head))
