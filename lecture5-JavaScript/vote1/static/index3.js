document.addEventListener('DOMContentLoaded', () => {
    console.log("jessie test-----------")
    //Connect to the websocket
    var socket = io.connect(location.protocol + '//' + document.domain +':' + location.port);

    //when connected, configure buttons
    socket.on('connect', () =>{
        document.querySelectorAll('button').forEach(button => {
            button.onclick = ()=> {
                console.log("初始化button")
                //alert("hello")
                const selection = button.dataset.vote;
                socket.emit('submit vote',{'selection':selection});
                
            };
        });
    });

    socket.on('vote totals', data => {
        console.log(data)
        document.querySelector('#yes').innerHTML = data.yes;
        document.querySelector('#no').innerHTML = data.no;
        document.querySelector('#maybe').innerHTML = data.maybe;
    }); 
    
    //return false;
       
});

    
