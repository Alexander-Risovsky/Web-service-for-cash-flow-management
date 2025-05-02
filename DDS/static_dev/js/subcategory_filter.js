document.addEventListener('DOMContentLoaded', function () {
    const categorySelect = document.getElementById("id_category");
    const subcategorySelect = document.getElementById("id_subcategory");

    if (!categorySelect || !subcategorySelect || typeof window.urlGetSubcategories === 'undefined') {
        return; // выходим, если нужных элементов или URL нет
    }

    categorySelect.addEventListener("change", function () {
        const categoryId = this.value;
        subcategorySelect.innerHTML = '<option value="">---------</option>';

        if (categoryId) {
            fetch(`${window.urlGetSubcategories}?category_id=${categoryId}`)
                .then(response => response.json())
                .then(data => {
                    data.forEach(subcat => {
                        const option = document.createElement('option');
                        option.value = subcat.id;
                        option.textContent = subcat.name;
                        subcategorySelect.appendChild(option);
                    });
                });
        }
    });
});