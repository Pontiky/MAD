import aiohttp_jinja2

from mapadroid.madmin.RootEndpoint import RootEndpoint


class EventsEndpoint(RootEndpoint):
    """
    "/statistics"
    """

    # TODO: Auth
    @aiohttp_jinja2.template('events.html')
    async def get(self):
        return {
            "title": "MAD Events",
            "time": self._get_mad_args().madmin_time,
            "responsive": str(self._get_mad_args().madmin_noresponsive).lower()
        }
