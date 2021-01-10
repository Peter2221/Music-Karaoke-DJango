elements = {
    btn: document.getElementById("player"),
    clips: document.querySelector(".clips"),
    instrumentalAudio: document.querySelector(".inst-audio"),
}

elements.btn.addEventListener("click", ()=>{
    if(!elements.btn.classList.contains('player--active')) {
        elements.btn.classList.add("player--active");
        elements.btn.setAttribute("data-state","play");
        elements.instrumentalAudio.play();
    } else {
        elements.btn.classList.remove("player--active");
        elements.btn.setAttribute("data-state","stop");
        elements.instrumentalAudio.pause();
        elements.instrumentalAudio.currentTime = 0;
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

function getAudioTrackVocalUrl() {
    return localStorage.getItem('audioFileVocal');
}

function sendBlob(blob, url) {
    let fd = new FormData();
    fd.append("audio_file_vocal", getAudioTrackVocalUrl());
    fd.append("audio_file", blob);
    fetch(url, {
        method: 'post',
        body: fd
    })
    .then(data => data.json())
    .then(score => console.log(score));
}

let chunks = [];

if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    console.log('getUserMedia supported.');
    navigator.mediaDevices.getUserMedia (
       {
          audio: true
       })
       .then(function(stream) {
            const mediaRecorder = new MediaRecorder(stream);

            mediaRecorder.ondataavailable = function(e) {
                console.log('read')
                chunks.push(e.data);
            }

            mediaRecorder.onstop = function(e) {
                let blob = new Blob(chunks, { type: 'audio/wav' });
                chunks = [];
                console.log(blob.size)
                console.log(blob)
                const audioURL = window.URL.createObjectURL(blob);

                elements.clips.innerHTML = "";
                addNewRecord(elements.clips, audioURL)
                sendBlob(blob, "http://127.0.0.1:8000/analysis")
            }

            elements.btn.onclick = function() {
                let state = getButtonState(elements.btn)
                if(state === "play") {
                    mediaRecorder.start()
                } else {
                    mediaRecorder.stop()
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
