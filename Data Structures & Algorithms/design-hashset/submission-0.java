class MyHashSet {
    int size=1000;
    LinkedList<Integer>[] buckets;

    public MyHashSet() {
        buckets=new LinkedList[size];
        for(int i=0;i<size;i++)
        buckets[i]=new LinkedList<>();
    }
    public  int getIndex(int key){
        return key%size;
    }
    
    public void add(int key) {
        int index=getIndex(key);
        if(!buckets[index].contains(key))
        buckets[index].add(key);
        
    }
    
    public void remove(int key) {
        int index=getIndex(key);
        buckets[index].remove((Integer)key);
        
    }
    
    public boolean contains(int key) {
        int index=getIndex(key);
        return buckets[index].contains(key);
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */