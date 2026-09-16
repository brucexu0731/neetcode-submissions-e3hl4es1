/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {
        List<ListNode> nodes = new ArrayList<>();
        ListNode curr = head;
        while(curr != null){
            nodes.add(curr);
            curr = curr.next;
        }
        ListNode dummy = new ListNode(-1);
        curr = dummy;

        int l = 0;
        int r = nodes.size() - 1;

        while (l <= r) {
            curr.next = nodes.get(l);
            curr = curr.next;
            if (l != r) {
                curr.next = nodes.get(r);
                curr = curr.next;
                r --;
            }

            curr.next = null;
            l ++;
        }
    }
}
