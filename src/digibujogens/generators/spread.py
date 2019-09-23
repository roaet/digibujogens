import calendar
import datetime as dt

from digibujogens.core import logger


LOG = logger.Logger(__name__)
LOG.start(level='DEBUG')





def monthly(datetime):
    month_start = dt.date(datetime.year, datetime.month, 1)
    cal = calendar.Calendar(6)
    LOG.debug("Starting monthly spread from %s" % cal)
    out = ["# " + calendar.month_name[datetime.month], ""]
    for y, m, d in cal.itermonthdays3(datetime.year, datetime.month):
        if m != datetime.month:
            break
        day_of_week = calendar.weekday(y, m, d)
        days = calendar.day_abbr
        out.append("- %s %2.d" % (
            days[day_of_week][0],
            d,
        ))
    return "\n".join(out)
