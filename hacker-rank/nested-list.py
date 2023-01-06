if __name__ == '__main__':
  #   students = []
  #   for _ in range(int(input())):
  #     name = input()
  #     score = float(input())
  #     students.append([name, score])

  students = [['Harry', 37.21], ['Berry', 37.21],
              ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

  score = sorted(set(student[1] for student in students))[1]
  runner = sorted([student[0] for student in students if student[1] == score])
  print(*runner, sep="\n")
