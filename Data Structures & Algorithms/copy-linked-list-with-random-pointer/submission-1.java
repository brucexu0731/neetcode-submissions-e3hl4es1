/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if (head == null){
            return null;
        }
        Node newHead = new Node(head.val);
        Node curr = head;
        Node curr2 = newHead;
        Map<Node, Node> map = new HashMap<>();
        while (curr != null){
            map.put(curr, curr2);
            curr = curr.next;
            curr2.next = curr == null ? null : new Node(curr.val);
            curr2 = curr2.next;
        }
        curr = head;
        curr2 = newHead;
        while (curr != null){
            if (curr.random == null){
                curr2.random = null;
            } else{
                Node random = map.get(curr.random);
                curr2.random = random;
            }
            curr = curr.next;
            curr2 = curr2.next;
        }
        return newHead;
    }
}

