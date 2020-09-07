//DOM:Document Object Model
//事件DOMContentLoaded : DOM，整个页面loaded完成
document.addEventListener('DOMContentLoaded',function(){
    //when the button is clicked on, call the count fuction
    document.querySelector('#form').onsubmit =() =>{
        //Initialize new request
        const request = new XMLHttpRequest();
        const currency = document.querySelector('%currency').nodeValue;
        request.open('POST','/convert');

        request.onload = () =>{
            const data = JSON.parse(request.responseText);

            //update the result div
            if (data.success) {
                const contents = `1 USD is equal to ${data.rate} ${currency}`
                document.querySelector('#result').innerHTML = contents;
            }
            else{
                document.querySelector('#result').innerHTML = 'There is an error';
            }
        }

        //add data to send with request
        const data = new FormData();
        data.append('currency',currency);

        //send request
        request.send(data)
        return false;
    };
    
});

