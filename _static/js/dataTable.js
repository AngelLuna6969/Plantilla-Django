let dataTable;
let dataTableIsInitialized = false;

//Opciones de la dataTable
const dataTableOptions = {
    // scrollX: "2000px", //El escroll maximo por pagina
    // lengthMenu: [5, 10, 15, 20, 100, 200, 500], //La catidad del paginador
    // Opciones de columnas especificas
    columnDefs: [
        { className: "text-center", targets: [0, 1, 2, 3, 4, 5] }, //Columnas centradas
        { orderable: false, targets: [5] }, //Columnas que No se pueden ordernar
        // { searchable: false, targets: [1] }, //Columnas que No permityen busqueda
        // { width: "50%", targets: [0] } //Ancho de una columna
    ],
    // pageLength: 3, //Cantidad de registros especifica por cada pagina
    destroy: true, //Destruccion de la tabla por si se trabaja con registros asincronos
    // Opciones de lenguaje
    language: {
        lengthMenu: "Mostrar _MENU_ registros por página",
        zeroRecords: "Ningún usuario encontrado",
        info: "Mostrando de _START_ a _END_ de un total de _TOTAL_ registros",
        infoEmpty: "Ningún usuario encontrado",
        infoFiltered: "(filtrados desde _MAX_ registros totales)",
        search: "Buscar:",
        loadingRecords: "Cargando...",
        paginate: {
            first: "Primero",
            last: "Último",
            next: "Siguiente",
            previous: "Anterior"
        }
    }
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }
    await lista_modelo();
    dataTable = $('#datatable-modelos').DataTable(dataTableOptions); //Se remplazan dataTableOptions por {} para quitar las opciones
    dataTableIsInitialized = true;
};

const lista_modelo = async () => {
    try {
        const response = await fetch("/generales/api/");
        const data = await response.json();
        let content = ``;
        data.forEach((modelo, index) => {
            content += `
            <tr>
                <td>${modelo.id}</td>
                <td>${modelo.nombre}</td>
                <td>${modelo.descripcion}</td>
                <td>${modelo.fecha}</td>
                <td>${modelo.hora}</td>
                <td><a class="btn-tabla" href="/generales/modelo/ver/${modelo.id}"><i class="bi bi-eye-fill"></i></a></td>
            </tr>
            `;
        });
        tableBody.innerHTML = content;
    }
    catch (ex) {
        console.log(ex);
    }
}

window.addEventListener('load', async () => {
    await initDataTable();
});