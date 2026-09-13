def to_rna(dna_strand):
    """Return the RNA complement of a given DNA strand.

    Each nucleotide is replaced with its RNA complement:
    G -> C, C -> G, T -> A, A -> U.
    """
    transcribed_rna = []
    for char in dna_strand:
        if char == "G":
            transcribed_rna.append("C")
        if char == "C":
            transcribed_rna.append("G")
        if char == "T":
            transcribed_rna.append("A")
        if char == "A":
            transcribed_rna.append("U")
    return "".join(transcribed_rna)
