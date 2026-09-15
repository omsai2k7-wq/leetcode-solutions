class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


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
head = create_list([1, 2, 3, 4, 5])

reversed_head = reverse_list(head)

print("Typical test case:", list_to_array(reversed_head))


# Edge case
head = create_list([])

reversed_head = reverse_list(head)

print("Edge case:", list_to_array(reversed_head))