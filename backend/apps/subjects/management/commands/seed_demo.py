from django.core.management.base import BaseCommand
from apps.subjects.models import Subject
from apps.quizzes.models import Question, Quiz

DEMO_SUBJECTS = [
    ('Mathematics', 'Algebra, geometry, statistics, and problem solving.', 'Intermediate'),
    ('Science', 'Physics, biology, chemistry, and earth science concepts.', 'Beginner'),
    ('Technology', 'Computing, digital systems, and software fundamentals.', 'Mixed'),
    ('Engineering', 'Design thinking, systems, forces, and practical applications.', 'Advanced'),
]

class Command(BaseCommand):
    help = 'Seed demo STEM subjects, questions, and quizzes.'

    def handle(self, *args, **options):
        for name, description, difficulty in DEMO_SUBJECTS:
            subject, _ = Subject.objects.get_or_create(name=name, defaults={'description': description, 'difficulty': difficulty})
            mcq, _ = Question.objects.get_or_create(subject=subject, question_text=f'{name}: choose the best answer.', defaults={'question_type': Question.Type.MULTIPLE_CHOICE, 'options': ['A', 'B', 'C', 'D'], 'answer': 'A', 'explanation': 'A is the configured demo correct answer.', 'difficulty': Question.Difficulty.EASY})
            tf, _ = Question.objects.get_or_create(subject=subject, question_text=f'{name} improves STEM reasoning.', defaults={'question_type': Question.Type.TRUE_FALSE, 'options': ['True', 'False'], 'answer': 'True', 'explanation': 'Practice and feedback improve reasoning over time.', 'difficulty': Question.Difficulty.EASY})
            quiz, _ = Quiz.objects.get_or_create(subject=subject, title=f'{name} Foundations', defaults={'duration': 15})
            quiz.questions.add(mcq, tf)
        self.stdout.write(self.style.SUCCESS('Seeded demo STEM quiz content.'))
