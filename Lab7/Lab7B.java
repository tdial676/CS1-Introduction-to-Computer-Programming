/**
 * Thierno Diallo
 * 
 * Starter Code for CS 1 21fa Lab 7 Part B.
 * 
 * This is an executable "client" Java program (as opposed to the 
 * DNA class defined in DNA.java). Note that this client
 * program has a main method, which is called when the program
 * is ran from the terminal (or in an IDE), similar to the
 * code ran in an if __name__ == '__main__' branch in a .py program.
 * 
 * If running a .java program in the terminal (assuming you have 
 * java installed), you can run this as follows:
 * 
 * $ javac Lab7B.java
 * $ java Lab7B
 * 
 * Analogous to:
 * $ python3 lab7b.py
 * 
 * The first line compiles the Java program (javac stands for compile Java)
 * The second line runs the compiled Java program, assuming no
 * compiler errors were thrown when compiling (very common to get these
 * when you have errors in your first Java programs). 
 * 
 * Alternatively, you can use the Play -> Run Java button in VSCode,
 * though the first approach can be helpful to get a feel for 
 * the required "compile, then run" process in Java.
 * You can find a Java setup guide on Canvas to get you started as well.
 */
public class Lab7B {
    /**
     * Main method, invoked when this Java program is compiled/ran.
     * The method header syntax is very strict for every main method
     * in an executable Java program; do not change it. 
     * You don't have to worry too much about what it means for the 
     * purposes of this assignment (you'll learn more
     * in CS 2 if you take it and can ask El on Discord/OH).
     */
    public static void main(String[] args) {
        // You can test expressions/Java code here.
        // To print to the terminal, use System.out.println(<value>); 

        // See Lectures 26 and 27 code/videos for more examples/review
        // if you get stuck.

        // Provided example from Part B.1.
        int example = 1 + 2;
        System.out.println(example);
        // Provided examples from Part B.2.
        String result = "foo";
        System.out.println(result);
        // String result = foo;
        // System.out.println(result);
    }

    /**
     * Part B.1. Expressions
     * Write your answers for Part B.1. here.
     * -------------------------------------------------- 
     * Example format of expected answers:
     * #. <expression from spec> // evaluated value
     * 0. 1 + 2 // 3
     * -------------------------------------------------- 
     * 1. 9 - 5 // 4
     * 2. 4 * 2.5 // 10.0
     * 3. 101 / 2 // 50
     * 4. 101 / -2 // -50
     * 5. 101 % 2 // 1
     * 6. 101 % -2 // 1
     * 7. -101 % 2 // -1
     * 8. 101 / -2.0 // -50.5
     * 9. 3 + 4 * 5 // 23
     * 10. (3 + 4) * 5 // 35
     */

