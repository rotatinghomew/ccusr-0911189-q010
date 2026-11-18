from collections import Counter


def proof_receipts(checks, version, eligible):
    totals = Counter()
    for row in checks:
        if row['page'] not in eligible or row['kind'] not in {'random','targeted'}:
            raise ValueError('点校记录来源或版面编号不正确')
        if row['version'] == version:
            totals[row['kind']] += 1
    return dict(totals)
