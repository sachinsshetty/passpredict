import datetime

from passpredict import SatnogsDbTLESource, Location, SGP4Propagator, Observer

try:
    from zoneinfo import ZoneInfo
except ImportError:
    from backports.zoneinfo import ZoneInfo


def satnogs_source():
    location = Location('Wurburg, Germany', 49.7833, 9.9333, 0)
    date_start = datetime.datetime.now(tz=ZoneInfo('Europe/Berlin')) 
    #date_start -= datetime.timedelta(days=1)
    date_end = date_start + datetime.timedelta(days=1)
    source = SatnogsDbTLESource()
    tle = source.get_tle(98847)  # International space station, Norad ID 25544
    satellite = SGP4Propagator.from_tle(tle)
    observer = Observer(location, satellite)
    overpasses = observer.pass_list(date_start, limit_date=date_end)
    print(overpasses)


if __name__ == "__main__":
    satnogs_source()
