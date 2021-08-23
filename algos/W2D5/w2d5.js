// singly linked lists
// ListNode class: we'll be using this

class ListNode {
    constructor(value) {
      this.value = value;
      this.next = null;
    }
}

// var x = new ListNode(7);

// var y = new ListNode(17);
// x.next = y;

// var z = new ListNode(3);
// y.next = z;

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }
    // addToFront - adds a node with the given value to the head of the list
    addToFront(value) {
        
        var newNode = new ListNode(value);

        if (this.head == null && this.tail == null) {
            this.head = newNode;
            this.tail = newNode;
        }

        else {
            newNode.next = this.head;
            this.head = newNode;
        }

    }
    // addToBack - adds a node with the given value to the tail of the list
    addToBack(value) {
        
        var newNode = new ListNode(value);

        if (this.head == null && this.tail == null) {
            this.head = newNode;
            this.tail = newNode;
        }

        else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
    }
    // contains - returns true if target is in the linked list (as a node value),
    // false otherwise
    contains(target) {
        var runner = this.head;

        while (runner != null) {

            if (runner.value == target) {
                return true;
            }
            runner = runner.next;
        }

        return false;
    }
    
    // display()
    // return a string with the value of every node from the
    // linked list - like "3 - 7 - 13 - 4 - 8"
    display() {
        console.log('starting display');
        if (this.head == null && this.tail == null) {
            return 'empty!'
        }
        var runner = this.head;
        var output = '';

        while (runner != null) {
            if (runner == this.tail) {
                output += runner.value;
            }
            else {
                output += runner.value + ' - ';
            }
            runner = runner.next;
        }

        return output;
    }

    // removeFront() - remove the head of the linked list and
    // return that node's value - not the node itself
    // that means that this.head is going to change as well
    // is there a special case for if the linked list only has two nodes? one node?
    // zero nodes????????

    removeFront() {

        if (this.head == null && this.tail == null) {
            return undefined;
        }

        if (this.head == this.tail) {
            var temp = this.head;
            this.head = null;
            this.tail = null;
            return temp.value;
        }

        var temp = this.head;
        this.head = this.head.next;
        temp.next = null;
        return temp.value;

    }

    // removeBack() - remove the tail of the linked list and return its value
    // again, this means this.tail will change
    // as above - is there a special case for linked lists with a minimal number of
    // nodes inside them?

    removeBack() {

        if (this.head == null && this.tail == null) {
            return undefined;
        }

        if (this.head == this.tail) {
            var temp = this.head;
            this.head = null;
            this.tail = null;
            return temp.value;
        }

        var runner = this.head;

        while (runner != null) {
            if (runner.next == this.tail) {
                var temp = this.tail;
                this.tail = runner;
                this.tail.next = null;
                return temp.value;
            }
            runner = runner.next;
        }
    }

    // findMinNode() - find the node in the linked list with the lowest value
    // and return that node - the node itself, not its value
    // if you find two or more nodes tied for that value,
    // return the first one you find
    findMinNode() {
        if (this.head == null) {
            return null;
        }

        var runner = this.head;
        var currentMin = runner;
        while (runner != null) {

            if (runner.value < currentMin.value) {
                currentMin = runner;
            }

            runner = runner.next;
        }

        return currentMin;
    }

    // findMaxNode() - find the node in the linked list with the highest value
    // and return that node - the node itself, not its value
    // if you find two or more nodes tied for that value,
    // return the first one you find
    findMaxNode() {
        if (this.head == null) {
            return null;
        }

        var runner = this.head;
        var currentMax = runner;
        while (runner != null) {

            if (runner.value > currentMax.value) {
                currentMax = runner;
            }

            runner = runner.next;
        }

        return currentMax;
    }

    // secondToLast() - return the value of the second-to-last node in
    // the linked list
    // what should you do if the list has less than two nodes?
    secondToLast() {
        if (this.head == null || this.head == this.tail) {
            return null;
        }

        else if (this.head.next == this.tail) {
            return this.head.value;
        }

        let runner = this.head;
        while (runner != this.tail) {
            if (runner.next == this.tail) {
                
                
                return runner.value;
            }
            runner = runner.next;
        }
    }

    // moveMinToFront() - take the node with the minimum value in the list
    // and make it the head. do not just swap the values in the nodes!
    // special cases for if it's already the head? or if it's the tail?
    moveMinToFront(){

        var temp = this.findMinNode();

    }

    // moveMaxToBack() - take the node with the maximum value in the list
    // and make it the tail. again, we can't just swap the values in the nodes
    // what if it's already the tail? what if it's the head?
    moveMaxToBack(){

        if (this.head == null && this.tail == null) {
            return undefined;
        }

        var temp = this.findMaxNode();
        var runner = this.head;

        if(temp == this.head){
            this.head = temp.next;
            temp.next = null;
            this.tail.next = temp;
            this.tail = temp;
        }
        else if(temp == this.tail){
            console.log('Maximum val is already at tail.');
        }
        else{
            while(runner.next != temp){
                runner = runner.next;
            }
            runner.next = temp.next;
            this.tail.next = temp;
            this.tail = temp;
            temp.next = null;
        }
    }

    partition(target){
    if (this.head == null && this.tail == null){
        return undefined;
    }
    if (this.head == this.tail){
        return this
    }
    var less_than = [];
    var greater_than = [];
    var in_between = [];
    var runner = this.head;
    while(runner != null){
        if( runner.value < target){
            less_than.push(runner);
        }
        if(runner.value > target){
            greater_than.push(runner);
        }
        if(runner.value == target){
            in_between.push(runner);
        }
        runner = runner.next;
    }
    var final_array = less_than.concat(in_between, greater_than);
    this.head = final_array[0];
    this.tail = final_array[final_array.length - 1];
    for (var i = 0; i < final_array.length ; ++i){
        final_array[i].next = final_array[i+1];
    }
    this.tail.next = null;

    return this

}
    // rearrange the nodes in the list so that all nodes with values less than
    // the target value come first in the list, then all nodes with the target
    // value, then all nodes with values greater than the target value
    // if there are no nodes with values greater or less than the target value,
    // or no nodes with the target value at all, the function should still work
    // if the target is 5, and the list is 8 - 7 - 1 - 5 - 4 - 5 - 2 - 8 - 3
    // the list should rearrange so that the nodes (represented by values)
    // are in this order:
    // 1 - 4 - 2 - 3 - 5 - 5 - 8 - 7 - 8
    // if the target 5, and the list contains:
    // 8 - 1 - 7 - 2 - 4 - 9 - 0 - 1 - 3 - 8
    // the output should be:
    // 1 - 2 - 4 - 0 - 1 - 3 - 8 - 7 - 9 - 8
    // order of nodes does not matter as long as the above rules 
    // for placement are respected
    // remember to fix your head and tail afterwards
    // bonus: can you do it without using an array?
    // other bonus: can you do it without using an array -and- without using
    // another instance(s) of SinglyLinkedList?

    // partition(target) {

    // }
}

// bonus: making these linked lists to test is kind of tedious. what if...
// what if... we had a function (not a method of the SLL class) to make them
// for us?
// generateNewList(length, min_value, max_value) -> creates a new SLL of the
// given length, with nodes containing values from min_value up to max_value
// some random integers may be helpful here

function generateNewList(length = 10, min_value = 0, max_value = 10) {
    var new_sll = new SinglyLinkedList();

    for (var i = 0; i < length; i++) {
        var value = Math.round((Math.random() * (max_value - min_value)) + min_value);
        new_sll.addToBack(value);
    }

    return new_sll;
}

var newSLL = new SinglyLinkedList();
newSLL.addToBack(6);
newSLL.addToBack(5);
newSLL.addToBack(5);
newSLL.addToBack(3);
newSLL.addToBack(32);
newSLL.addToBack(1);
newSLL.addToBack(4);
newSLL.addToBack(5);
newSLL.addToBack(21);
newSLL.addToBack(9);
console.log(newSLL.display());
console.log(newSLL.partition(5));
console.log(newSLL.display());