// Ждём полной загрузки DOM
document.addEventListener('DOMContentLoaded', function () {
    // Получаем элементы select для типа и категории
    const typeSelect = document.getElementById('id_type');
    const categorySelect = document.getElementById('id_category');

    // Проверяем, что элементы существуют и глобальная переменная с URL определена
    if (!categorySelect || !typeSelect || typeof window.urlGetcategories === 'undefined') {
        return;
    }

    // Вешаем обработчик на изменение значения типа
    typeSelect.addEventListener('change', function () {
        const typeId = this.value;
        // Делаем fetch-запрос для получения категорий по выбранному типу
        fetch(`${window.urlGetcategories}?type_id=${typeId}`)
            .then(response => response.json())
            .then(data => {
                // Очищаем текущие опции в select категории
                categorySelect.innerHTML = '';

                // Добавляем пустую опцию
                const emptyOption = document.createElement('option');
                emptyOption.value = '';
                emptyOption.textContent = '---------';
                categorySelect.appendChild(emptyOption);

                // Добавляем новые опции на основе полученных данных
                data.forEach(category => {
                    const option = document.createElement('option');
                    option.value = category.id;
                    option.textContent = category.name;
                    categorySelect.appendChild(option);
                });
            });
    });
});