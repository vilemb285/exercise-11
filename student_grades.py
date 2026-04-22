class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.get_by_index(index)

        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"

    def find(self, wanted_score):
        students = []
        for i in range(len(self.scores)):
            if self.scores[i] == wanted_score:
                students.append(i)
        return students

    def get_sorted(self):
        scores = self.scores[:]
        n = len(scores)

        for i in range(n):
            for j in range(0, n - i - 1):
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]

        return scores



from sorting import random_numbers
def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(f"Počet studentů: {results.count()}")
    for i in range(results.count()):
        print(f"Student {i}: {results.get_by_index(i)} points - {results.get_grade(i)}")
    print(f"Studenti s plným počtem bodů: {results.find(100)}")
    print(f"Body seřazené od nejhoršího po nejlepší: {results.get_sorted()}")

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(f"Náhodný počet studentů: {random_results.count()}")
    print(f"Náhodné výsledky: {random_results.get_sorted()}")






if __name__ == "__main__":
    main()