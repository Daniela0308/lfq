// Obtenemos el contenedor donde vamos a pintar los equipos
document.addEventListener('DOMContentLoaded', () => {
    const grid = document.getElementById('grid')
})

// petición a la API
fetch('/api/equipos/')
//La respuesta viene como HTTP response, la convertimos a JSON
.then(response => response.json()) 
//recibimos los equipos y los recorremos con forEach
.then(data => {
    data.forEach(team => {
        // Variable donde guardaremos el HTML del logo
        let logoHTML = ''
        if (team.logo) {
        // Creamos el HTML de la imagen del equipo
            logoHTML = `
                <img src="${team.logo}" class="eq-avatar">
            `
        } else {
            logoHTML = `
                <div class="eq-avatar">
                    ${team.name.slice(0,2).toUpperCase()}
                </div>
            `
        }
        // Insertamos la tarjeta del equipo dentro del grid
        grid.innerHTML += `
            <div class="eq-card">
                <div class="eq-franja"></div>
                <div class="eq-content">
                    ${logoHTML}
                    <p class="eq-nombre">
                        ${team.name}
                    </p>
                    <p class="eq-ciudad">
                        📍 ${team.city ?? ''}
                    </p>
                    <div class="eq-acciones">
                        <button class="eq-btn">
                            ✏️
                        </button>
                        <button class="eq-btn">
                            👁️
                        </button>
                    </div>
                </div>
            </div>
        `
    })
})