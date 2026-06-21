// --- Restaurant Data Embedded Directly (Serverless / Static Site friendly) ---
const RESTAURANTS = [
    {
        "id": 1,
        "name": "고른햇살",
        "category": "분식",
        "menus": [
            {"name": "참치김밥", "price": 4500, "is_signature": true},
            {"name": "야채김밥", "price": 3500, "is_signature": false},
            {"name": "라볶이", "price": 5500, "is_signature": true},
            {"name": "토종순대", "price": 5000, "is_signature": false},
            {"name": "치즈라볶이", "price": 6500, "is_signature": false}
        ],
        "price_range": "₩",
        "rating": 4.8,
        "location": "참살이길 (안암역 3번출구 도보 3분)",
        "coords": {"x": 48, "y": 62},
        "hours": "매일 06:30 - 23:30",
        "phone": "02-953-3394",
        "description": "고대생들의 영원한 소울푸드 분식집. 참치가 밥보다 많이 들어간 주먹만 한 크기의 참치김밥과 매콤달콤한 라볶이가 대표 메뉴입니다. 가성비 최강을 자랑합니다.",
        "image_url": "static/images/food_snack.jpg"
    },
    {
        "id": 2,
        "name": "야마토텐동",
        "category": "일식",
        "menus": [
            {"name": "에비텐동 (새우튀김덮밥)", "price": 11500, "is_signature": true},
            {"name": "토리텐동 (닭고기튀김덮밥)", "price": 10500, "is_signature": true},
            {"name": "부타텐동 (돼지고기튀김덮밥)", "price": 11000, "is_signature": false},
            {"name": "규동 (소고기덮밥)", "price": 9000, "is_signature": false}
        ],
        "price_range": "₩₩",
        "rating": 4.7,
        "location": "안암역 골목 (안암역 3번출구 도보 4분)",
        "coords": {"x": 54, "y": 55},
        "hours": "매일 11:00 - 21:00 (브레이크타임 15:00 - 17:00)",
        "phone": "02-6348-1008",
        "description": "겉바속촉의 정석, 바삭하고 진한 소스 맛이 일품인 안암 최고의 텐동 전문점. 일본 현지 식당에 온 듯한 아늑하고 특색 있는 인테리어 속에서 식사를 즐길 수 있습니다.",
        "image_url": "static/images/food_japanese.jpg"
    },
    {
        "id": 3,
        "name": "용초수",
        "category": "중식",
        "menus": [
            {"name": "꿔바로우 (찹쌀탕수육)", "price": 16000, "is_signature": true},
            {"name": "호남볶음밥", "price": 8500, "is_signature": true},
            {"name": "우육면", "price": 8500, "is_signature": false},
            {"name": "사천짬뽕", "price": 9000, "is_signature": false}
        ],
        "price_range": "₩₩",
        "rating": 4.6,
        "location": "정대후문 (안암역 2번출구 도보 2분)",
        "coords": {"x": 42, "y": 50},
        "hours": "매일 11:00 - 21:30 (일요일 휴무)",
        "phone": "02-922-7991",
        "description": "새콤달콤한 소스와 쫄깃한 식감이 완벽한 꿔바로우와, 불맛 가득하고 은근히 매콤한 중국식 호남볶음밥의 조합이 훌륭합니다. 정대후문의 최강 맛집 중 하나입니다.",
        "image_url": "static/images/food_chinese.jpg"
    },
    {
        "id": 4,
        "name": "무르무르드구스토",
        "category": "양식",
        "menus": [
            {"name": "통삼겹 로제 파스타", "price": 18500, "is_signature": true},
            {"name": "마르게리따 화덕 피자", "price": 19000, "is_signature": false},
            {"name": "채끝 등심 스테이크", "price": 29000, "is_signature": true},
            {"name": "트러플 크림 리조또", "price": 17500, "is_signature": false}
        ],
        "price_range": "₩₩₩",
        "rating": 4.5,
        "location": "안암역 대로변 (안암역 3번출구 바로 옆 건물 4층)",
        "coords": {"x": 49, "y": 58},
        "hours": "매일 11:30 - 21:30 (브레이크타임 15:00 - 17:00)",
        "phone": "02-928-0683",
        "description": "안암에서 분위기 좋은 데이트 코스나 소개팅 장소를 찾는다면 단연 첫손에 꼽히는 이탈리안 레스토랑. 고급스러운 인테리어와 훌륭한 플레이팅의 파스타, 피자를 선사합니다.",
        "image_url": "static/images/food_western.jpg"
    },
    {
        "id": 5,
        "name": "어흥식당",
        "category": "양식",
        "menus": [
            {"name": "어흥 스테이크 (소고기)", "price": 10900, "is_signature": true},
            {"name": "치즈 함박 스테이크", "price": 9900, "is_signature": true},
            {"name": "매콤 베이컨 크림 파스타", "price": 8900, "is_signature": false},
            {"name": "어흥 불고기 덮밥", "price": 8500, "is_signature": false}
        ],
        "price_range": "₩₩",
        "rating": 4.7,
        "location": "제기동 골목 (안암역 3번출구 도보 5분)",
        "coords": {"x": 58, "y": 68},
        "hours": "매일 11:30 - 21:00 (브레이크타임 14:30 - 17:00)",
        "phone": "02-923-5250",
        "description": "달궈진 뜨거운 철판 위에 직접 익혀 먹는 갓성비 스테이크 전문점. 푸짐하고 육즙 가득한 소고기 부채살 스테이크와 함박 스테이크가 학생들에게 선풍적인 인기를 끌고 있습니다.",
        "image_url": "static/images/food_western.jpg"
    },
    {
        "id": 6,
        "name": "특별식당",
        "category": "일식",
        "menus": [
            {"name": "오야코동 (닭고기달걀덮밥)", "price": 8500, "is_signature": true},
            {"name": "규동 (소고기덮밥)", "price": 9000, "is_signature": false},
            {"name": "사케동 (생연어덮밥)", "price": 13500, "is_signature": true},
            {"name": "에비카레 (새우튀김카레)", "price": 9500, "is_signature": false}
        ],
        "price_range": "₩₩",
        "rating": 4.6,
        "location": "법대후문 인근 (안암역 1번출구 도보 6분)",
        "coords": {"x": 30, "y": 42},
        "hours": "월~금 11:30 - 20:30 (토, 일요일 휴무)",
        "phone": "02-921-2525",
        "description": "고려대학교 법대후문 언덕 너머 아담하고 편안한 덮밥 전문점. 사장님의 정성 어린 손길이 담긴 소스와 따끈하고 풍부한 토핑 덮밥 한 그릇이 기분 좋은 든든함을 줍니다.",
        "image_url": "static/images/food_japanese.jpg"
    },
    {
        "id": 7,
        "name": "비나레스토랑",
        "category": "양식",
        "menus": [
            {"name": "치킨 마크니 커리", "price": 12000, "is_signature": true},
            {"name": "버터 난", "price": 3000, "is_signature": true},
            {"name": "탄두리 치킨 (반마리)", "price": 10000, "is_signature": false},
            {"name": "팔락 파니르 (시금치커리)", "price": 11000, "is_signature": false}
        ],
        "price_range": "₩₩",
        "rating": 4.8,
        "location": "참살이길 (안암역 2번출구 도보 2분)",
        "coords": {"x": 45, "y": 52},
        "hours": "매일 11:00 - 21:00",
        "phone": "02-928-2190",
        "description": "네팔/인도 현지 셰프가 직접 화덕에 굽는 난과 진하고 풍미 깊은 전통 커리를 선보입니다. 달콤하고 부드러운 치킨 마크니 커리와 버터 갈릭 난의 조화는 최고입니다.",
        "image_url": "static/images/food_western.jpg"
    },
    {
        "id": 8,
        "name": "언니네식당 (언니네반찬가게)",
        "category": "한식",
        "menus": [
            {"name": "제육볶음 정식", "price": 8000, "is_signature": true},
            {"name": "순두부찌개", "price": 7500, "is_signature": false},
            {"name": "치즈 계란말이", "price": 6000, "is_signature": true},
            {"name": "된장찌개 정식", "price": 7500, "is_signature": false}
        ],
        "price_range": "₩",
        "rating": 4.6,
        "location": "정대후문 골목 (안암역 2번출구 도보 3분)",
        "coords": {"x": 38, "y": 48},
        "hours": "월~금 10:30 - 20:00 (토요일 휴무)",
        "phone": "02-927-3330",
        "description": "집밥이 그리운 자취 대학생들에게 든든한 안식처가 되어주는 백반집. 매일 매장에서 직접 만드는 건강한 반찬들과 불향 나는 매콤달콤 제육볶음은 언제 먹어도 질리지 않습니다.",
        "image_url": "static/images/food_korean.jpg"
    },
    {
        "id": 9,
        "name": "삼통치킨 본점",
        "category": "분식",
        "menus": [
            {"name": "마늘치킨", "price": 20000, "is_signature": true},
            {"name": "후라이드 치킨", "price": 18000, "is_signature": false},
            {"name": "양념 치킨", "price": 19000, "is_signature": false},
            {"name": "골뱅이 소면", "price": 18000, "is_signature": false}
        ],
        "price_range": "₩₩",
        "rating": 4.5,
        "location": "안암오거리 (안암역 3번출구 도보 6분)",
        "coords": {"x": 55, "y": 78},
        "hours": "매일 12:00 - 익일 02:00",
        "phone": "02-922-0056",
        "description": "고려대 학생들이 축제 때나 동아리 뒤풀이 때 무조건 찾는 안암오거리의 전설적인 치킨집. 알싸하면서 달달한 소스가 뜨겁게 코팅된 촉촉한 마늘치킨이 시그니처입니다.",
        "image_url": "static/images/food_snack.jpg"
    },
    {
        "id": 10,
        "name": "춘자",
        "category": "분식",
        "menus": [
            {"name": "짜장라볶이", "price": 7000, "is_signature": true},
            {"name": "요구르트 소주", "price": 6000, "is_signature": true},
            {"name": "치즈감자튀김", "price": 8000, "is_signature": false},
            {"name": "바지락 조개탕", "price": 10000, "is_signature": false}
        ],
        "price_range": "₩",
        "rating": 4.5,
        "location": "참살이길 골목 (안암역 3번출구 도보 4분)",
        "coords": {"x": 44, "y": 64},
        "hours": "매일 17:00 - 익일 02:00",
        "phone": "02-929-2771",
        "description": "안암을 거쳐 간 고대생치고 춘자에서 요구르트 소주 한 잔 마시지 않은 사람이 없다고 할 만큼 상징적인 민속 주점이자 퓨전 분식집. 가성비 안주 라볶이와 달달한 요주가 대표적입니다.",
        "image_url": "static/images/food_snack.jpg"
    },
    {
        "id": 11,
        "name": "희정부대찌개",
        "category": "한식",
        "menus": [
            {"name": "부대찌개 (1인분)", "price": 9000, "is_signature": true},
            {"name": "철판 티본스테이크", "price": 35000, "is_signature": false},
            {"name": "모둠사리 추가", "price": 4000, "is_signature": false}
        ],
        "price_range": "₩₩",
        "rating": 4.5,
        "location": "제기동 방향 (안암역 4번출구 도보 5분)",
        "coords": {"x": 68, "y": 55},
        "hours": "매일 11:30 - 22:00",
        "phone": "02-924-4694",
        "description": "진하고 묵직한 사골 베이스의 육수에 햄과 소시지, 민찌 고기가 푸짐하게 들어가 끓일수록 진한 맛을 내는 얼큰 부대찌개 전문점입니다. 해장용 점심식사로 인기가 많습니다.",
        "image_url": "static/images/food_korean.jpg"
    },
    {
        "id": 12,
        "name": "백소정 안암점",
        "category": "일식",
        "menus": [
            {"name": "돈카츠 (등심)", "price": 10500, "is_signature": false},
            {"name": "마제소바", "price": 9900, "is_signature": true},
            {"name": "마제소바+돈카츠 세트", "price": 14900, "is_signature": true},
            {"name": "냉소바+돈카츠 세트", "price": 14500, "is_signature": false}
        ],
        "price_range": "₩₩",
        "rating": 4.6,
        "location": "참살이길 입구 (안암역 3번출구 도보 2분)",
        "coords": {"x": 50, "y": 60},
        "hours": "매일 11:00 - 21:00 (브레이크타임 15:00 - 17:00)",
        "phone": "02-921-0105",
        "description": "특제 비빔소스를 버무려 먹는 꾸덕하고 매콤고소한 마제소바와, 도톰하고 튀김옷이 바삭하게 살아있는 일식 돈카츠의 기분 좋은 세트 조합이 점심 식사로 각광받는 곳입니다.",
        "image_url": "static/images/food_japanese.jpg"
    },
    {
        "id": 13,
        "name": "용두동할매쭈꾸미 안암점",
        "category": "한식",
        "menus": [
            {"name": "웰빙 쭈꾸미 (1인분)", "price": 14000, "is_signature": true},
            {"name": "삼겹살 사리 추가", "price": 7000, "is_signature": false},
            {"name": "날치알 볶음밥", "price": 3000, "is_signature": true}
        ],
        "price_range": "₩₩",
        "rating": 4.7,
        "location": "안암오거리 이면도로 (안암역 3번출구 도보 7분)",
        "coords": {"x": 58, "y": 82},
        "hours": "매일 11:30 - 23:00",
        "phone": "02-927-4148",
        "description": "매콤하고 자극적인 양념의 통통한 쭈꾸미를 철판에 볶아 마요네즈 소스나 천사채와 깻잎에 싸서 먹는 중독성 높은 매운맛 맛집. 마무리 날치알 볶음밥은 고대생 국룰 코스입니다.",
        "image_url": "static/images/food_korean.jpg"
    },
    {
        "id": 14,
        "name": "어머니대성집",
        "category": "한식",
        "menus": [
            {"name": "해장국 (보통)", "price": 12000, "is_signature": true},
            {"name": "육회비빔밥", "price": 17000, "is_signature": true},
            {"name": "모둠수육", "price": 40000, "is_signature": false}
        ],
        "price_range": "₩₩₩",
        "rating": 4.8,
        "location": "신설동 방향 (안암역 도보 15분 / 제기동 인근)",
        "coords": {"x": 80, "y": 90},
        "hours": "매일 06:00 - 익일 04:00 (브레이크타임 15:00 - 18:00)",
        "phone": "02-923-1718",
        "description": "서울 최고의 해장국 노포 맛집 중 하나. 맑고 깊은 양지 육수에 잘게 다진 부드러운 양지와 선지, 토렴된 밥이 어우러져 해장은 물론 최고의 한 끼 든든함을 선물합니다.",
        "image_url": "static/images/food_korean.jpg"
    },
    {
        "id": 15,
        "name": "성북동돈까스",
        "category": "일식",
        "menus": [
            {"name": "경양식 왕돈까스", "price": 9500, "is_signature": true},
            {"name": "매운 돈까스", "price": 10000, "is_signature": false},
            {"name": "생선까스", "price": 10000, "is_signature": false},
            {"name": "반반 돈까스", "price": 10500, "is_signature": true}
        ],
        "price_range": "₩",
        "rating": 4.4,
        "location": "이공대 후문 부근 (안암역 4번출구 도보 4분)",
        "coords": {"x": 58, "y": 40},
        "hours": "매일 10:30 - 21:00",
        "phone": "02-921-2555",
        "description": "추억의 양념 소스가 듬뿍 뿌려진 커다란 경양식 돈까스를 제공합니다. 따끈한 식전 수프와 밥이 무료 리필되며 가격 대비 아주 푸짐한 양으로 이공계 학생들의 사랑을 듬뿍 받습니다.",
        "image_url": "static/images/food_japanese.jpg"
    }
];

