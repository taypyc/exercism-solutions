def to_rna(dna_strand):
    complements = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    
    return "".join([complements[nucleotide] for nucleotide in dna_strand])