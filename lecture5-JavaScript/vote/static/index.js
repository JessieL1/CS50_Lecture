//DOM:Document Object Model
//事件DOMContentLoaded : DOM，整个页面loaded完成
document.addEventListener('DOMContentLoaded',function(){
    console.log("ljx测试--------")
    //Connect to the websocket
    var socket = io.connect(location.protocol + '//' + document.domain +':' + location.port);

    //when connected, configure buttons
    socket.on('connect', () =>{
        document.querySelectorAll('button').forEach(button => {
            button.onclick = ()=> {
                
                const selection = button.dataset.vote;
                socket.emit('submit vote',{'selection':selection});
            };
        });
    });


    socket.on('announce vote', data =>{
        const li = document.createElement('li');
        li.innerHTML = `Vote recorded: ${data.selection}`
        document.querySelector('#votes').append(li);
    });
});

    
