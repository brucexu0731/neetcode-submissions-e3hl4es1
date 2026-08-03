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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        
        ListNode l = null; 
        ListNode r = null; 
        ListNode dummy = new ListNode(-1, head);
        ListNode prevL = dummy;

        ListNode curr = head;
        int counter = 1;
        while(curr != null){
            if (counter == left){
                l = curr;
            }
            if (counter == right){
                r = curr;
                break;
            }
            if (counter == left - 1){
                prevL = curr;
            }
            counter += 1;
            curr = curr.next;
        }
        System.out.println(l.val);
        System.out.println(r.val);

        ListNode nextR = r.next;
        r.next = null;
        ListNode prev = nextR;
        curr = l;
        
        while(curr != null){
            ListNode nxt = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nxt;
        }
        System.out.println(prevL.val);
        System.out.println(prev.val);
        prevL.next = prev;

        return dummy.next;


    }
}