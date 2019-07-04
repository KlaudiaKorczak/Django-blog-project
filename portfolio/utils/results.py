import itertools


class Results:

    @staticmethod
    def get_results(post_data):
        data = dict(itertools.islice(post_data.items(), 1, None))
        prepared_data = {int(question): int(choice) for question, choice in data.items()}
        return prepared_data

    def prepare_results(self):
        pass
