function twoSum(nums: number[], target: number): number[] {
  
    let result = new Map()

    let index = 0
    
    for (let num of nums){
        if (result.has(num)){
            return [result.get(num), index]
        }
        else {
            console.log(num)
            result.set(target - num,index)
            index++;
        }
    }

    return []
    

};