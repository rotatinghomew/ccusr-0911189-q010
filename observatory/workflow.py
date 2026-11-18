from .editions import frame
from .extract import raw_trend
from .reading import proof_receipts


def report(data):
    eligible,scanned = frame(data['issues'],data['scans'])
    edition = data['edition']
    return {'definition':edition, 'raw':raw_trend(eligible,scanned,data['glossaries'][edition][data['topic']]),
            'proof':proof_receipts(data['checks'],edition,eligible)}
