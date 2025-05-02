document.addEventListener('DOMContentLoaded', function () {
    const typeSelect = document.getElementById('id_type');
    const categorySelect = document.getElementById('id_category');

    if (!categorySelect || !typeSelect || typeof window.urlGetcategories === 'undefined') {
        return;
    }

    typeSelect.addEventListener('change', function () {
        const typeId = this.value;
        fetch(`${window.urlGetcategories}?type_id=${typeId}`)
            .then(response => response.json())
            .then(data => {
                categorySelect.innerHTML = '';

                const emptyOption = document.createElement('option');
                emptyOption.value = '';
                emptyOption.textContent = '---------';
                categorySelect.appendChild(emptyOption);

                data.forEach(category => {
                    const option = document.createElement('option');
                    option.value = category.id;
                    option.textContent = category.name;
                    categorySelect.appendChild(option);
                });
            });
    });
});