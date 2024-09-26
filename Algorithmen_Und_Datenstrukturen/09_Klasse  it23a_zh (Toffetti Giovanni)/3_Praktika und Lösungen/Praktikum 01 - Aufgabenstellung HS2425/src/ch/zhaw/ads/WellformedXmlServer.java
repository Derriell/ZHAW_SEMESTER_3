package ch.zhaw.ads;

public class WellformedXmlServer implements CommandExecutor {
    ListStack stack = new ListStack();

    public boolean checkWellformed(String command) {
        if (command == null || command.isEmpty()) {
            return false;
        }

        String token;
        while ((token = getNextToken(command)) != null) {
            if (isSelfClosingTag(token)) {
                // Self-closing tags do not need to be pushed to the stack
            } else if (isClosingTag(token)) {
                if (!handleClosingTag(token)) {
                    return false;
                }
            } else if (isOpeningTag(token)) {
                stack.push(token);
            }
            command = command.substring(command.indexOf(token) + token.length());
        }
        return stack.isEmpty();
    }

    private boolean isSelfClosingTag(String token) {
        return token.startsWith("<") && token.endsWith("/>");
    }

    private boolean isClosingTag(String token) {
        return token.startsWith("</") && token.endsWith(">");
    }

    private boolean isOpeningTag(String token) {
        return token.startsWith("<") && token.endsWith(">");
    }

    private boolean handleClosingTag(String token) {
        if (stack.isEmpty()) {
            return false;
        } else {
            String openingTag = (String) stack.pop();
            String expectedClosingTag = "</" + openingTag.substring(1);
            return token.equals(expectedClosingTag);
        }
    }

    private String getNextToken(String command) {
        int start = command.indexOf('<');
        if (start == -1) {
            return null;
        }
        int end = command.indexOf('>', start);
        if (end == -1) {
            return null;
        }

        String tag = command.substring(start, end + 1);

        // Remove attributes if there are any in the tag
        int spaceIndex = tag.indexOf(' ');
        if (spaceIndex != -1) {
            tag = tag.substring(0, spaceIndex) + ">";
        }
        return tag;
    }

    public String execute(String command) {
        return command;
    }
}