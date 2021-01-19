elements = {
    searchBar: document.querySelector(".searchbar__field"),
    songs: document.querySelectorAll(".item"),
}

elements.searchBar.addEventListener('keyup', (e) => {
    // If you want to check after pressing enter key - change event to 'keypress'
    // and in 'if' statement write 'e.key === "Enter"' 
    if(true) {
        let word = e.target.value.toLowerCase();
        elements.songs.forEach(song => {
            let title = song.children[0].children[0].textContent.toLowerCase(); 
            let id = song.id;
            if(title.startsWith(word)) {
                song.style.display = 'block';
            } else {
                song.style.display = 'none';
            }
        })
    }
})
