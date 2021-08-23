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


    findSecondToLast(){
        if (this.head == null || this.head == this.tail){
            return undefined;
        }
        
        var runner = this.head;
        while(runner.next != this.tail){
            runner = runner.next;
        }
        return runner.value;
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

    removeFront() {
        if(this.head == null && this.tail == null){
            return undefined;
        }
        if(this.head == this.tail){
            this.tail = null;
        }
        var temp = this.head;
        this.head = temp.next;
        return temp.value;
    }

    removeBack() {
        if(this.head == null && this.tail == null){
            return undefined;
        }
        var runner = this.head;
        var temp = this.tail;

        if(this.head == this.tail){
            var temp = this.head;
            this.head = null;
            this.tail = null;
            return temp.value;
        }

        var runner = this.head;
        var temp = this.tail;
        while(this.tail != runner.next){
            console.log(runner.value);
            runner = runner.next;
        }
        this.tail = runner;
        runner.next = null;
        return temp.value;
    }
    // moveMinToFront() - take the node with the minimum value in the list
    // and make it the head. do not just swap the values in the nodes!
    // special cases for if it's already the head? or if it's the tail?
    moveMinToFront(){
        var runner = this.head
        var temp = this.findMinNode();
        while(runner != null){
            if (runner.next == temp){
                runner.next == temp.next
            }

        }



    }

    // moveMaxToBack() - take the node with the maximum value in the list
    // and make it the tail. again, we can't just swap the values in the nodes
    // what if it's already the tail? what if it's the head?
    moveMaxToBack(){
        var temp = this.findMaxNode();
        var runner = this. head;
        
        if (this.head == null && this.tail == null){
            return undefined;
        }
        if (temp == this.head){
            this.head = temp.next;
            temp.next = null;
            this.tail.next = temp;
            this.tail = temp;
        }
        else if (temp == this.tail){
            console.log ('max is tail')
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

    // display()
    // return a string with the value of every node from the
    // linked list - like "3 - 7 - 13 - 4 - 8"
    display() {
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
}

function generateNewList(length, min_value, max_value){
    var newSLL = new SinglyLinkedList();

    for(var i = 0; i < length; ++i){
        newSLL.addToFront(Math.floor(Math.random()*(max_value-min_value))+min_value);
    }
    console.log(newSLL.display());
    return newSLL
}


var newSLL = new SinglyLinkedList();
newSLL.addToBack(27);
newSLL.addToFront(8);
newSLL.addToFront(4);
newSLL.addToFront(13);
newSLL.addToFront(7);
newSLL.addToFront(3);
newSLL.addToBack(14);
newSLL.addToBack(26);

// console.log(newSLL.contains(13));
// console.log(newSLL.contains(99));

// console.log(newSLL.display());
// newSLL.removeFront();
// newSLL.removeBack();
console.log(newSLL.display());
console.log(newSLL.moveMaxToBack)

// console.log(newSLL.findMinValue());
// console.log('')
// console.log(newSLL.findMaxValue());
// console.log('')
// console.log(newSLL.findSecondToLast());

// generateNewList(4, 20, 25);