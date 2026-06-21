// --- State Management ---
let currentCategory = "";
let currentMenu = "";
let categoriesData = {};
let allRestaurants = [];

// --- DOM Elements ---
const searchInput = document.getElementById("searchInput");
const searchBtn = document.getElementById("searchBtn");
const categoriesGrid = document.getElementById("categoriesGrid");
const menuPillsWrapper = document.getElementById("menuPillsWrapper");
const menuPillsList = document.getElementById("menuPillsList");
const resultsTitle = document.getElementById("resultsTitle");
const resultsCount = document.getElementById("resultsCount");
const restaurantsGrid = document.getElementById("restaurantsGrid");
const loadingState = document.getElementById("loadingState");

// Modals
const detailModal = document.getElementById("detailModal");
const detailModalBody = document.getElementById("detailModalBody");
const closeDetailModal = document.getElementById("closeDetailModal");

const randomModal = document.getElementById("randomModal");
const btnRandomPick = document.getElementById("btnRandomPick");
const closeRandomModal = document.getElementById("closeRandomModal");
const randomCatSelect = document.getElementById("randomCatSelect");
const startRandomBtn = document.getElementById("startRandomBtn");
const slotStrip = document.getElementById("slotStrip");
const randomResultCard = document.getElementById("randomResultCard");
const randomResBadge = document.getElementById("randomResBadge");
const randomResName = document.getElementById("randomResName");
const randomResRating = document.getElementById("randomResRating");
const randomResPrice = document.getElementById("randomResPrice");
const randomResDesc = document.getElementById("randomResDesc");
const viewRandomDetailBtn = document.getElementById("viewRandomDetailBtn");

let selectedRandomResId = null;

// --- Initialize App ---
document.addEventListener("DOMContentLoaded", () => {
    fetchCategories();
    fetchRestaurants();
    setupEventListeners();
});

// --- API Functions ---
async function fetchCategories() {
    try {
        const response = await fetch('/api/categories');
        categoriesData = await response.json();
    } catch (error) {
        console.error("Error fetching categories:", error);
    }
}

async function fetchRestaurants(params = {}) {
    showLoading();
    try {
        const queryString = new URLSearchParams(params).toString();
        const url = `/api/restaurants${queryString ? '?' + queryString : ''}`;
        const response = await fetch(url);
        allRestaurants = await response.json();
        renderRestaurants(allRestaurants);
    } catch (error) {
        console.error("Error fetching restaurants:", error);
        restaurantsGrid.innerHTML = `
            <div class="empty-state">
                <i class="fa-solid fa-triangle-exclamation"></i>
                <p>오류가 발생했습니다. 잠시 후 다시 시도해 주세요.</p>
            </div>
        `;
    }
}

// --- Render Functions ---
function renderRestaurants(restaurants) {
    restaurantsGrid.innerHTML = "";
    resultsCount.textContent = `총 ${restaurants.length}개 식당`;
    
    if (restaurants.length === 0) {
        restaurantsGrid.innerHTML = `
            <div class="empty-state">
                <i class="fa-solid fa-utensils"></i>
                <p>검색 조건에 맞는 맛집이 없습니다.<br>다른 조건으로 검색해 보세요!</p>
            </div>
        `;
        return;
    }

    restaurants.forEach(res => {
        const card = document.createElement("div");
        card.className = "restaurant-card";
        card.setAttribute("id", `resCard-${res.id}`);
        
        // Build tags html (first 3 menu items)
        const tagsHtml = res.menus.slice(0, 3).map(m => `<span class="tag">${m.name}</span>`).join("");
        
        card.innerHTML = `
            <div class="res-img-wrapper">
                <div class="res-img" style="background-image: url('${res.image_url}');"></div>
                <span class="res-badge">${res.category}</span>
            </div>
            <div class="res-card-body">
                <div class="res-card-header">
                    <h3 class="res-title">${res.name}</h3>
                    <div class="res-rating-price">
                        <span class="res-rating"><i class="fa-solid fa-star"></i> ${res.rating.toFixed(1)}</span>
                        <span class="res-price">${res.price_range}</span>
                    </div>
                </div>
                <p class="res-desc">${res.description}</p>
                <div class="res-location">
                    <i class="fa-solid fa-location-dot"></i>
                    <span>${res.location.split(' (')[0]}</span>
                </div>
                <div class="res-tags">
                    ${tagsHtml}
                </div>
            </div>
        `;
        
        card.addEventListener("click", () => openRestaurantDetail(res.id));
        restaurantsGrid.appendChild(card);
    });
}

