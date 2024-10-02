package ch.zhaw.ads;

import java.util.Stack;

public class BracketServer {
    private static final String[] openingBrackets = {"(", "[", "{", "<", "/*"};
    private static final String[] closingBrackets = {")", "]", "}", ">", "*/"};

    public boolean checkBrackets(String input) {
        Stack<String> stack = new Stack<>();
        for (int i = 0; i < input.length(); i++) {
            String c = String.valueOf(input.charAt(i));
            if (i < input.length() - 1 && c.equals("/") && input.charAt(i + 1) == '*') {
                c = "/*";
                i++;
            } else if (i < input.length() - 1 && c.equals("*") && input.charAt(i + 1) == '/') {
                c = "*/";
                i++;
            }

            if (isOpeningBracket(c)) {
                stack.push(c);
            } else if (isClosingBracket(c)) {
                if (stack.isEmpty() || !matches(stack.pop(), c)) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }

    private boolean isOpeningBracket(String c) {
        for (String openingBracket : openingBrackets) {
            if (c.equals(openingBracket)) {
                return true;
            }
        }
        return false;
    }

    private boolean isClosingBracket(String c) {
        for (String closingBracket : closingBrackets) {
            if (c.equals(closingBracket)) {
                return true;
            }
        }
        return false;
    }

    private boolean matches(String open, String close) {
        for (int i = 0; i < openingBrackets.length; i++) {
            if (openingBrackets[i].equals(open) && closingBrackets[i].equals(close)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        BracketServer server = new BracketServer();
        System.out.println(server.checkBrackets("[(3 +3)* 35 +3]* {3 +2}")); // should print true
        System.out.println(server.checkBrackets("<(<>)>")); // should print true
        System.out.println(server.checkBrackets("/*/* */")); // should print false
        System.out.println(server.checkBrackets("/*")); // should print false
        System.out.println(server.checkBrackets("/* hallo */")); // should print true
    }
}