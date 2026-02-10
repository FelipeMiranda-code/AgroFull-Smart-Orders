$(document).foundation()
document.addEventListener("DOMContentLoaded", function () {
    
    console.log("💚 JS está funcionando");

    const botones = document.querySelectorAll(".btn-agregar");

    if (botones.length === 0) {
        console.log("⚠ No encontré botones con la clase: btn-agregar");
    }

    botones.forEach(boton => {
        boton.addEventListener("click", () => {
            const nombre = boton.getAttribute("data-producto");
            alert(`✔ Producto agregado: ${nombre}`);
        });
    });
});
