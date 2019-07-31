import java.util.HashMap;
import java.util.Set;
import java.util.Collection;
import java.util.Map;
public class hashmapdemo{
    public static void main(String []args) {
        HashMap<String,Integer>map=new HashMap<>();
        map.put("India",310);
        map.put("USA",320);
        map.put("England",315);
        map.put("Canada",325);
        map.put("Denmark",330);
        System.out.println(map);
        System.out.println("\n");
        map.put("Sweden",800);
        System.out.println("map after update "+map);
        System.out.println("\n");
         //to get the value through key we have get function
         System.out.println(map.get("India"));
         System.out.println(map.get("RSA"));// when key is not availabel
         System.out.println("\n");
         // to remove any key-value pair we have remove funtion which returns the value and removes the key
        
        System.out.println(map.remove("USA"));
        System.out.println("After remove function"+map);
        System.out.println("\n");
        // to check whether the key is availabel or not we have containsKey function which retrun boolean value 
        System.out.println(map.containsKey("India"));
        System.out.println(map.containsKey("USA"));
        System.out.println("\n");
        // to get an entire key set using keySet method  we will use Set so that duplication will removed
        Set<String> keys=map.keySet();
        for(String key:keys){
            System.out.println(key);
        }
        System.out.println("\n");
        // to get an entire value set using valueSet function we will use collection so that value will allowed to repeat
        Collection<Integer>values=map.values();
        for(Integer value:values){
            System.out.println(value);
        }
        System.out.println("\n");
        // to get all the keys  corresponding its values
        Set<Map.Entry<String, Integer>> entries=map.entrySet();
        for(Map.Entry<String,Integer>entry:entries){
            System.out.println(entry.getKey()+"=>"+entry.getValue());
        }
    }
    
}
