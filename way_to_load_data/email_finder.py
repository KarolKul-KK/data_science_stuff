def get_domain(email_address: str) -> str:
    '''Split on @ and return everything after'''
    return email_address.lower().split('@')[-1]

    assert get_domain('sample@gmail.com') == 'gmail.com'
    assert get_domain('sam@scientist.com') == 'scientist.com'

    from collections import Counter

    with open('email_adresses.txt', 'r') as f:
        domain_counts = Counter(get_domain(line.strip())
                                for line in f
                                if "@" in line)