function renderMenuPills(category) {
    menuPillsList.innerHTML = "";
    currentMenu = "";
    
    if (!category || !categoriesData[category]) {
        menuPillsWrapper.classList.add("hidden");
        return;
    }

    menuPillsWrapper.classList.remove("hidden");
    const menus = categoriesData[category];
    
    // Add "전체" (All) pill
    const allPill = document.createElement("div");
    allPill.className = "pill active";
    allPill.textContent = "전체 메뉴";
    allPill.addEventListener("click", (e) => {
        document.querySelectorAll(".menu-pills .pill").forEach(p => p.classList.remove("active"));
        allPill.classList.add("active");
        currentMenu = "";
        fetchRestaurants({ category: currentCategory });
    });
    menuPillsList.appendChild(allPill);

    // Add specific menu pills
    menus.forEach(menu => {
        const pill = document.createElement("div");
        pill.className = "pill";
        pill.textContent = menu;
        pill.addEventListener("click", () => {
            document.querySelectorAll(".menu-pills .pill").forEach(p => p.classList.remove("active"));
            pill.classList.add("active");
            currentMenu = menu;
            fetchRestaurants({ category: currentCategory, menu: currentMenu });
        });
        menuPillsList.appendChild(pill);
    });
}

function showLoading() {
    restaurantsGrid.innerHTML = "";
    restaurantsGrid.appendChild(loadingState);
}

// --- Event Listeners Setup ---
function setupEventListeners() {
    // Category click handler
    const catCards = document.querySelectorAll(".category-card");
    catCards.forEach(card => {
        card.addEventListener("click", () => {
            const category = card.getAttribute("data-category");
            
            // Search Input clear
            searchInput.value = "";
            
            if (currentCategory === category) {
                // Deactivate category filter
                card.classList.remove("active");
                currentCategory = "";
                resultsTitle.textContent = "모든 맛집 목록";
                renderMenuPills(null);
                fetchRestaurants();
            } else {
                // Activate category filter
                catCards.forEach(c => c.classList.remove("active"));
                card.classList.add("active");
                currentCategory = category;
                resultsTitle.textContent = `${category} 맛집 목록`;
                renderMenuPills(category);
                fetchRestaurants({ category });
            }
        });
    });

    // Search action
    searchBtn.addEventListener("click", executeSearch);
    searchInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
            executeSearch();
        }
    });

    // Logo click reset
    document.getElementById("headerLogo").addEventListener("click", (e) => {
        e.preventDefault();
        resetFilters();
    });

    // Modal Close buttons
    closeDetailModal.addEventListener("click", () => {
        detailModal.classList.add("hidden");
        document.body.style.overflow = "auto";
    });
    
    closeRandomModal.addEventListener("click", () => {
        randomModal.classList.add("hidden");
        document.body.style.overflow = "auto";
    });

    // Open Random Modal
    btnRandomPick.addEventListener("click", () => {
        randomModal.classList.remove("hidden");
        randomResultCard.classList.add("hidden");
        document.body.style.overflow = "hidden";
        // Reset strip
        slotStrip.innerHTML = '<div class="slot-item">어떤 식당일까요?</div>';
        slotStrip.style.transform = 'translateY(0)';
    });

    // Randomize slot button click
    startRandomBtn.addEventListener("click", spinSlotMachine);

    // Detail button from Randomizer
    viewRandomDetailBtn.addEventListener("click", () => {
        if (selectedRandomResId) {
            randomModal.classList.add("hidden");
            openRestaurantDetail(selectedRandomResId);
        }
    });
}

// --- Helper Functions ---
function executeSearch() {
    const query = searchInput.value.trim();
    if (!query) {
        resetFilters();
        return;
    }
    
    // Deactivate categories
    document.querySelectorAll(".category-card").forEach(c => c.classList.remove("active"));
    currentCategory = "";
    renderMenuPills(null);
    
    resultsTitle.textContent = `"${query}" 검색 결과`;
    fetchRestaurants({ search: query });
}

function resetFilters() {
    searchInput.value = "";
    document.querySelectorAll(".category-card").forEach(c => c.classList.remove("active"));
    currentCategory = "";
    currentMenu = "";
    renderMenuPills(null);
    resultsTitle.textContent = "모든 맛집 목록";
    fetchRestaurants();
}

