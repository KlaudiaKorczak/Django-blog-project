import logging
import os
from csv import DictReader
from django.core.management import BaseCommand
from pathlib import Path
from portfolio.models import Choice, Comment, Paintings, Question

logging.basicConfig(level=logging.INFO)


NAMES_MAPPING = [{'model': Comment, 'csv_file': 'comment.csv'},
                 {'model': Paintings, 'csv_file': 'paintings.csv'},
                 {'model': Question, 'csv_file': 'question.csv'}]

APP_PATH = Path(__file__).parents[2]

ALREADY_LOADED_ERROR_MESSAGE = '''
***
If you need to reload data from the CSV file, first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty database with tables
***'''


class Command(BaseCommand):
    # Show this when the user types help
    help = 'Loads data from csv files into our models'

    def handle(self, *args, **options):
        if Choice.objects.exists() and Comment.objects.exists() and \
                Paintings.objects.exists() and Question.objects.exists():
            logging.info('Data have already been loaded. \n' + ALREADY_LOADED_ERROR_MESSAGE)
            return
        try:
            for mapping in NAMES_MAPPING:
                model = mapping['model']
                if not model.objects.exists():
                    csv_data, headers = get_csv_data(mapping['csv_file'])
                    for row in csv_data:
                        model_instance = model()
                        for name in headers[1:]:
                            setattr(model_instance, name, row[name])
                        model_instance.save()
                    logging.info('Data fully loaded from {}'.format(mapping['csv_file']))

            process_with_foreign_key()

            logging.info('Database has been successfully filled.')
        except Exception as e:
            logging.exception(e)


def get_csv_data(csv_file):
    file_path = os.path.join(APP_PATH, 'static/tables/' + csv_file)
    csv_data = DictReader(open(file_path))
    headers = csv_data.fieldnames
    return csv_data, headers


def process_with_foreign_key():
    if Choice.objects.exists():
        return
    csv_data, headers = get_csv_data('choice.csv')
    questions = Question.objects.all()
    questions_ids = [question.id for question in questions]
    for row in csv_data:
        choice = Choice()
        id_position = row['question_id']
        question_id = questions_ids[int(id_position) - 1]
        for name in headers[1:]:
            if name == 'question_id':
                setattr(choice, name, question_id)
            else:
                setattr(choice, name, row[name])
        choice.save()
    logging.info('Data fully loaded from choice.csv.')
