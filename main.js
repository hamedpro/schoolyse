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
    let result = {}
    array.forEach(element => {
        if(
            !result[element]
        ){
            result[element] = 1
        }else{
            result[element]++
        }
    });
    return result;
}

class ring{
   value;
   duration_as_minute;
}
class day{
    name;
    rings =[];
}
class class_room{
    name;
    days =[];   

}
class school{
    name;
    class_rooms =[];
}
function bind_analyser_to_ring(ring){
    //accept a ring object
}
function bind_analyser_to_day(day){
    //accept a ring object
    day.data = {
        rings_count : day.rings.count,
        rings_info:countDuplicates(day.rings)
    }
}
function bind_analyser_to_class_room(class_room){
    //accept a ring object

    //calculate and bind all child rings to instance
    class_room.rings = [];
    class_room.days.forEach(day=>{
        day.rings.forEach(ring=>{
            class_room.rings.push(ring.value)
        })
    })
    //bind rings info to instace.data
    class_room.data = {}
    class_room.data.rings_info = countDuplicates(class_room.rings);
}

function bind_analyser_to_school(school){
    //bind analyser to rings
    school.class_rooms.forEach(class_room => {
        class_room.days.forEach(day=>{
            day.rings.forEach(ring=>{
                bind_analyser_to_ring(ring);
            })
        })
    })

    //bind analyser to days
    school.class_rooms.forEach(class_room =>{
        class_room.days.forEach(day => {
            bind_analyser_to_day(day)
        })
    })

    //bind analyser to class_rooms 
    school.class_rooms.forEach(class_room =>{
        bind_analyser_to_class_room(class_room)
    })
}

let amir = new school

let class_205 = new class_room
amir.class_rooms.push(class_205)

let shanbe = new day
shanbe.rings.push(new ring)
shanbe.rings.push(new ring)
amir.class_rooms[0].days.push(shanbe)

bind_analyser_to_school(amir)

function get_plan_as_object(school){
    return JSON.stringify(
        school
    ,null,1)
}
console.log(get_plan_as_object(amir))