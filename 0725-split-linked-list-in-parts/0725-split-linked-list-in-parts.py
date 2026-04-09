class Solution:
    def splitListToParts(self, head, k):
        ans = [None] * k

        size = 0
        current = head
        while current is not None:
            size += 1
            current = current.next


        split_size = size // k

        num_remaining_parts = size % k

        current = head
        prev = current
        for i in range(k):

            new_part = current
            current_size = split_size
            if num_remaining_parts > 0:
                num_remaining_parts -= 1
                current_size += 1

            j = 0
            while j < current_size:
                prev = current
                if current is not None:
                    current = current.next
                j += 1

            if prev is not None:
                prev.next = None

            ans[i] = new_part

        return ans