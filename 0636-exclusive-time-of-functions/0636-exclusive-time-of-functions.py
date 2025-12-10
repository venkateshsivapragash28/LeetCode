class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        stack = []
        res = [0] * n
        prev = 0

        for i in logs:
            fn, typ, time = i.split(':')
            fn = int(fn)
            time = int(time)
            if typ == 'start':
                if stack:
                    res[stack[-1]] += time-prev
                stack.append(fn)
                prev = time

            else:
                res[stack.pop()] += time-prev + 1
                prev = time + 1

        return res

        

            