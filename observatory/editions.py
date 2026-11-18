def frame(issues, scans):
    eligible = {page:row['id'] for row in issues for page in row['eligible']}
    index = {}
    for scan in scans:
        page = scan['page']
        if page not in eligible or page in index:
            raise ValueError('扫描页重复或不在发行口径内')
        index[page] = scan
    return eligible,index
