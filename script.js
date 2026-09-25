let allMovies = [];

// Fetch movie data from json
async function fetchMovies() {
    try {
        const response = await fetch('movies.json?t=' + new Date().getTime());
        if (!response.ok) {
            throw new Error('movies.json load වුණේ නැත.');
        }
        allMovies = await response.json();
        displayMovies(allMovies);
    } catch (error) {
        console.error("Error loading movies:", error);
        document.getElementById('movieGrid').innerHTML = 
            '<p style="grid-column: 1/-1; text-align: center; color: #ef4444;">Movies Load කිරීමට නොහැකි විය. කරුණාකර movies.json file එක නිවැරදිදැයි පරීක්ෂා කරන්න.</p>';
    }
}

function displayMovies(movies) {
    const grid = document.getElementById('movieGrid');
    grid.innerHTML = '';

    if (!movies || movies.length === 0) {
        grid.innerHTML = '<p style="grid-column: 1/-1; text-align: center;">කිසිදු චිත්‍රපටයක් හමු නොවීය.</p>';
        return;
    }

    movies.forEach(movie => {
        const card = document.createElement('div');
        card.className = 'movie-card';
        card.innerHTML = `
            <img src="${movie.poster}" alt="${movie.title}" loading="lazy" onerror="this.src='https://via.placeholder.com/200x280'">
            <div class="movie-info">
                <span class="source-badge">${movie.source}</span>
                <div class="movie-title">${movie.title}</div>
                <a href="${movie.download_link}" target="_blank" class="download-btn">
                    <i class="fas fa-download"></i> Download Page
                </a>
            </div>
        `;
        grid.appendChild(card);
    });
}

function filterSource(source) {
    document.querySelectorAll('.source-nav button').forEach(btn => btn.classList.remove('active'));
    if(event) event.target.classList.add('active');

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