    /**
     * Part B.2. String Expressions
     * Write your answers for Part B.2. here.
     * Two examples of what we expect for your answers are provided below,
     * one with a valid assignment and the other with an error.
     * -------------------------------------------------- 
     * Example format of expected answers:
     * 0. String result = "foo";
     * a. "foo" 
     * b. No error
     * c. Aside from the type and ;, Python evaluates "foo" the same as Java.
     * 
     * 0. String result = foo;
     * a. Error 
     * b. Lab7B.java:35: error: cannot find symbol
          String result = foo;
                        ^
          symbol:   variable foo
          location: class Lab7B
     * c. Python and Java have similar errors in this case for missing quotes
     * around characters that are expected to be treated as 
     * String/str values. For example: 
     * 
     *               (you don't have to go this in depth, but you are encouraged 
     *               to indicate that you actually understand the 
     *               error/difference between Java and Python.
     *               
     * >>> result = foo
     * gives an error for an undefined variable/symbol 
       Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
       NameError: name 'foo' is not defined
     * however, this error occurs when the Java program is _compiled_, 
     * whereas Python (which we don't compile) raises the NameError only
     * when the statement is (unsuccessfully) executed. 
     * -------------------------------------------------- 
     * 1. String result = "foo" + 'bar';
     * a. Error
     * b:
     *  Main.java:3: error: unclosed character literal
            String result = "foo" + 'bar';
                                    ^
        Main.java:3: error: unclosed character literal
            String result = "foo" + 'bar';
                                        ^
        Main.java:3: error: not a statement
            String result = "foo" + 'bar';
                                    ^
        3 errors
exit status 1
     * c. This is a unique error to java compared to python where we can add
     *    a single quote string to a double quote string. Also, Jave won't 
     *    accept charecters in single quotes as strings whereas python does,
     *    because in Java single quotes can have only one charecter.
     * -------------------------------------------------- 
     * 2. String result = "foo" + "bar";
     * a. "foobar"
     * b. No error
     * c. Aside from declaring the type and adding the simcollin, python
     * would provide the same result for adding two douple qoute strings.
     * -------------------------------------------------- 
     * 3. String result = "foo"
          String b = "bar"
          String result += b;
     * a. Errors
     * b:
     *  Main.java:3: error: ';' expected
            String result = "foo"
                                ^
        Main.java:4: error: ';' expected
            String b = "bar"
                            ^
        Main.java:5: error: ';' expected
            String result += b;
                        ^
        Main.java:5: error: not a statement
            String result += b;
                            ^
        4 errors
     * c. Unlike python java expect every statement to end with ';' thus
     * there are three errors purely because of that fact. Also, while
     * we can use += to add string to a string in both, like python,
     * java does not require us to redefine the type when adding two already
     * defined types thus its saying we are missing a fourth ';' because it
     * sees two different statements.
     * -------------------------------------------------- 
     * 4. String month = "December";
          int days = 31;
          String result = days + " days hath " + month;
          System.out.println(result);
     * a. "31 days hath December"
     * b. No errors
     * c. Unlike python we do not need a format string or method
     * to add variable to a string in Java. Howver, unlike python,
     * we still have to declare the variable types.
     * -------------------------------------------------- 
     */

     /**
     * Part B.3. String Generation
     * Warm-up:
     * Write your answers for Part B.3.a. and B.3.b. here, 
     * indicating the evaluated result (or an error/what type 
     * if an error is thrown) as well as whether the behavior
     * was different than what you expected.
     * -------------------------------------------------- 
     * a. This gace me varying results deping if I ran it in the
     * java shell or in main class on repleit.com (both of which were allowed),
     * however in both cases I expected an error. The jshel returns an
     * int value of 6650, whearas repleit.com returns an error saying we
     * have a bad operator trying to combine two different types.
     * 
     * b. I expected this to work and print 70 '_', but instead i recived an 
     * error from both the jshell and repleit.com. They both read a bad oprand
     * error arising from trying to combine an int to a string.
     * 
     * -------------------------------------------------- 
     * c. Next, you'll write your first Java method to implement
     * the string multiplication behavior we get with * in Python.
     * We are providing the method stub and documentation to get
     * you started, which you are encouraged to use as reference for
     * the methods you write in Part C.
     * 
     * The equivalent of a Python docstring in Java is called a 
     * javadoc comment. These use multiline comments in the seen format 
     * (_above_) the function, not within. Javadoc comments clearly 
     * indicate parameters and any return value 
     * with @params and @return. The function template 
     * is commented out with // so a compiler error isn't raised 
     * due to placeholders.
     */
     
    /**
     * Function description
     * 
     * @param name1 - description of name1 parameter
     * @param name2 - description of name2 parameter
     * ...
     * @return - description of return value
     */
     // IMPORTANT: Functions (outside of classes) are defined with static
     //            Methods (those you write in Part C) should omit static
     // public static <returnType> fnName(param1Type name1, param2Type name2, ...) {
     //  
     // } 

    /**
     * Part B.3.c.
     * Generates a String result of s repeated n times.
     * Analogous to Python's str * int string-multiplication.
     *
     * @param s - String to multiply
     * @param n - Number of times to multiply s
     * @return - A generated String of n occurrences of s
     */
    public static String stringMultiplier(String s, int n) {
        String result = "";
        for (int i = 0; i < n; i++){
            result += s;
        }
        return result; 
    }
}

