//DOM:Document Object Model
//事件DOMContentLoaded : DOM，整个页面loaded完成
document.addEventListener('DOMContentLoaded',function(){
    //when the button is clicked on, call the count fuction
    document.querySelector('button').onclick = count;
    
});

//define a variable
let counter = 0;

function count(){
    counter++;
    //extract the item that has id with name counter
    //详见CS50.md querySelector的用法  
    document.querySelector('#counter').innerHTML = counter;

    if (counter % 10 ==0){
        alert(`Counter is at ${counter}!`);
    }
}