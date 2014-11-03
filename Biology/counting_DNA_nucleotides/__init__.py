def counting_dna_nucleotides(data):
    for i in 'ACGT':
        print "{} = {}".format(i, data.count(i))

if __name__ == "__main__":
    data_set = open('dna.txt')
    data_text = data_set.read()
    counting_dna_nucleotides(data_text)
