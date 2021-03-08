function myRange(loopCount){
    let result = [];
    for(let i = 0;i<loopCount;i++){
        result.push(i)
    }
    return result
}
myRange(5).forEach(Element =>{
    console.log(Element)
})