if __name__ == '__main__':
  #   students = []
  #   for _ in range(int(input())):
  #     name = input()
  #     score = float(input())
  #     students.append([name, score])

  students = [['Harry', 37.21], ['Berry', 37.21],
              ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

  runner_up_score = sorted(set(score for name, score in students))[1]
  runner_up_names = sorted([name for name, score in students if score == runner_up_score])
  print(*runner_up_names, sep="\n")
