"""
Thierno Diallo

Lab7c

This class contains methods for creating DNA sequences and finding
out their lengths, complements, base occurences and base percentages.
"""

# Complete Doc
class DNA:
    """
    Represents a DNA sequences with the unique attributes:
    seq (Str) - a DNA sequence
    """
    
    def __init__(self, seq):
        """
        Constructs a DNA sequence and raises a value error if the sequence
        has an unrecognized base.
        """
        self.seq = seq.upper()
        for letter in seq:
            if letter.upper() not in ['A','T','G', 'C']:
                raise ValueError('Invalid DNA sequence. Must only '
                                 + 'contain A, T, G, C bases.')
    
    def __str__(self):
        """
        Returns a string representation of the DNA sequence. 
        """
        return f'{self.seq}' 
    
    def __len__(self):
        """
        Returns the length of the DNA sequence.
        """
        return len(self.seq)
    
    def complement(self):
        """
        Returns the complement of the DNA sequence.
        """
        DNA_compliment = ''
        for base in self.seq:
            if base == 'A':
                DNA_compliment += 'T'
            elif base == 'T':
                DNA_compliment += 'A'
            elif base == "C":
                DNA_compliment += 'G'
            elif base == 'G':
                DNA_compliment += 'C'
        return DNA_compliment

    def count_occurrences(self, val):
        """
        Takes a base and returns the numer of times that base occurs in the
        sequence.

        Arguments: a str DNA base
        Return Value: an int number of occurances
        """
        if val.upper() not in ['A','T','G', 'C']:
            raise ValueError('Invalid base given. Base must be A, T, G, or C.')
        count = 0
        for base in self.seq:
            if base == val.upper():
                count += 1
        return count

    def percentage_of(self, base):
        """
        Takes a base name and returns the percentage of the sequence
        that is made up of that base as a float.

        Arguments: a str base
        Return Value: the concetration of that base as a float
        """
        return self.count_occurrences(base)/ len(self.seq)

            