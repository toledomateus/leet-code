class LRUCache {
    constructor(capacity) {
        this.capacity = capacity;
        this.cache = new Map()
    }

    get(key) {
        if(this.cache.has(key)) {
            let val = this.cache.get(key)
            this.cache.delete(key)
            this.cache.set(key,val)
            return val;
        } else {
            return -1
        }
    }

    put(key,value) {
        if(this.get(key) === -1) {
            if(this.capacity === this.cache.size) {
                for (let keyVal of this.cache) {
                    this.cache.delete(keyVal[0]);
                    break;
                }
            }
        }
        this.cache.set(key,value)
    }
}