// --- Detail View Logic ---
function openRestaurantDetail(restaurantId) {
    const res = allRestaurants.find(r => r.id === restaurantId);
    if (!res) return;

    // Build menus list html
    const menuListHtml = res.menus.map(m => `
        <div class="menu-list-item">
            <div class="menu-item-info">
                <span class="menu-name">${m.name}</span>
                ${m.is_signature ? '<span class="sig-badge">대표</span>' : ''}
            </div>
            <span class="menu-price">₩${m.price.toLocaleString()}</span>
        </div>
    `).join("");

    detailModalBody.innerHTML = `
        <div class="detail-body-grid">
            <!-- Left Panel -->
            <div class="detail-left">
                <div class="detail-img" style="background-image: url('${res.image_url}');"></div>
                
                <div class="detail-header">
                    <h2 class="detail-title">${res.name}</h2>
                    <div class="detail-meta">
                        <span class="res-badge">${res.category}</span>
                        <span class="res-rating"><i class="fa-solid fa-star text-crimson"></i> ${res.rating.toFixed(1)}</span>
                        <span class="res-price">${res.price_range}</span>
                    </div>
                </div>

                <div class="detail-info-list">
                    <div class="info-item">
                        <i class="fa-solid fa-quote-left"></i>
                        <div class="info-text">
                            <span>${res.description}</span>
                        </div>
                    </div>
                    <div class="info-item">
                        <i class="fa-solid fa-location-dot"></i>
                        <div class="info-text">
                            <strong>위치</strong>
                            <span>${res.location}</span>
                        </div>
                    </div>
                    <div class="info-item">
                        <i class="fa-solid fa-clock"></i>
                        <div class="info-text">
                            <strong>영업 시간</strong>
                            <span>${res.hours}</span>
                        </div>
                    </div>
                    <div class="info-item">
                        <i class="fa-solid fa-phone"></i>
                        <div class="info-text">
                            <strong>전화번호</strong>
                            <span>${res.phone}</span>
                        </div>
                    </div>
                </div>

                <!-- Relative Campus Map -->
                <div class="campus-map-wrapper">
                    <div class="map-title"><i class="fa-solid fa-map"></i> 고려대 캠퍼스 대비 위치</div>
                    <div class="campus-map">
                        <div class="map-bg-grid"></div>
                        <div class="map-landmark main-gate">고대 정문</div>
                        <div class="map-landmark library">중앙도서관</div>
                        <div class="map-landmark station-anam station">안암역 (6호선)</div>
                        <div class="map-landmark science-campus">이공대캠퍼스</div>
                        
                        <!-- Pulse Pin for Restaurant -->
                        <div class="map-restaurant-pin" style="left: ${res.coords.x}%; top: ${res.coords.y}%;"></div>
                        <div class="map-restaurant-label" style="left: ${res.coords.x}%; top: ${res.coords.y}%;">${res.name}</div>
                    </div>
                </div>
            </div>

            <!-- Right Panel: Menu List -->
            <div class="detail-right">
                <h3 class="menu-section-title">메뉴 안내</h3>
                <div class="detail-menu-list">
                    ${menuListHtml}
                </div>
            </div>
        </div>
    `;

    detailModal.classList.remove("hidden");
    document.body.style.overflow = "hidden";
}

// --- "오늘 뭐 먹지?" Slot Machine Spinning Animation ---
async function spinSlotMachine() {
    startRandomBtn.disabled = true;
    randomResultCard.classList.add("hidden");
    
    const cat = randomCatSelect.value;
    
    // Fetch random restaurant from server
    try {
        const url = `/api/random${cat ? '?category=' + cat : ''}`;
        const response = await fetch(url);
        
        if (!response.ok) {
            alert("해당 카테고리의 식당을 찾을 수 없습니다.");
            startRandomBtn.disabled = false;
            return;
        }
        
        const randomRes = await response.json();
        selectedRandomResId = randomRes.id;
        
        // Compile a sequence of random restaurant names for slot rotation
        const spinNames = [];
        const dummyPool = allRestaurants.filter(r => !cat || r.category === cat);
        
        // Generate 15 items for the rotation strip to give a rolling effect
        for (let i = 0; i < 15; i++) {
            const randIndex = Math.floor(Math.random() * dummyPool.length);
            spinNames.push(dummyPool[randIndex].name);
        }
        // Force the last item to be the chosen winner
        spinNames.push(randomRes.name);
        
        // Inject into the slotStrip
        slotStrip.innerHTML = spinNames.map(name => `<div class="slot-item">${name}</div>`).join("");
        
        // Trigger translation
        const itemHeight = 80;
        const totalTravel = (spinNames.length - 1) * itemHeight;
        
        // Apply smooth transition and translateY
        slotStrip.style.transition = 'none';
        slotStrip.style.transform = 'translateY(0)';
        
        // Force reflow
        slotStrip.offsetHeight;
        
        // Animate!
        slotStrip.style.transition = 'transform 2.5s cubic-bezier(0.1, 0.8, 0.2, 1)';
        slotStrip.style.transform = `translateY(-${totalTravel}px)`;
        
        // Wait for animation completion
        setTimeout(() => {
            // Display result details card below the slot machine
            randomResBadge.textContent = randomRes.category;
            randomResName.textContent = randomRes.name;
            randomResRating.innerHTML = `<i class="fa-solid fa-star text-crimson"></i> ${randomRes.rating.toFixed(1)}`;
            randomResPrice.textContent = randomRes.price_range;
            randomResDesc.textContent = randomRes.description;
            
            randomResultCard.classList.remove("hidden");
            startRandomBtn.disabled = false;
        }, 2600);

    } catch (error) {
        console.error("Error rolling random restaurant:", error);
        alert("추천 중 오류가 발생했습니다.");
        startRandomBtn.disabled = false;
    }
}
