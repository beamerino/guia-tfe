/* Checklist interactiva: guarda en el navegador de cada estudiante qué casillas
   ha marcado. Cada lista va dentro de <div class="checklist" data-id="...">.
   El progreso se comparte entre la versión en español y en inglés. */
(function () {
  var TEXTOS = {
    es: { de: "de", hecho: "hechos", reiniciar: "Desmarcar todo" },
    en: { de: "of", hecho: "done", reiniciar: "Clear all" }
  };

  function leer(clave) {
    try {
      var valor = window.localStorage.getItem(clave);
      return valor ? JSON.parse(valor) : [];
    } catch (e) {
      return [];
    }
  }

  function guardar(clave, estado) {
    try {
      window.localStorage.setItem(clave, JSON.stringify(estado));
    } catch (e) {
      /* Sin almacenamiento: la lista funciona igual, pero no recuerda */
    }
  }

  function montar(contenedor) {
    if (contenedor.dataset.montada) return;
    contenedor.dataset.montada = "1";

    var idioma = (document.documentElement.lang || "es").slice(0, 2);
    var t = TEXTOS[idioma] || TEXTOS.es;
    var clave = "guia-tfe:checklist:" + (contenedor.dataset.id || "general");
    var casillas = contenedor.querySelectorAll('.task-list-item input[type="checkbox"]');
    var estado = leer(clave);

    var barra = document.createElement("div");
    barra.className = "checklist-barra";
    barra.innerHTML =
      '<span class="checklist-texto"></span>' +
      '<div class="checklist-progreso"><span></span></div>' +
      '<button type="button" class="checklist-reiniciar"></button>';
    contenedor.insertBefore(barra, contenedor.firstChild);
    var texto = barra.querySelector(".checklist-texto");
    var relleno = barra.querySelector(".checklist-progreso > span");
    var boton = barra.querySelector(".checklist-reiniciar");
    boton.textContent = t.reiniciar;

    function actualizar() {
      var hechos = 0;
      casillas.forEach(function (c, i) {
        estado[i] = c.checked;
        var li = c.closest(".task-list-item");
        if (li) li.classList.toggle("hecho", c.checked);
        if (c.checked) hechos++;
      });
      texto.textContent = hechos + " " + t.de + " " + casillas.length + " " + t.hecho;
      relleno.style.width = casillas.length ? (100 * hechos / casillas.length) + "%" : "0";
      guardar(clave, estado);
    }

    casillas.forEach(function (c, i) {
      c.disabled = false;
      c.checked = !!estado[i];
      c.addEventListener("change", actualizar);
    });

    boton.addEventListener("click", function () {
      casillas.forEach(function (c) { c.checked = false; });
      actualizar();
    });

    actualizar();
  }

  function iniciar() {
    document.querySelectorAll(".md-typeset .checklist").forEach(montar);
  }

  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(iniciar);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", iniciar);
  } else {
    iniciar();
  }
})();
