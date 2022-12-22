public class DNAClient {
    public static void main(String[] args) {
        // Note: This is just like the if __name__ == "__main__" in Python programs,
        // and is much longer than it should be. However, to avoid confusion we are 
        // just putting the examples from the spec here which you can uncomment/add to
        // when testing your code.

        /*************************************************************
         * Java C.1. Constructor Method (given)
         *************************************************************/
        // The following are valid constructor calls
        DNA dnaSeq1 = new DNA("ATCGatcg");
        DNA dnaSeq2 = new DNA("a");
        DNA dnaSeq3 = new DNA("AaAa");
        DNA dnaSeq4 = new DNA("");
        //DNA dnaSeq5 = new DNA("ACCAGTGTAG");
        DNA dnaSeq6 = new DNA("GCGGCCATGCATGGGG");
        DNA dnaSeq7 = new DNA("ATATATATA");
        DNA dnaSeq8 = new DNA("ATGCCCCTTAAAGAGTTTACATATTGCTGGAGGCGTTAACCCCGG");
        System.out.println(dnaSeq6);
        System.out.println(dnaSeq7);
        System.out.println(dnaSeq8);
        // The following is an invalid private access to a field
        // (different than Python) that will cause a compiler
        // error when _compiled_ 
        // System.out.println(dnaSeq1.seq);

        // The following are invalid constructor calls which 
        // should throw an IllegalArgumentException when uncommented/ran.
        // invalidSeq = new DNA("catdog"); // Runtime error
        // System.out.println(invalidSeq); // unreached

        /*************************************************************
         * Java C.2. toString() and size()
         *************************************************************/
        dnaSeq1.toString();// should give "ATCGATCG"
        dnaSeq1.size(); // should give 8 

        dnaSeq2.toString(); // should give "A"
        dnaSeq2.size(); // should give 1 

        dnaSeq3.toString(); // should give "AAAA"
        dnaSeq3.size(); // should give 4

        dnaSeq4.toString(); // should give ""
        dnaSeq4.size(); // should give 0 

        dnaSeq8.toString(); // should give "ATGCCCCTTAAAGAGTTTACATATTGCTGGAGGCGTTAACCCCGG"
        dnaSeq8.size(); // should give 45

        /*************************************************************
         * Java C.3. complement()
         *************************************************************/
        dnaSeq1.complement(); //should give "TAGCTAGC"
        dnaSeq2.complement();// should give "T"
        dnaSeq3.complement(); // should give "TTTT"
        dnaSeq4.complement(); // should give ""
        DNA dnaSeq5 = new DNA("ACCAGTGTAG");
        String comp5 = dnaSeq5.complement(); // shoudl give "TGGTCACATC"
        DNA doubleCompSeq = new DNA(comp5);
        System.out.println(doubleCompSeq);  // uses toString()
        // TGGTCACATC
        String doubleComp = doubleCompSeq.complement();
        // "ACCAGTGTAG", back to dnaSeq5
        System.out.println(doubleComp);

        /*************************************************************
         * Java C.4. countOccurrences(base)
         *************************************************************/
        dnaSeq1.complement(); // should give "TAGCTAGC"
        dnaSeq2.complement(); // should give "T"
        dnaSeq3.complement(); // should give "A"
        dnaSeq4.complement(); // should give ""
        //DNA dnaSeq5 = new DNA("ACCAGTGTAG");
        //String comp5 = dnaSeq5.complement(); // shoudl give "TGGTCACATC"
        //DNA doubleCompSeq = new DNA(comp5);
        System.out.println(doubleCompSeq);  // uses toString()
        // TGGTCACATC
        //String doubleComp = doubleCompSeq.complement();
        // "ACCAGTGTAG", back to dnaSeq5
        int a1Count = dnaSeq1.countOccurrences('a');
        // 2
        System.out.println(a1Count);
        int t1Count = dnaSeq1.countOccurrences('T');
        // 2
        System.out.println(t1Count);
        int a0Count = dnaSeq2.countOccurrences('A');
        // 1
        System.out.println(a0Count);
        int a3_count = dnaSeq3.countOccurrences('A');
        // 4
        System.out.println(a3_count);
        int a4Count = dnaSeq4.countOccurrences('A');
        // 0
        System.out.println(a4Count);
        int d1Count = dnaSeq1.countOccurrences('d');
        // Exception java.lang.IllegalArgumentException: Invalid base given. Base must be A, T, C, or G.
        // Traceback omitted
        System.out.println(d1Count);
        int c5Count = dnaSeq5.countOccurrences('C');
        // 2
        System.out.println(c5Count);
        int g5Count = dnaSeq5.countOccurrences('G');
        // 3
        System.out.println(g5Count);
        int gc5Count = c5Count + g5Count;
        // 5 
        System.out.println(gc5Count);
        double gc_content = gc5Count * 1.0 / (dnaSeq5).size();
        // 5.0 / 10 -> 0.5 (Lab 1!)
        System.out.println(gc_content);
        /*************************************************************
         * Java C.5. percentageOf(base)
         *************************************************************/
        t1Count = dnaSeq1.countOccurrences('T');
        // 2
        System.out.println(t1Count);
        double t1Percent = dnaSeq1.percentageOf('T');
        // 0.25
        // can't reassign types for an already-defined variable
        System.out.println(t1Percent);
        t1Percent = dnaSeq1.percentageOf('t');
        // 0.25
        System.out.println(t1Percent);
        int a2Count = dnaSeq2.countOccurrences('A');
        // 1
        System.out.println(a2Count);
        double a2Percent = dnaSeq2.percentageOf('A');
        // 1.0
        System.out.println(a2Percent);
        int a3Count = dnaSeq3.countOccurrences('A');
        // 4
        System.out.println(a3Count);
        double a3Percent = dnaSeq3.percentageOf('A');
        // 0.0
        System.out.println(a3Percent);
        a4Count = dnaSeq4.countOccurrences('A');
        // 0
        System.out.println(a4Count);
        double a4Percent = dnaSeq4.percentageOf('A');
        // 0.0
        System.out.println(a4Percent);
        double d1Percent = dnaSeq1.percentageOf('d');
        System.out.println(d1Percent);
        // Exception java.lang.IllegalArgumentException: Invalid base given. Base must be A, T, C, or G.
        // Traceback omitted
    }
}

