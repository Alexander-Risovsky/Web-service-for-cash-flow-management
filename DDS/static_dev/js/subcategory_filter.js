// Ждём полной загрузки DOM
document.addEventListener('DOMContentLoaded', function () {
    // Получаем элементы select для категории и подкатегории
    const categorySelect = document.getElementById("id_category");
    const subcategorySelect = document.getElementById("id_subcategory");

    // Проверяем, что оба элемента и URL для запроса существуют
    if (!categorySelect || !subcategorySelect || typeof window.urlGetSubcategories === 'undefined') {
        return; // выходим, если нужных элементов или URL нет
    }

    // Вешаем обработчик на изменение значения категории
    categorySelect.addEventListener("change", function () {
        const categoryId = this.value;
        // Очищаем подкатегории и добавляем пустую опцию
        subcategorySelect.innerHTML = '<option value="">---------</option>';

        // Если выбрана категория, делаем запрос за подкатегориями
        if (categoryId) {
            fetch(`${window.urlGetSubcategories}?category_id=${categoryId}`)
                .then(response => response.json())
                .then(data => {
                    // Для каждой подкатегории создаём и добавляем опцию
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