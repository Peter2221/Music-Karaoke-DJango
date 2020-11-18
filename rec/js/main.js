elements = {
    btn: document.getElementById("btn"),
    clips: document.querySelector(".clips")
}

elements.btn.addEventListener("click", ()=>{
    if(!elements.btn.classList.contains('btn--active')) {
        elements.btn.classList.add("btn--active");
        elements.btn.setAttribute("data-state","play");
    } else {
        elements.btn.classList.remove("btn--active");
        elements.btn.setAttribute("data-state","stop");
    }
});

function getButtonState(button) {
    return button.getAttribute("data-state")
}

function addNewRecord(box, src) {
    let newRecord = `
        <audio class="clip" src="${src}" controls></audio>
    `;
    box.insertAdjacentHTML('beforeend',newRecord)
}

if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    console.log('getUserMedia supported.');
    navigator.mediaDevices.getUserMedia (
       {
          audio: true
       })
       .then(function(stream) {
            const mediaRecorder = new MediaRecorder(stream);

            let chunks = [];
            mediaRecorder.ondataavailable = function(e) {
                chunks.push(e.data);
            }

            elements.btn.onclick = function() {
                let state = getButtonState(elements.btn)
                if(state === "play") {
                    mediaRecorder.start()
                    console.log(mediaRecorder.state);
                } else {
                    mediaRecorder.stop()
                    console.log(mediaRecorder.state);

                    const blob = new Blob(chunks, { 'type' : 'audio/ogg; codecs=opus' })
                    chunks = [];
                    const audioURL = window.URL.createObjectURL(blob);
                    elements.clips.innerHTML = "";
                    addNewRecord(elements.clips, audioURL)
                }
            }
            
       })
       .catch(function(err) {
          console.log('The following getUserMedia error occured: ' + err);
       }
    );
 } else {
    console.log('getUserMedia not supported on your browser!');
 }
