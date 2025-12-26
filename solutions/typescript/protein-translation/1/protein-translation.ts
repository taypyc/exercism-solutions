const CODON_TO_PROTEIN: Record<string, string> = {
  UUU: 'Phenylalanine',
  UUC: 'Phenylalanine',
  UUA: 'Leucine',
  UUG: 'Leucine',
  UCU: 'Serine',
  UCC: 'Serine',
  UCA: 'Serine',
  UCG: 'Serine',
  UAU: 'Tyrosine',
  UAC: 'Tyrosine',
  UGU: 'Cysteine',
  UGC: 'Cysteine',
  UGG: 'Tryptophan',
  AUG: 'Methionine',
  UAA: 'STOP',
  UAG: 'STOP',
  UGA: 'STOP',
};

export function translate(rna: string): string[] {
  if (!rna) {
    return [];
  }

  const protein: string[] = [];
  
  for (let i = 0; i < rna.length; i += 3) {
    const codon = rna.slice(i, i + 3);
    
    if (codon.length < 3) {
      throw new Error('Invalid codon');
    }
    
    const aminoAcid = CODON_TO_PROTEIN[codon];
    
    if (!aminoAcid) {
      throw new Error(`Invalid codon: ${codon}`);
    }
    
    if (aminoAcid === 'STOP') {
      break;
    }
    
    protein.push(aminoAcid); 
  }
  
  return protein;
}
