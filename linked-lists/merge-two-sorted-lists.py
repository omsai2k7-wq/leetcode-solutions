class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1
    else:
        current.next = list2

    return dummy.next


def create_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def list_to_array(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


# Typical test case
list1 = create_list([1, 2, 4])
list2 = create_list([1, 3, 4])

merged = merge_two_lists(list1, list2)

print("Typical test case:", list_to_array(merged))


# Edge case
list1 = None
list2 = create_list([0])

merged = merge_two_lists(list1, list2)

print("Edge case:", list_to_array(merged))