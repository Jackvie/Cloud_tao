from django.core.management.base import BaseCommand

class Command(BaseCommand):
	help='xxxxx'

	def add_arguments(self,parser):
		parser.add_argument('aaa', nargs='+', type=int)

	def handle(self, *args, **options):
		print('hhh')
		print(args)
		print(options)

	
