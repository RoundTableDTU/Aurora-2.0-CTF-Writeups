## Keith orders a pizza

We have been given a java code, which does not run, because it does not follow the java principles.
Java needs classes to run and we see no classes in this code, but anyway we encapsulate the code in a class to run.
Now reading through the code, we see that in the main function the strings have been compared using ==. This again does not make sense in java because strings are compared using .equals() in java.
== compares the addresses of the 2 strings which can never be equal, hence lets replace the comparisons from == to .equals.
with that we have our code as
```
import java.util.Scanner;

public class test{
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        String input = s.next();
        if(input.length() != 9)
        {
            System.out.println("WRONG: try again! ");
            input = s.next();
        }
        else
        {
            String solution = change1(change2(input));
            if(solution.equals("djckktjbq"))
                System.out.println("The flag is: " + input);
            else
            {
                System.out.println("WRONG: try again! ");
                input = s.next();
            }
        }
    }
    public static String change1(String w)
    {
        int[] vary = {4, 3, 5, 6, 1, 2, 3, 3, 1};
        char[] temp = new char[9];
        for(int i = 0; i < 9; i++)
        {
            temp[i] = (char)(w.charAt(i) + vary[i]);
        }
        return new String(temp);
    }
    public static String change2(String w)
    {
        int[] vary = {1, 7, 5, 3, 5, 4, 2, 6, 3};
        char[] temp = new char[9];
        for(int i = 0; i < 9; i++)
        {
            temp[i] = (char)(w.charAt(i) - vary[i]);
        }
        return new String(temp);
    }
}
```

Now in this code, the main idea is, that we program takes an input of a string of length 9 and then does some operation via change2 then passes that returned string to change1 and then compares that string to the string `djckktjbq`.
So what we do here is first we reverse the changes done by change1 at each character and then reverse change2. Doing that we will get the string `anchovies` now wrapping it up with the flag format

Flag is `aurora{anchovies}`



//complete