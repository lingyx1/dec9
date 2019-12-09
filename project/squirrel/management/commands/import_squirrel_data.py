from django.core.management.base import BaseCommand
import csv
from squirrel.models import Squirrel

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        for item in data:
            s = Squirrel(
                Longitude=item['X'],
                Latitude=item['Y'],
                Unique_Squirrel_ID=item['Unique Squirrel ID'],
                Shift=item['Shift'],
                Date=item['Date'],
                Age=item['Age'],
                Primary_Fur_Color=item['Primary Fur Color'],
                Location=item['Location'],
                Specific_Location=item['Specific Location'],
                Running=item['Running'].capitalize(),
                Chasing=item['Chasing'].capitalize(),
                Climbing=item['Climbing'].capitalize(),
                Eating=item['Eating'].capitalize(),
                Foraging=item['Foraging'].capitalize(),
                Other_Activities=item['Other Activities'],
                Kuks=item['Kuks'].capitalize(),
                Quaas=item['Quaas'].capitalize(),
                Moans=item['Moans'].capitalize(),
                Tail_flags=item['Tail flags'].capitalize(),
                Tail_twitches=item['Tail twitches'].capitalize(),
                Approaches=item['Approaches'].capitalize(),
                Indifferent=item['Indifferent'].capitalize(),
                Runs_from=item['Runs from'].capitalize(),
            )
            s.save()
