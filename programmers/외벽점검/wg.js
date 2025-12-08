function getPermutation(array, n) {
  let result = []
  if (n === 1) return array.map((el) => [el])
  array.forEach((fixed, index, original) => {
    const rest = [...original.slice(0, index), ...original.slice(index + 1)]
    const perm_rest = getPermutation(rest, n - 1)
    const attached = perm_rest.map((el) => [fixed, ...el])
    result.push(...attached)
  })
  return result
}



function solution(n, weak, dist) {
  var answer = 1e9;
  let linearWeak = []
  //     원형 => 선형으로 만들기
  for (let i = 0; i < weak.length * 2; i++) {
    if (i < weak.length) {
      linearWeak.push(weak[i])
    } else {
      linearWeak.push(weak[i - weak.length] + n)
    }
  }

  //     친구 활용 순서 순열로 만들기
  let permDist = getPermutation(dist, dist.length)

  //     각 순열마다 탐색

  for (let perm of permDist) {
    for (let start = 0; start < weak.length; start++) {
      let count = 1
      let coverage = linearWeak[start] + perm[0]

      for (let i = start; i < start + weak.length; i++) {
        if (linearWeak[i] > coverage) {
          count += 1

          if (count > perm.length) {
            break
          }
          coverage = linearWeak[i] + perm[count - 1]
        }
      }
      answer = Math.min(answer, count)
    }
  }

  if (answer > dist.length) {
    return -1
  } else {
    return answer
  }
}