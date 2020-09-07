document.addEventListener('DOMContentLoaded',() =>{
    //when the button is clicked on, call the count fuction
    document.querySelector('#form').onsubmit =() =>{
        //Initialize new request
        const request = new XMLHttpRequest();
        const currency = document.querySelector('#currency').Value;
        request.open('POST','/convert');

        request.onload = () =>{
            //request.responseText:get the text of response when make request
            //JSON.parse:(JavaScript) take the text and parse it into json
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

        // 上面获取了需要展示的信息，但是还未发送到服务器进行显示

        //add data to send with request
        const data = new FormData();
        data.append('currency',currency);

        //send request
        //send data to /convert
        request.send(data)
        return false;
    };
    
});