const CATEGORIES_WITH_MENUS = {
    "한식": ["제육볶음", "순두부찌개", "부대찌개", "해장국", "쭈꾸미삼겹살", "김치찌개", "육회비빔밥"],
    "중식": ["꿔바로우", "호남볶음밥", "우육면"],
    "일식": ["텐동", "규동", "오야코동", "사케동", "돈카츠", "마제소바"],
    "양식": ["파스타", "피자", "스테이크", "리조또", "커리"],
    "분식": ["김밥", "라볶이", "순대", "치킨", "짜장라볶이"]
};

// --- State Management ---
let currentCategory = "";
let currentMenu = "";
let allFilteredRestaurants = [...RESTAURANTS];

// --- DOM Elements ---
const searchInput = document.getElementById("searchInput");
const searchBtn = document.getElementById("searchBtn");
const categoriesGrid = document.getElementById("categoriesGrid");
const menuPillsWrapper = document.getElementById("menuPillsWrapper");
const menuPillsList = document.getElementById("menuPillsList");
const resultsTitle = document.getElementById("resultsTitle");
const resultsCount = document.getElementById("resultsCount");
const restaurantsGrid = document.getElementById("restaurantsGrid");

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
    filterRestaurants();
    setupEventListeners();
});

// --- Serverless Core Filter Function ---
function filterRestaurants() {
    let results = [...RESTAURANTS];
    const query = searchInput.value.trim().toLowerCase();

    if (currentCategory) {
        results = results.filter(r => r.category === currentCategory);
    }

    if (currentMenu) {
        results = results.filter(r => {
            return r.menus.some(m => m.name.toLowerCase().includes(currentMenu.toLowerCase()));
        });
    }

    if (query) {
        results = results.filter(r => {
            const nameMatch = r.name.toLowerCase().includes(query);
            const descMatch = r.description.toLowerCase().includes(query);
            const locMatch = r.location.toLowerCase().includes(query);
            const menuMatch = r.menus.some(m => m.name.toLowerCase().includes(query));
            return nameMatch || descMatch || locMatch || menuMatch;
        });
    }

    allFilteredRestaurants = results;
    renderRestaurants(results);
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
    
    if (!category || !CATEGORIES_WITH_MENUS[category]) {
        menuPillsWrapper.classList.add("hidden");
        return;
    }

    menuPillsWrapper.classList.remove("hidden");
    const menus = CATEGORIES_WITH_MENUS[category];
    
    const allPill = document.createElement("div");
    allPill.className = "pill active";
    allPill.textContent = "전체 메뉴";
    allPill.addEventListener("click", () => {
        document.querySelectorAll(".menu-pills .pill").forEach(p => p.classList.remove("active"));
        allPill.classList.add("active");
        currentMenu = "";
        filterRestaurants();
    });
    menuPillsList.appendChild(allPill);

    menus.forEach(menu => {
        const pill = document.createElement("div");
        pill.className = "pill";
        pill.textContent = menu;
        pill.addEventListener("click", () => {
            document.querySelectorAll(".menu-pills .pill").forEach(p => p.classList.remove("active"));
            pill.classList.add("active");
            currentMenu = menu;
            filterRestaurants();
        });
        menuPillsList.appendChild(pill);
    });
}

