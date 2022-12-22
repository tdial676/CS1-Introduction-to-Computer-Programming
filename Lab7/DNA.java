/**
 * Thierno Diallo
 * 
 * This class represents a DNA sequence comprised of 
 * 'A', 'T', 'C', 'G' nucleotide bases. The class supports
 * simple methods to represent the sequence as a String,
 * get a complement sequence, and compute information
 * about base counts and percentages.
 */
public class DNA {
    // String of DNA base characters in upper-case
    // (private means only methods in this class
    // can access the field which is what we want)
    private String seq;

    public DNA(String seq) {
        /**
         * Initializes a new DNA sequence using the provided
         * seq String. Letter-casing is supported for the given
         * seq, but a DNA sequence is represented in upper-case.
         * 
         * @param seq - sequence of 'A', 'C', 'G', 'T' bases.
         * @throws IllegalArgumentException if the sequence
         * is not comprised of ATCG bases.
         */
        seq = seq.toUpperCase();
        for (int i = 0; i < seq.length(); i++) {
            char ch = seq.charAt(i);
            if (ch != 'A' && ch != 'T' && ch != 'G' && ch != 'C') {
                String errMesage = "Invalid DNA sequence. Must only contain " +
                                   "A, T, G, C bases.";
                throw new IllegalArgumentException(errMesage);
            }
        }
        this.seq = seq;
    }
    
    /**
    * Part C1.
    * This method returns the length of the DNA sequence as an int.
    */
    public int size() {
        return seq.length(); 
    }

    /**
     * Part C2.
     * This method returns the DNA sequence as a string.
     */
    public String toString(){
        return seq;
    }

    /**
     * This method returns the complement to the DNA sequence object.
     * 
     * @return returns a string complement to the DNA sequence object.
     */
    public String complement(){
        String result = "";
        for (int i = 0; i < seq.length(); i++){
            char val = seq.charAt(i);
            if (val == 'A'){
                result += 'T';
            }
            else if (val == 'T'){
                result += 'A';
            }
            else if (val == 'G'){
                result += 'C';
            }
            else if (val == 'C'){
                result += 'G';
            }
        }
        return result;
    }

    /**
     * Takes a base and returns the numer of times that base occurs in the
       sequence.
     *
     * @param base (a char DNA base)
     * @return an int number of times that base occurs
     */
    // d.  countOccurrences(char base) method
    public int countOccurrences(char base){
        base = Character.toUpperCase(base);;
        int count = 0;
        if (base != 'A' && base != 'T' && base != 'G' && base != 'C'){
            String errMesage = "Invalid base given. Base must be " +
                               "A, T, G, or C.";
            throw new IllegalArgumentException(errMesage); 
        }
        for (int i = 0; i < seq.length(); i++){
            if (seq.charAt(i) == base){
            count ++;
            }
        }
        return count;
    }

    /**
     * Takes a base name and returns the percentage of the sequence
        that is made up of that base as a float.
     * @param base (a char DNA base)
     * @return a double reprencenting the concentration that base
     */
    // e.  percentageOf(char base) method
    public double percentageOf(char base){
        double len = seq.length();
        // to avoid zero division errors as seen in the test file
        if (len == 0){
            return 0.0;
        }
        else{
            return countOccurrences(base) / len;
        }
    }
}

