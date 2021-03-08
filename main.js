function myRange(loopCount){
    let result = [];
    for(let i = 0;i<loopCount;i++){
        result.push(i)
    }
    return result
}
function compareTwoObject(firstObject,secondObject){
    if(
        Object.keys(firstObject).length!=Object.keys(secondObject).length
    ){
        return false;
    }
    let passedCount = 0;
    Object.keys(firstObject).forEach(element =>{
        if(firstObject[element]==secondObject[element]){
            passedCount++
        }
    })
    if(passedCount == Object.keys(firstObject).length){
        return true;
    }
    return false
}

function countDuplicates(array){
    // make sure about this part : checking if a index exist or not
    let result = {}
    array.forEach(element => {
        if(
            result[element] == null ||
            result[element] == "undefined"
        ){
            result[element] = 1
        }else{
            result[element]++
        }
    });
    return result;
}
limits = {
    shimi:2,
    riazi:3,
    hendese:4
}
class ring{
    duration;
    value;
    constructor(value){
        this.value = value;
    }
    checkResists(){
        
    }
}
class day{
    rings;
    ringsCount;
    constructor(ringsCount){
        this.ringsCount = ringsCount;
    }
    checkResists(){
        
    }
}
class classRoom{
    days;
    ringsAsArray;
    updateComputedVars(){
        this.days.forEach(day => {
            day.rings.forEach(ring=>{
                this.ringsAsArray.push(ring.value)
            })
        });
    }
    className;
    constructor(){

    }
    checkResists(limits){
       if(compareTwoObject(limits,countDuplicates(this.ringsAsArray))){
           return true
       }
       console.log("not passed")
       return false
    }
}
class school{
    classRooms;
    checkResists(){
        let passed;
        
        this.classRooms.forEach(element => {
            if(element.checkResists()){
                this.passed++;
            }
                
        })

        if (passed == this.classRooms.length){
            return true;
        }else{
            return false;
        }
    }
}
function newSchool(
    classRoomsCount,
    daysCount,
    ringsCount
){
    let result =new school;
    myRange(classRoomsCount).forEach(element => {
        result.classRooms.push(new classRoom)
    });
    result.classRooms.forEach(classRoom => {
        classRoom.days.push
    })
    myRange(daysCount).forEach(element => {
        result.classRooms.push(element)
    });
}