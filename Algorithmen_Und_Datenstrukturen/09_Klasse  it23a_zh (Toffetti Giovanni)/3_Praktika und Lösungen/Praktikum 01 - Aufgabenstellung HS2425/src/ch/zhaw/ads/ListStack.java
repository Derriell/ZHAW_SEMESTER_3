package ch.zhaw.ads;

import java.util.ArrayList;

public class ListStack implements Stack {
    private ArrayList<Object> stack;

    public ListStack() {
        stack = new ArrayList<>();
    }

    @Override
    public void push(Object x) {
        stack.add(x);
    }

    @Override
    public Object pop() {
        if (isEmpty()) {
            return null;
        }
        return stack.remove(stack.size() - 1);
    }

    @Override
    public boolean isEmpty() {
        return stack.isEmpty();
    }

    @Override
    public Object peek() {
        if (isEmpty()) {
            return null;
        }
        return stack.get(stack.size() - 1);
    }

    @Override
    public boolean isFull() {
        return false; // ArrayList is dynamically sized
    }

    @Override
    public void removeAll() {
        stack.clear();
    }
}