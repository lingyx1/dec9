from django.core.management.base import BaseCommand
import csv
from squirrel.models import Squirrel
class Command(BaseCommand):
   
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    
    def handle(self, *args, **options): 
        headers = ['X', 'Y', 'Unique Squirrel Id', 'Shift', 'Date', 'Age', 'Primary Fur Color', 'Location', 'Specific Location', 'Running', 'Chasing', 'Climbing', 'Eating', 'Foraging', 'Other Activities', 'Kuks', 'Quaas', 'Moans', 'Tail flags', 'Tail tritches', 'Approached', 'Indifferent', 'Runs from']
        rows = []
        ss = Squirrel.objects.all()
        for p in ss:
            row = [p.Longitude, p.Latitude, p.Unique_Squirrel_ID, p.Shift, p.Date, p.Age, p.Primary_Fur_Color, p.Location, p.Specific_Location, p.Running, p.Chasing, p.Climbing, p.Eating, p.Foraging, p.Other_Activities, p.Kuks, p.Quaas, p.Moans, p.Tail_flags, p.Tail_twitches, p.Approaches, p.Indifferent, p.Runs_from]
            rows.append(row)
        with open(options['csv_file'],'w') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(headers)
            f_csv.writerows(rows)
