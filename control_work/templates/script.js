    // Обработчик события для формы добавления заметки
    document.getElementById("addForm").addEventListener("submit", event => {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию
        const title = document.getElementById("title").value;
        const message = document.getElementById("message").value;
        fetch("/add", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ title, message })
        })
            .then(response => response.json())
            .then(data => {
                console.log(data.message); // Выводим сообщение с сервера
                updateNotesList(); // Обновляем список заметок после добавления
            })
            .catch(error => {
                console.error("Ошибка при добавлении заметки:", error);
            });
    });

    // Обработчик события для формы фильтрации списка заметок
    document.getElementById("listForm").addEventListener("submit", event => {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию
        const date = document.getElementById("date").value;
        fetch(`/list?date=${date}`)
            .then(response => response.json())
            .then(notes => {
                updateNotesList(notes); // Обновляем список заметок с учетом фильтра
            })
            .catch(error => {
                console.error("Ошибка при фильтрации заметок:", error);
            });
    });

    // Обработчик события для формы чтения заметки
    document.getElementById("readForm").addEventListener("submit", event => {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию
        const note_id = document.getElementById("note_id").value;
        fetch(`/read?note_id=${note_id}`)
            .then(response => response.json())
            .then(note => {
                // Обновляем содержимое страницы с данными о заметке
                // Например, выводим заголовок и текст заметки в определенном элементе на странице
            })
            .catch(error => {
                console.error("Ошибка при чтении заметки:", error);
            });
    });

    // Обработчик события для формы редактирования заметки
    document.getElementById("editForm").addEventListener("submit", event => {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию
        const edit_note_id = document.getElementById("edit_note_id").value;
        const edit_title = document.getElementById("edit_title").value;
        const edit_message = document.getElementById("edit_message").value;
        fetch("/edit", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ edit_note_id, edit_title, edit_message })
        })
            .then(response => response.json())
            .then(data => {
                console.log(data.message); // Выводим сообщение с сервера
                updateNotesList(); // Обновляем список заметок после редактирования
            })
            .catch(error => {
                console.error("Ошибка при редактировании заметки:", error);
            });
    });

    // Обработчик события для формы удаления заметки
    document.getElementById("deleteForm").addEventListener("submit", event => {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию
        const delete_note_id = document.getElementById("delete_note_id").value;
        fetch(`/delete?note_id=${delete_note_id}`)
            .then(response => response.json())
            .then(data => {
                console.log(data.message); // Выводим сообщение с сервера
                updateNotesList(); // Обновляем список заметок после удаления
            })
            .catch(error => {
                console.error("Ошибка при удалении заметки:", error);
            });
    });

    // Функция для обновления списка заметок (получения данных с сервера)
    function updateNotesList(notes) {
        const notesList = document.getElementById("notesList");
        notesList.innerHTML = "";
        if (notes.length === 0) {
            notesList.innerHTML = "<li>Список заметок пуст.</li>";
        } else {
            notes.forEach(note => {
                const listItem = document.createElement("li");
                listItem.innerHTML = `${note.title} (${note.timestamp}): ${note.message}`;
                notesList.appendChild(listItem);
            });
        }
    }

    // Обновляем список заметок при загрузке страницы
    updateNotesList([]);

