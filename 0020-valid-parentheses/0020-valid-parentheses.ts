function isValid(s: string): boolean {
    const stack = []
    const closedParenthese = {
        ")":"(",
        "]":"[",
        "}":"{",
    }
    

    for (let parentesis of s){
        if (closedParenthese[parentesis]){
            const lastOpenParenthese = stack.pop()
            if (lastOpenParenthese !== closedParenthese[parentesis]){
                return false
            }
        } else{
            stack.push(parentesis)
        }
    }

    return stack.length === 0


};


