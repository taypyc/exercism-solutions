def proteins(strand):
    codon_table = {
        'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
        'UUA': 'Leucine', 'UUG': 'Leucine', 'CUU': 'Leucine', 
        'CUC': 'Leucine', 'CUA': 'Leucine', 'CUG': 'Leucine',
        'AUU': 'Isoleucine', 'AUC': 'Isoleucine', 'AUA': 'Isoleucine',
        'AUG': 'Methionine',
        'GUU': 'Valine', 'GUC': 'Valine', 'GUA': 'Valine', 'GUG': 'Valine',
        'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
        'AGU': 'Serine', 'AGC': 'Serine',
        'CCU': 'Proline', 'CCC': 'Proline', 'CCA': 'Proline', 'CCG': 'Proline',
        'ACU': 'Threonine', 'ACC': 'Threonine', 'ACA': 'Threonine', 'ACG': 'Threonine',
        'GCU': 'Alanine', 'GCC': 'Alanine', 'GCA': 'Alanine', 'GCG': 'Alanine',
        'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
        'CAU': 'Histidine', 'CAC': 'Histidine',
        'CAA': 'Glutamine', 'CAG': 'Glutamine',
        'AAU': 'Asparagine', 'AAC': 'Asparagine',
        'AAA': 'Lysine', 'AAG': 'Lysine',
        'GAU': 'Aspartic acid', 'GAC': 'Aspartic acid',
        'GAA': 'Glutamic acid', 'GAG': 'Glutamic acid',
        'UGU': 'Cysteine', 'UGC': 'Cysteine',
        'UGG': 'Tryptophan',
        'CGU': 'Arginine', 'CGC': 'Arginine', 'CGA': 'Arginine', 'CGG': 'Arginine',
        'AGA': 'Arginine', 'AGG': 'Arginine',
        'GGU': 'Glycine', 'GGC': 'Glycine', 'GGA': 'Glycine', 'GGG': 'Glycine',
        'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'
    }
    
    protein = []
    
    for i in range(0, len(strand), 3):
        codon = strand[i:i+3]
        
        if len(codon) < 3:
            break
        
        if codon in codon_table:
            amino_acid = codon_table[codon]
            
            if amino_acid == 'STOP':
                break
            
            protein.append(amino_acid)
        else:
            raise ValueError(f"Invalid codon: {codon}")
    
    return protein