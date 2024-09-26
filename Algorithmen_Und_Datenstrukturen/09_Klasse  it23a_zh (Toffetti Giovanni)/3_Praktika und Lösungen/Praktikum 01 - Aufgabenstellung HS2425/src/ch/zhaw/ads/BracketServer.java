package ch.zhaw.ads;

import java.util.List;

public class BracketServer {
    List<String> openingBrackets = List.of("(", "[", "{");
    List<String> closingBrackets = List.of(")", "]", "}");

    ListStack stack = new ListStack();

    public boolean checkBrackets(String command) {
        for (int i = 0; i < command.length(); i++) {
            String c = String.valueOf(command.charAt(i));
            if (isOpeningBracket(c)) {
                stack.push(c);
            } else if (isClosingBracket(c)) {
                if (stack.isEmpty() || openingBrackets.indexOf(stack.pop()) != closingBrackets.indexOf(c)) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }

    public String execute(String command) {
        // TODO
        return null;
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

}