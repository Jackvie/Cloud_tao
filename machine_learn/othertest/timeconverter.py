from datetime import datetime,timedelta
import pytz
a = datetime.now(pytz.UTC) - timedelta(days=14)
print a
print a.strftime('%F %T')
#order_dict['paid_time'] = datetime.strptime(order_dict['paid_at'], '%a, %d %b %Y %H:%M:%S GMT').strftime('%Y-%m-%d %H:%M:%S')
import dateutil
order_dict['paid_time'] = dateutil.parser.parse(order_dict['paid_at'])
### https://stackoverflow.com/questions/38189867/valueerror-time-data-fri-mar-11-155957-est-2016-does-not-match-format-a-b
