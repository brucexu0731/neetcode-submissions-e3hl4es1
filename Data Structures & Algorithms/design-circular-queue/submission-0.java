class MyCircularQueue {

    private int[] queue;
    private int load = 0;
    private int capacity;
    private int head = 0;
    private int tail = 0;

    public MyCircularQueue(int k) {
        this.queue = new int[k];
        this.capacity = k;
    }
    
    public boolean enQueue(int value) {
        if (isFull()){
            return false;
        }
        this.load += 1;
        this.queue[this.tail] = value;

        if (this.tail == this.queue.length - 1){
            this.tail = 0;
        } else {
            this.tail += 1;
        }
        return true;
    }
    
    public boolean deQueue() {
        if(isEmpty()){
            return false;
        }
        this.load -= 1;
        if (this.head == this.queue.length - 1){
            this.head = 0;
        } else {
            this.head += 1;
        }

        return true;
    }
    
    public int Front() {
        if(isEmpty()){
            return -1;
        }
        return this.queue[this.head];
    }
    
    public int Rear() {
        if(isEmpty()){
            return -1;
        }

        if (this.tail == 0){
            return this.queue[this.queue.length - 1];
        } else {
            return this.queue[this.tail - 1];
        }
    }
    
    public boolean isEmpty() {
        return this.load == 0;
    }
    
    public boolean isFull() {
        return this.load == this.capacity;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */