from core.utils.logcl import GraphenexLogger

logger = GraphenexLogger(__name__)

class HardenMethod:
    display_name = __name__
    require_superuser = False

    def command(self):
        # You must override this function
        logger.warn("Harden command not defined!")
        return None