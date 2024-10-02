package ch.zhaw.ads;

import java.util.AbstractList;

public class MyList extends AbstractList<Object> {
    private class Node {
        Object data;
        Node next;
        Node prev;

        Node(Object data) {
            this.data = data;
        }
    }

    private Node dummy;
    private int size;

    public MyList() {
        dummy = new Node(null);
        dummy.next = dummy;
        dummy.prev = dummy;
        size = 0;
    }

    @Override
    public boolean add(Object o) {
        Node newNode = new Node(o);
        newNode.next = dummy;
        newNode.prev = dummy.prev;
        dummy.prev.next = newNode;
        dummy.prev = newNode;
        size++;
        return true;
    }

    @Override
    public boolean remove(Object obj) {
        Node current = dummy.next;
        while (current != dummy) {
            if ((obj == null && current.data == null) || (obj != null && obj.equals(current.data))) {
                current.prev.next = current.next;
                current.next.prev = current.prev;
                size--;
                return true;
            }
            current = current.next;
        }
        return false;
    }

    @Override
    public Object get(int pos) {
        if (pos < 0 || pos >= size) {
            throw new IndexOutOfBoundsException();
        }
        Node current = dummy.next;
        for (int i = 0; i < pos; i++) {
            current = current.next;
        }
        return current.data;
    }

    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public void clear() {
        dummy.next = dummy;
        dummy.prev = dummy;
        size = 0;
    }

    @Override
    public Object set(int index, Object element) {
        throw new UnsupportedOperationException();
    }

    @Override
    public void add(int index, Object element) {
        throw new UnsupportedOperationException();
    }

    @Override
    public Object remove(int index) {
        throw new UnsupportedOperationException();
    }
}