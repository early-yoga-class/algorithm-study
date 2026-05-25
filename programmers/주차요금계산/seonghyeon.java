import java.util.*;
import java.time.*;
import java.time.format.DateTimeFormatter;

class Solution {
    static DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HH:mm");
    int basicTime = 0;
    int basicFee = 0;
    int perTime = 0;
    int perFee = 0;
    String IN = "IN";
    String OUT = "OUT";
    
    public int[] solution(int[] fees, String[] records) {
        int[] answer;

        basicTime = fees[0]; basicFee = fees[1];
        perTime = fees[2]; perFee = fees[3];
        
        TreeMap<Integer, Park> map = new TreeMap<>();
        
        for(String str : records){
            String[] splitStr = str.split(" ");
            Integer carNumber= Integer.parseInt(splitStr[1]);
            if(splitStr[2].equals(IN)){
                if(map.containsKey(carNumber)){
                    map.get(carNumber).setInTime(splitStr[0]);
                } else {
                    map.put(carNumber, new Park(carNumber, splitStr[0]));
                }
            }else{
                Park car = map.get(carNumber);
                car.setOutTime(splitStr[0]);
            }
        }
        
        answer = new int[map.size()];
        int idx = 0;
        
        for(Park p : map.values()){
            if(p.inTime != null){
                p.setOutTime("23:59");
            }
            answer[idx++] = p.calculateParkFee();
        }
        
        return answer;
    }
    
    class Park{
        int carNumber = 0;
        LocalTime inTime = null;
        LocalTime outTime = LocalTime.of(23,59);
        long totalTime = 0;
        
        Park(Integer number, String inTime){
            carNumber = number;
            this.inTime = LocalTime.parse(inTime, formatter);
        }
        
        void setInTime(String inTime){
            this.inTime = LocalTime.parse(inTime, formatter);
        }
        
        void setOutTime(String outTime){
            this.outTime = LocalTime.parse(outTime, formatter);
            totalTime += Duration.between(inTime, this.outTime).toMinutes();
            this.inTime = null;
            this.outTime = LocalTime.of(23,59);
        }
    
        
        int calculateParkFee(){
            long diffMinutes = totalTime - basicTime;
            int result = basicFee;

            if(diffMinutes <= 0) return result;

            long temp = diffMinutes / perTime;
            result += (int)temp * perFee;

            if(diffMinutes % perTime != 0){
                result += perFee;
            }

            return result;
        }
        
    }
}
