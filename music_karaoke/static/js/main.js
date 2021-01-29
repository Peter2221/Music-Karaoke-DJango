elements = {
    btn: document.getElementById("player"),
    clips: document.querySelector(".clips"),
    instrumentalAudio: document.querySelector(".inst-audio"),
    score: document.querySelector(".score"),
    scorePoints: document.querySelector(".score__points"),
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

function changeScore(s) {
    elements.score.classList.remove("score--inactive");
    elements.scorePoints.innerHTML = s.score;
}

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

function getSongId() {
    let currentUrl = window.location.href
    return currentUrl.substring(currentUrl.lastIndexOf('/') + 1);
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
        .then(response => {
            changeScore(response);
            localStorage.setItem('score', response.score.toString());
        })
        .then(() => openRankingModal());
}

function openRankingModal() {
    rankingModal.style.display = "block";
}

function setRankingModalCloseTriggers() {
    let span = rankingModal.getElementsByClassName("close")[0];
    span.onclick = function () {
        closeRankingModal()
    }
    window.onclick = function (event) {
        if (event.target === rankingModal) {
            closeRankingModal()
        }
    }
}

function closeRankingModal() {
    rankingModal.style.display = "none";
}

function saveScoreInRanking() {
    let fd = new FormData();
    fd.append("song_id", getSongId())
    fd.append("score", localStorage.getItem('score'))
    fetch('/ranking/save', {
        method: 'post',
        body: fd
    })
        .then(() => closeRankingModal());
}


let chunks = [];
let rankingModal = document.getElementById("rankingModal");

setRankingModalCloseTriggers()

if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    console.log('getUserMedia supported.');
    navigator.mediaDevices.getUserMedia (
       {
          audio: true
       })
       .then(function(stream) {
            const mediaRecorder = new MediaRecorder(stream);

            mediaRecorder.ondataavailable = function(e) {
                chunks.push(e.data);
            }

            mediaRecorder.onstop = function(e) {
                let blob = new Blob(chunks, { type: 'audio/wav' });
                chunks = [];
                const audioURL = window.URL.createObjectURL(blob);

                elements.clips.innerHTML = "";
                addNewRecord(elements.clips, audioURL)
                sendBlob(blob, '/analysis')
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