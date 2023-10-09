/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function hasCycle(head: ListNode | null): boolean {

    const newSet = new Map();
    
    while (head){
        if (newSet.has(head)){
            return true
        } 
        newSet.set(head, true)
        
        head = head.next
        
    }
    
    return false
    
};