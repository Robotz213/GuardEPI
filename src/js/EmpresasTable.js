window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple = document.getElementById('EmpresaTable');
    if (datatablesSimple) {
        new DataTable(datatablesSimple);
    }
});
