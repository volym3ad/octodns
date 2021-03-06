#
#
#

from .geo_data import geo_data


class GeoCodes(object):
    __COUNTRIES = None

    @classmethod
    def validate(cls, code, prefix):
        '''
        Validates an octoDNS geo code making sure that it is a valid and
        corresponding:
            * continent
            * continent & country
            * continent, country, & province
        '''
        reasons = []

        pieces = code.split('-')
        n = len(pieces)
        if n > 3:
            reasons.append('{}invalid geo code "{}"'.format(prefix, code))
        elif n > 0 and pieces[0] not in geo_data:
            reasons.append('{}unknown continent code "{}"'
                           .format(prefix, code))
        elif n > 1 and pieces[1] not in geo_data[pieces[0]]:
            reasons.append('{}unknown country code "{}"'.format(prefix, code))
        elif n > 2 and \
                pieces[2] not in geo_data[pieces[0]][pieces[1]]['provinces']:
            reasons.append('{}unknown province code "{}"'.format(prefix, code))

        return reasons
