from typing import List, Optional
from linkedlist.ListNode import ListNode

def traverseLinkedList(head: Optional[ListNode]) -> List[int]:
    ans = []
    cur = head 
    while cur:
        ans.append(cur.val)
        cur = cur.next
    return ans  