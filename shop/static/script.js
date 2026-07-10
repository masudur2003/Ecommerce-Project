
/* ==========================================
            MyShop - Advanced JavaScript
========================================== */

document.addEventListener("DOMContentLoaded", () => {

    console.log("MyShop Loaded Successfully");

    /* =========================
          Dark Mode Toggle
    ========================= */

    const themeBtn = document.getElementById("themeToggle");

    if (localStorage.getItem("theme") === "dark") {
        document.body.classList.add("dark-mode");
        if(themeBtn){
            themeBtn.innerHTML = '<i class="fa-solid fa-sun"></i>';
        }
    }

    if(themeBtn){

        themeBtn.addEventListener("click", () => {

            document.body.classList.toggle("dark-mode");

            if(document.body.classList.contains("dark-mode")){

                localStorage.setItem("theme","dark");

                themeBtn.innerHTML =
                '<i class="fa-solid fa-sun"></i>';

            }else{

                localStorage.setItem("theme","light");

                themeBtn.innerHTML =
                '<i class="fa-solid fa-moon"></i>';

            }

        });

    }

    /* =========================
          Live Search
    ========================= */

    const searchInput = document.getElementById("searchInput");
    const searchBtn = document.getElementById("searchBtn");

    function searchProduct(){

        let keyword = searchInput.value.trim();

        if(keyword === ""){

            alert("Please enter a product name.");

            searchInput.focus();

            return;

        }

        alert("Searching for : " + keyword);

        // Django Version
        // window.location.href="/search/?q="+keyword;

    }

    if(searchBtn){

        searchBtn.addEventListener("click", searchProduct);

    }

    if(searchInput){

        searchInput.addEventListener("keypress",(e)=>{

            if(e.key==="Enter"){

                searchProduct();

            }

        });

    }

    /* =========================
         Active Menu
    ========================= */

    const navLinks =
    document.querySelectorAll(".nav-link");

    navLinks.forEach(link=>{

        link.addEventListener("click",function(){

            navLinks.forEach(item=>
                item.classList.remove("active"));

            this.classList.add("active");

        });

    });

    /* =========================
          Cart Badge Demo
    ========================= */

    let cartCount = 0;

    const badge =
    document.querySelector(".badge");

    const cartBtn =
    document.querySelector(".btn-warning");

    if(cartBtn){

        cartBtn.addEventListener("click",()=>{

            cartCount++;

            badge.innerText = cartCount;

        });

    }

    /* =========================
          Navbar Shadow
    ========================= */

    window.addEventListener("scroll",()=>{

        const navbar =
        document.querySelector(".navbar");

        if(window.scrollY > 50){

            navbar.style.boxShadow =
            "0 10px 30px rgba(0,0,0,.20)";

        }

        else{

            navbar.style.boxShadow =
            "none";

        }

    });

});

/* ==========================================
        Back To Top Button
========================================== */

const topBtn =
document.createElement("button");

topBtn.innerHTML =
'<i class="fa-solid fa-arrow-up"></i>';

topBtn.id="topBtn";

document.body.appendChild(topBtn);

topBtn.style.position="fixed";
topBtn.style.bottom="20px";
topBtn.style.right="20px";
topBtn.style.width="50px";
topBtn.style.height="50px";
topBtn.style.borderRadius="50%";
topBtn.style.border="none";
topBtn.style.display="none";
topBtn.style.cursor="pointer";
topBtn.style.zIndex="999";
topBtn.style.background="#0d6efd";
topBtn.style.color="#fff";

window.addEventListener("scroll",()=>{

    if(window.scrollY>300){

        topBtn.style.display="block";

    }

    else{

        topBtn.style.display="none";

    }

});

topBtn.addEventListener("click",()=>{

    window.scrollTo({

        top:0,

        behavior:"smooth"

    });

});



// Simple JS interaction

console.log("MyShop E-commerce site loaded successfully 🚀");

// Alert on button click (optional demo)
document.addEventListener("DOMContentLoaded", function () {

    let buttons = document.querySelectorAll(".btn-success");

    buttons.forEach(btn => {
        btn.addEventListener("click", function () {
            alert("Product added to cart 🛒");
        });
    });

});