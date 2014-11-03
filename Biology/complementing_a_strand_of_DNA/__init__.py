import re


def complementing_a_strand_of_dna(data):
    rdict = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }
    robj = re.compile('|'.join(rdict.keys()))
    result = robj.sub(lambda m: rdict[m.group(0)], data)
    print result[::-1]

if __name__ == "__main__":
    data_set = open('dna.txt')
    data_text = data_set.read()
    complementing_a_strand_of_dna(data_text)
