from collections import defaultdict


def raw_trend(eligible, scans, glossary):
    output = defaultdict(lambda: {'eligible':0, 'scanned':0, 'hits':0})
    for page, issue in eligible.items():
        stats = output[issue]
        stats['eligible'] += 1
        if page in scans:
            stats['scanned'] += 1
            stats['hits'] += bool(set(scans[page]['tokens']) & set(glossary))
    return dict(output)
