    // removeFront() - remove the head of the linked list and
    // return that node's value - not the node itself
    // that means that this.head is going to change as well
    // is there a special case for if the linked list only has two nodes? one node?
    // zero nodes????????

    removeFront() {

        if (this.head == null && this.tail == null) {
            return undefined;
        }

    }

    // removeBack() - remove the tail of the linked list and return its value
    // again, this means this.tail will change
    // as above - is there a special case for linked lists with a minimal number of
    // nodes inside them?

    removeBack() {

        if (this.head == null && this.tail == null) {
            return undefined;
        }

    }