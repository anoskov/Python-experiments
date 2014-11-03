def transcribing_dna_into_rna(data):
    print data.replace('T', 'U')

if __name__ == "__main__":
    data_set = open('dna.txt')
    data_text = data_set.read()
    transcribing_dna_into_rna(data_text)
