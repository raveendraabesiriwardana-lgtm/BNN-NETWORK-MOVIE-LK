let allMovies = [];

// Fetch movie data from json file created by Python Auto-Scraper
async function fetchMovies() {
    try {
        const response = await fetch('movies.json');
        allMovies = await response.json();
        displayMovies(allMovies);
    } catch (error) {
        console.error("Error loading movies:", error);
    }
}

function displayMovies(movies) {
    const grid = document.getElementById('movieGrid');
    grid.innerHTML = '';

    if (movies.length === 0) {
        grid.innerHTML = '<p style="grid-column: 1/-1; text-align: center;">කිසිදු චිත්‍රපටයක් හමු නොවීය.</p>';
        return;
    }

    movies.forEach(movie => {
        const card = document.createElement('div');
        card.className = 'movie-card';
        card.innerHTML = `
            <img src="${movie.poster}" alt="${movie.title}" loading="lazy">
            <div class="movie-info">
                <span class="source-badge">${movie.source}</span>
                <div class="movie-title">${movie.title}</div>
                <a href="${movie.download_link}" target="_blank" class="download-btn" download>
                    <i class="fas fa-download"></i> Download
                </a>
            </div>
        `;
        grid.appendChild(card);
    });
}

function filterSource(source) {
    document.querySelectorAll('.source-nav button').forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');

    if (source === 'all') {
        displayMovies(allMovies);
    } else {
        const filtered = allMovies.filter(m => m.source_code === source);
        displayMovies(filtered);
    }
}

function searchMovies() {
    const query = document.getElementById('searchInput').value.toLowerCase();
    const filtered = allMovies.filter(m => m.title.toLowerCase().includes(query));
    displayMovies(filtered);
}

// Initial Call
fetchMovies();
