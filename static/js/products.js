document.addEventListener("DOMContentLoaded", function () {

    console.log("📌 products.js cargado correctamente");

    const botones = document.querySelectorAll(".btn-agregar");
    const inputs = document.querySelectorAll(".cantidad-input");

    // ✅ MENSAJE VISUAL
    function mostrarMensaje(texto) {
        const mensaje = document.createElement("div");
        mensaje.textContent = texto;
        mensaje.style.position = "fixed";
        mensaje.style.top = "20px";
        mensaje.style.right = "20px";
        mensaje.style.background = "#2d572c";
        mensaje.style.color = "white";
        mensaje.style.padding = "10px 18px";
        mensaje.style.borderRadius = "10px";
        mensaje.style.zIndex = "9999";
        mensaje.style.boxShadow = "0 4px 10px rgba(0,0,0,0.2)";
        mensaje.style.fontSize = "14px";

        document.body.appendChild(mensaje);

        setTimeout(() => {
            mensaje.remove();
        }, 1500);
    }

    // ✅ AGREGAR AL PEDIDO SIN BLOQUEAR BOTONES
    botones.forEach((boton, index) => {
        boton.addEventListener("click", () => {

            const productoId = boton.dataset.id;
            const cantidad = inputs[index].value;

            if (!cantidad || cantidad <= 0) {
                mostrarMensaje("⚠ Debes ingresar una cantidad válida");
                return;
            }

            fetch(`/pedidos/agregar/${productoId}/?cantidad=${cantidad}`)
                .then(response => response.json())
                .then(data => {
                    if (data.ok) {
                        mostrarMensaje("✅ Producto agregado al pedido");
                        inputs[index].value = 1; // vuelve a 1
                    } else {
                        mostrarMensaje("⚠ Error al agregar");
                    }
                });

        });
    });

});
