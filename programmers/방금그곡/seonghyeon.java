import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public String solution(String m, String[] musicinfos) {
                List<String> strings = Arrays.stream(musicinfos).collect(Collectors.toList());
        Queue<Music> musics = new PriorityQueue<>();
        int count = 1;

        String normalizedM = normalize(m);

        for (String s : strings) {
            String[] split = s.split(",");
            String [] start = split[0].split(":");
            String [] end = split[1].split(":");
            int length = (Integer.parseInt(end[0])-Integer.parseInt(start[0]))*60
                            + (Integer.parseInt(end[1])-Integer.parseInt(start[1]));
            musics.add(new Music(length, split[2], split[3], count++));
        }

        while(!musics.isEmpty()){
            final Music poll = musics.poll();
            String melody = poll.totalMelody();
            if(melody.contains(normalizedM)){
                return poll.musicName;
            }

        }
        return "(None)";
    }
    private static String normalize(String melody) {
        return melody.replace("C#", "c")
                .replace("B#","b")
                .replace("E#","e")
                .replace("D#", "d")
                .replace("F#", "f")
                .replace("G#", "g")
                .replace("A#", "a");
    }

    private static class Music implements Comparable<Music>{
        int recordLength;
        String musicName;
        String melody;
        int num;

        public Music(int recordLength, String musicName, String melody, int num) {
            this.recordLength = recordLength;
            this.musicName = musicName;
            this.melody = melody;
            this.num = num;
        }

        private String normalize(String melody) {
            return melody.replace("C#", "c")
                         .replace("B#","b")
                         .replace("D#", "d")
                         .replace("F#", "f")
                         .replace("G#", "g")
                         .replace("E#","e")
                         .replace("A#", "a");
        }

        public String totalMelody(){
            StringBuilder sb = new StringBuilder();
            String normalizedMelody = normalize(melody);

            for (int i = 0; i < recordLength; i++) {
                sb.append(normalizedMelody.charAt(i % normalizedMelody.length()));
            }
            return sb.toString();
        }

        @Override
        public int compareTo(Music o) {
            if (this.recordLength != o.recordLength) {
                return o.recordLength - this.recordLength;
            }
            return this.num - o.num;
        }
    }
}