from collections import Counter


def get_domain(email_address: str) -> str:
    '''Split on @ and receive all post'''
    return email_address.lower().split("@")[-1]

assert get_domain('joelgrus@gmail.com') == 'gmail.com'
assert get_domain('joel@m.datascientester.com') == 'm.datascientester.com'

with open('email_adresses.txt', 'r') as f:
    domain_counts = Counter(get_domain(line.strip())
                                        for line in f
                                        if "@" in line)

print(domain_counts)