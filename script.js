let allMovies = [];

async function fetchMovies() {
    try {
        const response = await fetch('movies.json?t=' + new Date().getTime());
        allMovies = await response.json();
        displayMovies(allMovies);
    } catch (error) {
        console.error("Error loading movies:", error);
    }
}

function displayMovies(movies) {
    const grid = document.getElementById('movieGrid');
    grid.innerHTML = '';

    if (!movies || movies.length === 0) {
        grid.innerHTML = '<p style="grid-column: 1/-1; text-align: center;">චිත්‍රපට හමු නොවීය.</p>';
        return;
    }

    movies.forEach((movie, index) => {
        const card = document.createElement('div');
        card.className = 'movie-card';
        card.innerHTML = `
            <img src="${movie.poster}" alt="${movie.title}" loading="lazy" onerror="this.src='https://via.placeholder.com/200x280/111827/e11d48?text=CineSubz'">
            <div class="movie-info">
                <div class="movie-title">${movie.title}</div>
                <button class="open-download-btn" onclick="openDownloadModal(${index})">
                    <i class="fas fa-download"></i> Direct Download
                </button>
            </div>
        `;
        grid.appendChild(card);
    });
}

function openDownloadModal(index) {
    const movie = allMovies[index];
    document.getElementById('modalTitle').innerText = movie.title;
    document.getElementById('modalPoster').src = movie.poster;

    const linksContainer = document.getElementById('downloadLinksContainer');
    linksContainer.innerHTML = '';

    if (movie.download_links && movie.download_links.length > 0) {
        movie.download_links.forEach(linkObj => {
            const btn = document.createElement('a');
            btn.className = 'direct-dl-btn';
            btn.href = linkObj.url;
            btn.target = '_blank';
            btn.innerHTML = `
                <span><i class="fas fa-file-download"></i> ${linkObj.quality || 'Direct Link'}</span>
                <span>${linkObj.size || 'Download'}</span>
            `;
            linksContainer.appendChild(btn);
        });
    } else {
        linksContainer.innerHTML = `<a href="${movie.page_url}" target="_blank" class="direct-dl-btn" style="justify-content:center;">Visit CineSubz Download Page</a>`;
    }

    document.getElementById('downloadModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('downloadModal').style.display = 'none';
}

function searchMovies() {
    const query = document.getElementById('searchInput').value.toLowerCase();
    const filtered = allMovies.filter(m => m.title.toLowerCase().includes(query));
    displayMovies(filtered);
}

// Initial Fetch
fetchMovies();
