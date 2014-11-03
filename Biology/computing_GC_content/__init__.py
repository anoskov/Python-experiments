from Bio import SeqIO
from operator import itemgetter

def parse_fasta(fasta_file):
    data = {}
    for f in fasta_file:
        data[f.id] = str(f.seq)
    return data


def computing_gc_content(data):
    gc_content = {}
    for id, seq in data.iteritems():
        gc_count = seq.count('G') + seq.count('C')
        gc_content[id] = round(float(gc_count)*100/len(seq), 6)
    return max(gc_content.iteritems(), key=itemgetter(1))

if __name__ == "__main__":
    fasta_sequences = SeqIO.parse(open('data.fasta'), 'fasta')
    data = computing_gc_content(parse_fasta(fasta_sequences))
    print "{}\n{}".format(data[0], data[1])