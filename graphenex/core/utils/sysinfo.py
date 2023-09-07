import re
import psutil
import platform
from collections import namedtuple, OrderedDict
from unicodedata import normalize


class SysInformation:
    UNITS_MAPPING = [
        (1 << 50, ' PB'),
        (1 << 40, ' TB'),
        (1 << 30, ' GB'),
        (1 << 20, ' MB'),
        (1 << 10, ' KB'),
        (1, (' byte', ' bytes')),
    ]

    @staticmethod
    def pretty_size(bytes, units=UNITS_MAPPING):
        for factor, suffix in units:
            if bytes >= factor:
                break
        amount = int(bytes / factor)

        if isinstance(suffix, tuple):
            singular, multiple = suffix
            if amount == 1:
                suffix = singular
            else:
                suffix = multiple
        return str(amount) + suffix

    @staticmethod
    def get_network_info():
        masks = list()
        MaskResult = namedtuple('MaskResult', ['name', 'recv', 'sent', 'slug'])
        for mask, data in OrderedDict(psutil.net_io_counters(pernic=True)).items():
            if data.packets_recv > 0 or data.packets_sent > 0:
                res = MaskResult(mask, SysInformation.pretty_size(data.packets_recv), SysInformation.pretty_size(data.packets_sent),
                                 SysInformation.slugify(mask))
                masks.append(res)

        return masks

    @staticmethod
    def get_disk_info():
        disks = list()
        DiskResult = namedtuple('DiskResult', ['data', 'name'])
        for disk in psutil.disk_partitions():
            try:
                res = DiskResult(psutil.disk_usage(
                    disk.mountpoint), disk.mountpoint)
                disks.append(res)
            except PermissionError:
                pass

        return disks

    @staticmethod
    def get_general_info():
        uname = platform.uname()
        GeneralResult = namedtuple('GeneralResult', ['system', 'processor'])
        res = GeneralResult(f"{uname.system} | {uname.version}",
                            f"{uname.processor} - ({uname.machine})")

        return res

    @staticmethod
    def get_all_info():
        info_dict = {}
        info_dict['disks'] = SysInformation.get_disk_info()
        info_dict['network'] = SysInformation.get_network_info()
        info_dict['general'] = SysInformation.get_general_info()

        return info_dict

    @staticmethod
    def slugify(text, delim='-'):
        """
        Generate an ASCII-only slug.
        """
        _punctuation_re = re.compile(
            r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
        result = []
        for word in _punctuation_re.split(text.lower()):
            word = normalize('NFKD', word) \
                .encode('ascii', 'ignore') \
                .decode('utf-8')

            if word:
                result.append(word)

        return delim.join(result)
