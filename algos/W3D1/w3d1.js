class ArrayStack {
    constructor() {
        this.contents = [];
    }
    // push(value) - adds the given value to the stack
    push(value) {
        this.contents.push(value);
    }

    // pop() - removes the top value from stack and returns it
    pop() {

    }

    // top() - returns the top value without removing it
    top() {

    }

    // contains(target) - returns true if the target value is in the stack,
    // false if not
    contains(target) {

    }


    // isEmpty() - returns true if the stack is empty, false otherwise
    isEmpty() {

    }

    // size() - returns the size of the stack
    size() {

    }

}

// make sure you test all six methods!
// make sure that you test any edge cases you find
push(value) {
    this.contents.push(value);
}

// pop() - removes the top value from stack and returns it
pop() {
    return this.contents.pop();
}

// top() - returns the top value without removing it
top() {
    return this.contents[this.contents.length-1];
}

// contains(target) - returns true if the target value is in the stack,
// false if not
contains(target) {
    for(var i in this.contents){
        if(this.contents[i] == target){
            return true;
        }
    }
    return false;
}


// isEmpty() - returns true if the stack is empty, false otherwise
isEmpty() {
    if(this.contents.length == 0){
        return true;
    }
    else{
        return false;
    }
    // var empty = this.contents.length == 0 ? true : false 
    // return empty
}

// size() - returns the size of the stack
size() {
    return this.contents.length;
}

var x = new ArrayStack();