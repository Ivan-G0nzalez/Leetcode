function twoSum(numbers: number[], target: number): number[] {
  let possibleResult = new Map();

  for (let i = 0; i < numbers.length; i++) {
    const restNumber = target - numbers[i];
    if (possibleResult.has(restNumber)) {
      return [possibleResult.get(restNumber) +1, i+1];
    } else {
      possibleResult.set(numbers[i], i);
    }
  }

  return [];
};