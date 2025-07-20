function solution(m, musicinfos) {
  var answer = "";
  // 악보에 사용되는 음 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개

  let code = {
    C: "0",
    "C#": "1",
    D: "2",
    "D#": "3",
    E: "4",
    F: "5",
    "F#": "6",
    G: "7",
    "G#": "8",
    A: "9",
    "A#": "A",
    B: "B",
    "B#": "C",
  };

  // 방금 그곡 : 음악 제목, 시작, 종료 시각, 악보

  const getTime = (start, end) => {
    let [startHour, startMinute] = start.split(":");
    let [endHour, endMinute] = end.split(":");
    return (+endHour - +startHour) * 60 + (+endMinute - +startMinute);
  };

  const codeToStr = sheet => {
    let arr = "";
    for (let i = 0; i < sheet.length - 1; i++) {
      let currentCode = sheet[i];
      let checkSharp = sheet[i + 1];
      let targetCode = "";
      if (checkSharp === "#") {
        targetCode += currentCode + checkSharp;
        i += 1;
      } else {
        targetCode += currentCode;
      }
      arr += code[targetCode];
    }
    if (sheet[sheet.length - 1] !== "#") {
      arr += code[sheet[sheet.length - 1]];
    }
    return arr;
  };
  let ans = [];
  let melodyString = codeToStr(m);

  for (let i = 0; i < musicinfos.length; i++) {
    let musicinfo = musicinfos[i];
    let [start, end, title, sheet] = musicinfo.split(",");
    let playtime = getTime(start, end);
    let codeString = codeToStr(sheet);
    let compareString = "";

    if (codeString.length < playtime) {
      for (let i = 0; i < Math.floor(playtime / codeString.length); i++) {
        compareString += codeString;
      }
      compareString += codeString.slice(0, playtime % codeString.length);
    } else {
      compareString += codeString.slice(0, playtime);
    }

    if (compareString.indexOf(melodyString) !== -1) {
      ans.push([title, playtime, i]);
    }
  }
  ans.sort((a, b) => b[1] - a[1] || a[2] - b[2]);

  if (ans.length === 0) {
    answer = "(None)";
  } else {
    answer = ans[0][0];
  }

  return answer;
}
