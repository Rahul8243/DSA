# =========================================================
# LeetCode Problem 25: Reverse Nodes in k-Group
# 
# Given a linked list, reverse the nodes of a linked list k at a time 
# and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes in the end remain as is.
# =========================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(start, end):
            prev, curr = None, start
            while curr != end:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev

        node = head
        count = 0
        while node and count < k:
            node = node.next
            count += 1

        if count == k:
            reversed_head = reverse(head, node)
            head.next = self.reverseKGroup(node, k)
            return reversed_head
        return head

# -----------------------
# Helper functions
# -----------------------
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals))

# -----------------------
# User Input
# -----------------------
nums = input("Enter linked list values separated by space: ").strip().split()
nums = list(map(int, nums))
k = int(input("Enter k: "))

head = build_linked_list(nums)
solution = Solution()
new_head = solution.reverseKGroup(head, k)

print("Reversed list in k-groups:")
print_linked_list(new_head)
