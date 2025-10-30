#Q.2: Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]


# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        first = second = dummy
        
        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers together
        while first:
            first = first.next
            second = second.next
        
        # Remove nth node from end
        second.next = second.next.next
        
        return dummy.next


# Helper: Convert list to linked list
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper: Convert linked list to list
def linkedListToList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

if __name__ == "__main__":
    arr = list(map(int, input("Enter linked list elements (space-separated): ").split()))
    n = int(input("Enter n (node position from end to remove): "))
    
    head = createLinkedList(arr)
    sol = Solution()
    new_head = sol.removeNthFromEnd(head, n)
    
    print("\n Linked List after removing", n, "node(s) from end:")
    print(linkedListToList(new_head))
