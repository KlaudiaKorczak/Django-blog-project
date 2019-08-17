import itertools
from django.db.models import Max, Sum

class Data:

    @staticmethod
    def get_results(questions):
        statistics = {}
        for question in questions:
            choices = question.choice_set
            max_vote = choices.aggregate(Max('votes'))
            all_votes = choices.aggregate(Sum('votes'))
            choice = question.choice_set.filter(votes=max_vote['votes__max'])

            votes_percent = (max_vote['votes__max'] / all_votes['votes__sum']) * 100
            statistics[question] = [choice, votes_percent]
            print(statistics)
        return "message"

    @staticmethod
    def get_poll_dict(post_data):
        data = dict(itertools.islice(post_data.items(), 1, None))
        prepared_data = {int(question): int(choice) for question, choice in data.items()}
        return prepared_data
