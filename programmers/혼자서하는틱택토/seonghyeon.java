class Solution {
    int oCnt = 0;
    int xCnt = 0;
    String[][] game = new String[3][3];

    public int solution(String[] board) {
        int answer = 1;
        for(int i=0;i<3;i++){
            String[] line = board[i].split("");

            for(int j=0;j<3;j++){
                game[i][j] = line[j];

                if(line[j].equals("O")){
                    oCnt++;
                }else if(line[j].equals("X")){
                    xCnt++;
                }
            }
        }

        // 실수 1 확인
        if((oCnt - xCnt > 1) || (oCnt<xCnt)){
            return 0;
        }

        boolean oWin = checkFinish("O");
        boolean xWin = checkFinish("X");

        if (oWin && xWin) return 0;
        if (oWin && oCnt == xCnt) return 0;
        if (xWin && oCnt > xCnt) return 0;
        return answer;
    }

    boolean checkFinish(String p) {
        // 가로, 세로
        for (int i = 0; i < 3; i++) {
            if (game[i][0].equals(p) && game[i][1].equals(p) && game[i][2].equals(p)) return true;
            if (game[0][i].equals(p) && game[1][i].equals(p) && game[2][i].equals(p)) return true;
        }
        // 대각선
        if (game[0][0].equals(p) && game[1][1].equals(p) && game[2][2].equals(p)) return true;
        if (game[0][2].equals(p) && game[1][1].equals(p) && game[2][0].equals(p)) return true;
        return false;
    }
}