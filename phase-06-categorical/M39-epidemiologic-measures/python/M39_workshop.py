from csv import DictReader
from math import ceil, isclose
from fractions import Fraction
from pathlib import Path

data = Path(__file__).resolve().parents[1] / 'data'


def read(name):
    with (data / name).open() as stream:
        return list(DictReader(stream))


risk = read('M39_risk.csv')
x, y = [Fraction(int(r['events']), int(r['total'])) for r in risk]
print('L1:', float(x-y), float(x/y), float((x/(1-x))/(y/(1-y))), ceil(1/(y-x)))
for r in read('M39_followup.csv'):
    events = int(r['events'])
    print('L2:',r['group'], events/int(r['eligible']),
          100*events/float(r['person_years']), int(r['existing'])/int(r['census']))
rows = read('M39_standard.csv')
for g, target in zip('AB',(.13,.104)):
    group = [r for r in rows if r['group']==g]
    risks = [int(r['events'])/int(r['population']) for r in group]
    weights = [int(r['standard_population']) for r in group]
    direct = sum(a*b for a,b in zip(risks,weights))/sum(weights)
    expected = sum(int(r['population'])*float(r['reference_risk']) for r in group)
    indirect = sum(int(r['events']) for r in group)/expected
    print('L3:',g,direct,expected,indirect)
    assert isclose(direct,target)
    if g=='B':
        assert isclose(indirect,.8)
