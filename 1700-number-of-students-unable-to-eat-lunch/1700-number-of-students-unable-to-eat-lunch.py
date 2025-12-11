class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while students:
            if students[0] == sandwiches[0]:
                students = students[1:] 
                sandwiches = sandwiches[1:]
                count = 0

            else:
                students = students[1:] + [students[0]]
                count += 1

            if count == len(students):
                break

        return len(students)