// --- Event Listeners Setup ---
function setupEventListeners() {
    const catCards = document.querySelectorAll(".category-card");
    catCards.forEach(card => {
        card.addEventListener("click", () => {
            const category = card.getAttribute("data-category");
            searchInput.value = "";
            
            if (currentCategory === category) {
                card.classList.remove("active");
                currentCategory = "";
                resultsTitle.textContent = "모든 맛집 목록";
                renderMenuPills(null);
                filterRestaurants();
            } else {
                catCards.forEach(c => c.classList.remove("active"));
                card.classList.add("active");
                currentCategory = category;
                resultsTitle.textContent = `${category} 맛집 목록`;
                renderMenuPills(category);
                filterRestaurants();
            }
        });
    });

    searchBtn.addEventListener("click", () => {
        executeSearch();
    });
    searchInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
            executeSearch();
        }
    });

    document.getElementById("headerLogo").addEventListener("click", (e) => {
        e.preventDefault();
        resetFilters();
    });

    closeDetailModal.addEventListener("click", () => {
        detailModal.classList.add("hidden");
        document.body.style.overflow = "auto";
    });
    
    closeRandomModal.addEventListener("click", () => {
        randomModal.classList.add("hidden");
        document.body.style.overflow = "auto";
    });

    btnRandomPick.addEventListener("click", () => {
        randomModal.classList.remove("hidden");
        randomResultCard.classList.add("hidden");
        document.body.style.overflow = "hidden";
        slotStrip.innerHTML = '<div class="slot-item">어떤 식당일까요?</div>';
        slotStrip.style.transform = 'translateY(0)';
    });

    startRandomBtn.addEventListener("click", spinSlotMachine);

    viewRandomDetailBtn.addEventListener("click", () => {
        if (selectedRandomResId) {
            randomModal.classList.add("hidden");
            openRestaurantDetail(selectedRandomResId);
        }
    });
}

