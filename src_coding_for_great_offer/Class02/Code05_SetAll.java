package Class02;

import java.util.HashMap;

public class Code05_SetAll {

    public static class MyValue<V> {//V 表示是一个泛型（表示value可以是任意的类型）
        public V value;//存储泛型的值
        public long time;//存储时间戳

        public MyValue(V v, long t) {
            value = v;
            time = t;
        }
    }

    public static class MyHashMap<K, V> {//加了时间戳和全量设置值的功能
        private HashMap<K, MyValue<V>> map;
        private long time;
        private MyValue<V> setAll;

        //支持记录每个键值对的存储时间，并且支一次性为所有键设置相同的功能
        public MyHashMap() {
            map = new HashMap<>();
            time = 0;
            setAll = new MyValue<V>(null, -1);
        }

        public void put(K key, V value) {
            map.put(key, new MyValue<V>(value, time++));
        }

        public void setAll(V value) {
            setAll = new MyValue<V>(value, time++);
        }

        public V get(K key) {
            if (!map.containsKey(key)) {
                return null;
            }
            if (map.get(key).time > setAll.time) {
                return map.get(key).value;
            } else {
                return setAll.value;
            }
        }
    }
}
