class QuizScoringService:
    def score(self, quiz, answers):
        questions=list(quiz.questions.all()); score=sum(q.check_answer(answers.get(str(q.id), '')) for q in questions)
        return score, round((score / len(questions)) * 100, 2) if questions else 0