function executeSearch() {
    const query = searchInput.value.trim();
    if (!query) {
        resetFilters();
        return;
    }
    
    document.querySelectorAll(".category-card").forEach(c => c.classList.remove("active"));
    currentCategory = "";
    renderMenuPills(null);
    
    resultsTitle.textContent = `"${query}" 검색 결과`;
    filterRestaurants();
}

function resetFilters() {
    searchInput.value = "";
    document.querySelectorAll(".category-card").forEach(c => c.classList.remove("active"));
    currentCategory = "";
    currentMenu = "";
    renderMenuPills(null);
    resultsTitle.textContent = "모든 맛집 목록";
    filterRestaurants();
}

function openRestaurantDetail(restaurantId) {
    const res = RESTAURANTS.find(r => r.id === restaurantId);
    if (!res) return;

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

                <div class="campus-map-wrapper">
                    <div class="map-title"><i class="fa-solid fa-map"></i> 고려대 캠퍼스 대비 위치</div>
                    <div class="campus-map">
                        <div class="map-bg-grid"></div>
                        <div class="map-landmark main-gate">고대 정문</div>
                        <div class="map-landmark library">중앙도서관</div>
                        <div class="map-landmark station-anam station">안암역 (6호선)</div>
                        <div class="map-landmark science-campus">이공대캠퍼스</div>
                        <div class="map-restaurant-pin" style="left: ${res.coords.x}%; top: ${res.coords.y}%;"></div>
                        <div class="map-restaurant-label" style="left: ${res.coords.x}%; top: ${res.coords.y}%;">${res.name}</div>
                    </div>
                </div>
            </div>

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

function spinSlotMachine() {
    startRandomBtn.disabled = true;
    randomResultCard.classList.add("hidden");
    
    const cat = randomCatSelect.value;
    let candidates = [...RESTAURANTS];
    if (cat) {
        candidates = candidates.filter(r => r.category === cat);
    }
    
    if (candidates.length === 0) {
        alert("해당 카테고리의 식당이 없습니다.");
        startRandomBtn.disabled = false;
        return;
    }
    
    const winnerIndex = Math.floor(Math.random() * candidates.length);
    const randomRes = candidates[winnerIndex];
    selectedRandomResId = randomRes.id;
    
    const spinNames = [];
    for (let i = 0; i < 15; i++) {
        const randIdx = Math.floor(Math.random() * candidates.length);
        spinNames.push(candidates[randIdx].name);
    }
    spinNames.push(randomRes.name);
    
    slotStrip.innerHTML = spinNames.map(name => `<div class="slot-item">${name}</div>`).join("");
    
    const itemHeight = 80;
    const totalTravel = (spinNames.length - 1) * itemHeight;
    
    slotStrip.style.transition = 'none';
    slotStrip.style.transform = 'translateY(0)';
    slotStrip.offsetHeight;
    
    slotStrip.style.transition = 'transform 2.5s cubic-bezier(0.1, 0.8, 0.2, 1)';
    slotStrip.style.transform = `translateY(-${totalTravel}px)`;
    
    setTimeout(() => {
        randomResBadge.textContent = randomRes.category;
        randomResName.textContent = randomRes.name;
        randomResRating.innerHTML = `<i class="fa-solid fa-star text-crimson"></i> ${randomRes.rating.toFixed(1)}`;
        randomResPrice.textContent = randomRes.price_range;
        randomResDesc.textContent = randomRes.description;
        
        randomResultCard.classList.remove("hidden");
        startRandomBtn.disabled = false;
    }, 2600);
}
