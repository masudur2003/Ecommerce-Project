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