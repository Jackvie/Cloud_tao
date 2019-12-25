from datetime import datetime,timedelta
import pytz
a = datetime.now(pytz.UTC) - timedelta(days=14)
print a
print a.strftime('%F %T')
