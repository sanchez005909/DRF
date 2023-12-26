# import json
# from datetime import datetime, timedelta
#
# from django_celery_beat.models import PeriodicTask, IntervalSchedule
#
#
# def set_schedule(*args, **kwargs):
#     # executes every 10 seconds.
#     schedule, created = IntervalSchedule.objects.get_or_create(
#         every=1,
#         period=IntervalSchedule.DAYS,
#     )
#
#     PeriodicTask.objects.create(
#         interval=schedule,                  # we created this above.
#         name='Importing contacts',          # simply describes this periodic task.
#         task='proj.tasks.import_contacts',  # name of task.
#         args=json.dumps(['arg1', 'arg2']),
#         kwargs=json.dumps({
#            'be_careful': True,
#         }),
#         expires=datetime.utcnow() + timedelta(seconds=30)
# )